#!/usr/bin/env python3
"""Convert binary datasets to text on fetch, when they hold text.

Some datasets ship their data as parquet or pickle rather than csv/json. Those
are convertible if the payload is *data* (pandas can read them). This tool
downloads a dataset, writes any plain-text files as-is, converts parquet/pickle
payloads to .csv (+ a .md preview), and reports anything it cannot convert
(model artifacts, images). PDFs convert to .md when pypdf is installed.

Usage:
    python3 corpus/convert.py <dataset-id> [<dataset-id> ...]

Never unpickles blindly: a pickle is only read with pandas.read_pickle inside a
try/except; a model artifact (.pkl weights, vectorizer) is reported, not kept.
"""
import json
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://huggingface.co/api/datasets"
TEXT_EXT = {".csv", ".json", ".jsonl", ".ndjson", ".txt", ".tsv", ".xml"}


def slug(did):
    return did.replace("/", "__")


def tree(did):
    with urllib.request.urlopen(f"{API}/{did}/tree/main?recursive=true", timeout=60) as r:
        return json.load(r)


def fetch(did, path, dest):
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    url = f"https://huggingface.co/datasets/{did}/resolve/main/{path}"
    urllib.request.urlretrieve(url, dest)
    return dest


def convert(did):
    dest = os.path.join(HERE, slug(did))
    os.makedirs(dest, exist_ok=True)
    files = [e for e in tree(did) if e.get("type") == "file" and not e["path"].startswith(".")]
    notes = []
    for e in files:
        path = e["path"]
        ext = os.path.splitext(path)[1].lower()
        stem = os.path.splitext(os.path.basename(path))[0]
        if ext in TEXT_EXT:
            fetch(did, path, os.path.join(dest, path))
            notes.append(f"text kept: {path}")
            continue
        if ext == ".parquet":
            tmp = os.path.join(dest, ".tmp_" + os.path.basename(path))
            fetch(did, path, tmp)
            try:
                import pandas as pd
                df = pd.read_parquet(tmp)
                out = os.path.join(dest, f"{stem}.csv")
                df.to_csv(out, index=False)
                with open(os.path.join(dest, f"{stem}.md"), "w", encoding="utf-8") as f:
                    f.write(f"# {did} — {path}\n\nConverted from parquet. {len(df)} rows, columns: {', '.join(map(str, df.columns))}\n\n```\n")
                    f.write(df.head(20).to_string())
                    f.write("\n```\n")
                notes.append(f"converted parquet -> {stem}.csv + {stem}.md ({len(df)} rows)")
            except Exception as exc:  # noqa: BLE001
                notes.append(f"parquet {path}: could not convert ({exc})")
            finally:
                if os.path.exists(tmp):
                    os.remove(tmp)
            continue
        if ext in {".pkl", ".pickle"}:
            tmp = os.path.join(dest, ".tmp_" + os.path.basename(path))
            fetch(did, path, tmp)
            try:
                import pandas as pd
                obj = pd.read_pickle(tmp)
                out = os.path.join(dest, f"{stem}.csv")
                obj.to_csv(out, index=False) if hasattr(obj, "to_csv") else None
                notes.append(f"pickle -> {stem}.csv (data)") if hasattr(obj, "to_csv") else notes.append(f"pickle {path}: not tabular data, dropped")
            except Exception as exc:  # noqa: BLE001
                notes.append(f"pickle {path}: not data / model artifact, dropped ({type(exc).__name__})")
            finally:
                if os.path.exists(tmp):
                    os.remove(tmp)
            continue
        if ext == ".pdf":
            tmp = os.path.join(dest, ".tmp_" + os.path.basename(path))
            fetch(did, path, tmp)
            try:
                from pypdf import PdfReader
                text = "\n\n".join((p.extract_text() or "") for p in PdfReader(tmp).pages)
                with open(os.path.join(dest, f"{stem}.md"), "w", encoding="utf-8") as f:
                    f.write(f"# {did} — {path}\n\n{text}")
                notes.append(f"converted pdf -> {stem}.md")
            except Exception as exc:  # noqa: BLE001
                notes.append(f"pdf {path}: no extractor ({exc})")
            finally:
                if os.path.exists(tmp):
                    os.remove(tmp)
            continue
        notes.append(f"skipped non-text: {path}")
    print(f"\n{did}:")
    for n in notes:
        print("   ", n)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    for did in sys.argv[1:]:
        try:
            convert(did)
        except Exception as exc:  # noqa: BLE001
            print(f"{did}: FAILED {exc}")

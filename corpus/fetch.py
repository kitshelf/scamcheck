#!/usr/bin/env python3
"""Fetch indexed corpora on demand — stdlib only.

ScamCheck's corpus index (corpus/index.json) lists every scam/fraud/phishing/
spam dataset found on Hugging Face. This tool downloads one, or the top-N of a
category, without vendoring the whole surface into git.

Usage:
    python3 corpus/fetch.py <dataset-id>                 # one dataset
    python3 corpus/fetch.py --category phishing          # top 20 by downloads
    python3 corpus/fetch.py --category fraud -n 50       # top 50
    python3 corpus/fetch.py --list phishing              # list, no download
    python3 corpus/fetch.py <dataset-id> --max-mb 25     # skip files over 25 MB

Downloads land in corpus/<slug>/ (slug = dataset id with '/' -> '__').
Only call this for licenses you may redistribute; the index records each
dataset's license. Nothing here is trained on, and nothing runs inside a screen.
"""
import argparse
import json
import os
import sys
import urllib.request
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "index.json")
API = "https://huggingface.co/api/datasets"


def load_index():
    with open(INDEX, encoding="utf-8") as f:
        return json.load(f)


def slug(did):
    return did.replace("/", "__")


def tree(did):
    """List files (recursive) for a dataset."""
    url = f"{API}/{did}/tree/main?recursive=true"
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def download(did, max_mb=100):
    dest = os.path.join(HERE, slug(did))
    os.makedirs(dest, exist_ok=True)
    files = [e for e in tree(did) if e.get("type") == "file" and not e["path"].startswith(".")]
    total = 0
    for e in files:
        path, size = e["path"], e.get("size", 0)
        if max_mb and size > max_mb * 1_000_000:
            print(f"  skip {path} ({size/1e6:.1f} MB > {max_mb} MB cap)")
            continue
        out = os.path.join(dest, path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        url = f"https://huggingface.co/datasets/{did}/resolve/main/{path}"
        try:
            urllib.request.urlretrieve(url, out)
            total += size
            print(f"  got  {path} ({size/1e6:.2f} MB)")
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"  FAIL {path}: {exc}")
    print(f"{did}: {len(files)} files, ~{total/1e6:.1f} MB -> corpus/{slug(did)}/")


def main():
    ap = argparse.ArgumentParser(description="Fetch indexed ScamCheck corpora on demand.")
    ap.add_argument("dataset", nargs="?", help="Hugging Face dataset id, e.g. zefang-liu/phishing-email-dataset")
    ap.add_argument("--category", help="fetch the top-N by downloads in this category")
    ap.add_argument("-n", "--number", type=int, default=20, help="how many for --category (default 20)")
    ap.add_argument("--list", metavar="CATEGORY", help="list a category without downloading")
    ap.add_argument("--max-mb", type=int, default=100, help="skip individual files larger than this (default 100)")
    args = ap.parse_args()

    index = load_index()

    if args.list:
        rows = [(d, v) for d, v in index.items() if args.list in v["categories"]]
        rows.sort(key=lambda x: -x[1]["downloads"])
        for d, v in rows:
            print(f"{v['downloads']:>7}  {v['license']:<16} {d}")
        print(f"\n{len(rows)} datasets in '{args.list}'.")
        return

    if args.category:
        rows = [(d, v) for d, v in index.items() if args.category in v["categories"]]
        rows.sort(key=lambda x: -x[1]["downloads"])
        rows = rows[: args.number]
        print(f"Fetching {len(rows)} datasets from '{args.category}' ...")
        for d, _ in rows:
            download(d, args.max_mb)
        return

    if args.dataset:
        if args.dataset not in index:
            print(f"note: {args.dataset} is not in the index; fetching it anyway.")
        download(args.dataset, args.max_mb)
        return

    ap.print_help()
    sys.exit(2)


if __name__ == "__main__":
    main()

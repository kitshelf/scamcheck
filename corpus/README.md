# corpus/ — the learn-from library

Public scam, phishing, and spam message corpora, vendored under redistributable licenses, plus a full index of the Hugging Face surface. The material marker rubrics and packs are researched against, and the calibration reference the synthetic fixtures are judged by.

## The boundary (read this first)

| Tier | Where | What it is | Used for |
|---|---|---|---|
| Synthetic fixtures | `tests/fixtures/` | Invented messages, planted markers | The gauntlet — the kit is tested here |
| External corpora | `corpus/` (this folder) | Public datasets, downloaded as-is, text-only | Marker research, pack development, calibration review |
| Runtime | — | A user's pasted message | The screen. The kit never reads this folder during a screen |

The kit does not train on this corpus. The charter says **not a trained model**, and it stays that way.

## The full surface index

[`INDEX.md`](INDEX.md) + [`index.json`](index.json) index **1,051 datasets** across Hugging Face for this domain, categorized by PRD surface with license and download counts. Pull any of them on demand:

```sh
python3 corpus/fetch.py --list phishing       # list a category
python3 corpus/fetch.py --category phishing -n 20
python3 corpus/fetch.py <dataset-id>
```

Some datasets ship as parquet. Convert those to text on fetch (`convert.py` writes `.csv` + `.md` preview; model artifacts and images are dropped, nothing is ever blindly unpickled):

```sh
python3 corpus/convert.py <dataset-id>
```

## Contents — 21 vendored datasets

| Directory | License | Rows | What it is |
|---|---|---|---|
| `phishing-emails/` | LGPL-3.0 | 18,650 | full phishing + safe emails |
| `sms-spam-collection/` | CC-BY-4.0 | 5,572 | the classic SMS Spam Collection v.1 |
| `clair-fraud-emails/` | CC-BY-3.0 | 11,903 | CLAIR advance-fee fraud letters (Radev 2008) |
| `scam-dialogues/` | Apache-2.0 | 1,600 | 8-type synthetic scam dialogues |
| `scam-conversations-multi/` | Apache-2.0 | 1,600 | multi-agent variant, with scammer-personality column |
| `scam-conversations-single/` | Apache-2.0 | 1,600 | single-agent variant |
| `youtube-scam-conversations/` | Apache-2.0 | 20 | comment-section scams |
| `discord-scam-detection/` | MIT | 3,260 | Discord scam messages |
| `BothBosu__Scammer-Conversation/` | Apache-2.0 | 1,000 | scammer conversation transcripts (synthetic) |
| `DarkNeuron-AI__spam-sms-collection-01/` | MIT | 5,574 | spam SMS collection |
| `DatasetNewUser__Indian_Cyber_Scam_PhoneCall_Hinglish_Dataset/` | Apache-2.0 | 10,001 | Hinglish scam-call transcripts with `scam_category`, `urgency_level` |
| `Dizzzy0x00__LLMGen-Phishing-Email-Dataset/` | Apache-2.0 | 3,031 | LLM-generated phishing emails (synthetic; multilingual incl. Chinese) |
| `Bektemir96az96__Uzbek_and_Russian_Phishing_dataset/` | Apache-2.0 | 100,000 | Uzbek + Russian phishing texts |
| `bolewara__hinglish-scam-text-dataset/` | CC-BY-4.0 | 3,787 | Hinglish spam/ham SMS |
| `softecapps__spam_ham_spanish/` | Apache-2.0 | 1,207 | Spanish spam/ham SMS |
| `HyaDoo__ko-voicephishing-binary-classification/` | Apache-2.0 | 8,725 | Korean voice-phishing transcripts (converted from parquet) |
| `HyaDoo__ko-voicephishing-binary-classification-ver2/` | Apache-2.0 | 19,225 | the same, larger version |
| `HyaDoo__hd-bert-voicephishing-binary-classification-ver3/` | Apache-2.0 | 2,773 | Korean voice-phishing, variant set |
| `HyaDoo__hd-bert-voicephishing-binary-classification-ver4/` | Apache-2.0 | 4,173 | variant set |
| `HyaDoo__hd-bert-voicephishing-binary-classification-ver5/` | Apache-2.0 | 5,573 | variant set |
| `IRBXrocket__phishing-url/` | CC-BY-4.0 | paper | the phishing-URL research paper, converted to Markdown; its URL tables were dropped (URLs are not message text) |

Per-dataset provenance, exact ids, and the full removal record: [`MANIFEST.md`](MANIFEST.md). Every directory carries its source card as `README.md`.

## The learn-from protocol

1. **Sample.** Pull messages by label or dialogue `type`. The scam-dialogue types map onto kit families: `ssn` → identity extraction, `support` → tech-support, `delivery` → the package-fee opener, `wrong` → the wrong-number romance opener, `appointment` → the fake-booking bait, and `refund` / `reward` / `insurance` / `telemarketing` → the banking-adjacent baits. The multi-agent set adds a `personality` column — the scammer's scripted persona.
2. **Extract recurring tells.** What actually repeats in the scam messages — words, structure, asks.
3. **Draft the candidate marker.** Name, category, the tell, and — mandatory — the *not-a-marker-when* calibration line, tested against the safe/ham side of the same corpus.
4. **Review.** A marker enters a rubric or pack only with its calibration line, a source note, and a fixture that exercises it. Nothing auto-enters.

## Rules for this folder

- **Text formats only.** `.csv`, `.json`, `.jsonl`, `.ndjson`, `.txt`, `.tsv`, `.xml`, `.md`. Binaries never come in *as binaries* — parquet and data-pickles convert to text first (`convert.py`); model artifacts, images, and audio are dropped. `fetch.py` enforces this by default.
- **No gated datasets.** A 401 on download means it does not come in.
- **No mirrors.** Datasets are deduplicated by content hash before vendoring; a mirror of an already-vendored set is deleted, not kept twice.
- Never add a corpus without license and provenance in `MANIFEST.md`. An unclear license means it does not come in.
- Never use corpus material as a fixture, and never paste corpus messages into a user's screen.
- Keep the manifest accurate: row counts, dates, exact Hugging Face ids.

# corpus/ — external research corpora

Public scam, phishing, and spam message corpora, downloaded from Hugging Face on 2026-11-20. This folder is the kit's **learn-from library**: the material marker rubrics and packs are researched against, and the calibration reference the synthetic fixtures are judged by.

## The boundary (read this first)

| Tier | Where | What it is | Used for |
|---|---|---|---|
| Synthetic fixtures | `tests/fixtures/` | Invented messages, planted markers | The gauntlet — the kit is tested here |
| External corpora | `corpus/` (this folder) | Public research corpora, downloaded as-is | Marker research, pack development, calibration review |
| Runtime | — | A user's pasted message | The screen. The kit never reads this folder during a screen |

The kit does not train on this corpus. The charter says **not a trained model**, and it stays that way. This is a research library for humans and agents writing rubrics — and a public resource for anyone building a classifier as a *separate* project.

## Contents

| Corpus | Source (Hugging Face) | License | Rows | Shape |
|---|---|---|---|---|
| `phishing-emails/` | `zefang-liu/phishing-email-dataset` | LGPL-3.0 | 18,650 — 7,328 phishing / 11,322 safe | full emails: `Email Text`, `Email Type` |
| `sms-spam-collection/` | `codesignal/sms-spam-collection` | CC-BY-4.0 | 5,572 — 747 spam / 4,825 ham | SMS bodies: `label`, `message` |
| `scam-dialogues/` | `BothBosu/scam-dialogue` | Apache-2.0 | 1,600 dialogues — 800 scam / 800 not, 8 scam types | multi-turn: `dialogue`, `type`, `label`. **Synthetic** (generated, labeled) |
| `clair-fraud-emails/` | `tasksource/CLAIR_email_fraud` | CC-BY-3.0 | 11,903 — 5,171 FRAUD / 6,732 NOT_FRAUD (train/dev/test) | fraud letters, JSONL: `label`, `text` |

Per-dataset provenance, attribution, and exact licenses: [`MANIFEST.md`](MANIFEST.md).

## The learn-from protocol

How a marker earns its way from this corpus into a rubric or pack:

1. **Sample.** Pull messages by label or dialogue `type`. The eight dialogue types map cleanly onto scam families: `ssn` → identity extraction, `support` → tech-support, `delivery` → package-fee, `wrong` → the wrong-number opener, and `refund` / `reward` / `insurance` / `telemarketing` → the banking-adjacent baits.
2. **Extract recurring tells.** What actually repeats in the scam messages — words, structure, asks — not what a summary claims repeats.
3. **Draft the candidate marker.** Name, category, the tell, and — mandatory — the *not-a-marker-when* calibration line, tested against the safe/ham side of the same corpus.
4. **Review.** A marker enters a rubric or pack only with its calibration line, a source note, and a fixture that exercises it. Nothing auto-enters.

## Rules for this folder

- Never add a corpus without license and provenance in `MANIFEST.md`. An unclear license means it does not come in.
- Never use corpus material as a fixture. Fixtures are authored, synthetic, planted; corpus is downloaded, as-is.
- Never paste corpus messages into a user's screen or treat them as a user's material.
- Keep the manifest accurate: row counts, dates, exact Hugging Face ids.

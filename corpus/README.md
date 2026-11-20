# corpus/ — external research corpora

Public scam, phishing, and spam message corpora, downloaded from Hugging Face on 2026-11-20. This folder is the kit's **learn-from library**: the material marker rubrics and packs are researched against, and the calibration reference the synthetic fixtures are judged by.

## The boundary (read this first)

| Tier | Where | What it is | Used for |
|---|---|---|---|
| Synthetic fixtures | `tests/fixtures/` | Invented messages, planted markers | The gauntlet — the kit is tested here |
| External corpora | `corpus/` (this folder) | Public research corpora, downloaded as-is | Marker research, pack development, calibration review |
| Runtime | — | A user's pasted message | The screen. The kit never reads this folder during a screen |

The kit does not train on this corpus. The charter says **not a trained model**, and it stays that way. This is a research library for humans and agents writing rubrics — and a public resource for anyone building a classifier as a *separate* project.

## The full surface index

Beyond the vendored datasets below, [`INDEX.md`](INDEX.md) and [`index.json`](index.json) index the **whole Hugging Face surface** for this domain — **1,051 datasets**, categorized (jobs, rentals, banking, marketplace, romance, phishing, spam, fraud, social-engineering, robocall), with license and download counts. Pull any of them on demand:

```sh
python3 corpus/fetch.py --list phishing       # list a category
python3 corpus/fetch.py --category phishing -n 20
python3 corpus/fetch.py <dataset-id>
```

The index is metadata only — nothing is vendored wholesale, because 1,000 datasets in git is multiple gigabytes. The vendored sets below are the verified, redistributable, message-level ones.

## Contents

| Corpus | Source (Hugging Face) | License | Rows | Shape |
|---|---|---|---|---|
| `phishing-emails/` | `zefang-liu/phishing-email-dataset` | LGPL-3.0 | 18,650 — 7,328 phishing / 11,322 safe | full emails: `Email Text`, `Email Type` |
| `sms-spam-collection/` | `codesignal/sms-spam-collection` | CC-BY-4.0 | 5,572 — 747 spam / 4,825 ham | SMS bodies: `label`, `message` |
| `scam-dialogues/` | `BothBosu/scam-dialogue` | Apache-2.0 | 1,600 dialogues — 800 scam / 800 not, 8 scam types | multi-turn: `dialogue`, `type`, `label`. **Synthetic** (generated, labeled) |
| `scam-conversations-multi/` | `BothBosu/multi-agent-scam-conversation` | Apache-2.0 | 1,600 dialogues, 8 scam types | multi-agent: `dialogue`, `personality`, `type`, `labels` — a scammer **personality** per row. Synthetic |
| `scam-conversations-single/` | `BothBosu/single-agent-scam-conversations` | Apache-2.0 | 1,600 dialogues, 8 scam types | `dialogue`, `type`, `labels`. Synthetic |
| `youtube-scam-conversations/` | `BothBosu/youtube-scam-conversations` | Apache-2.0 | 20 dialogues | `dialogue`, `type`, `call`, `link`, `channel`, `labels` — comment-section scams |
| `discord-scam-detection/` | `DQN-Labs/discord_scam_detection` | MIT | 3,260 messages | `label`, `msg_content` |
| `clair-fraud-emails/` | `tasksource/CLAIR_email_fraud` | CC-BY-3.0 | 11,903 — 5,171 FRAUD / 6,732 NOT_FRAUD (train/dev/test) | fraud letters, JSONL: `label`, `text` |

Per-dataset provenance, attribution, and exact licenses: [`MANIFEST.md`](MANIFEST.md).

## The learn-from protocol

How a marker earns its way from this corpus into a rubric or pack:

1. **Sample.** Pull messages by label or dialogue `type`. The scam-dialogue `type` values map cleanly onto scam families: `ssn` → identity extraction, `support` → tech-support, `delivery` → the package-fee opener, `wrong` → the wrong-number romance opener, `appointment` → the fake-booking bait, and `refund` / `reward` / `insurance` / `telemarketing` → the banking-adjacent baits. The multi-agent set adds a **`personality`** column — the scammer's scripted persona, useful for studying how tone is matched to victim.
2. **Extract recurring tells.** What actually repeats in the scam messages — words, structure, asks — not what a summary claims repeats.
3. **Draft the candidate marker.** Name, category, the tell, and — mandatory — the *not-a-marker-when* calibration line, tested against the safe/ham side of the same corpus.
4. **Review.** A marker enters a rubric or pack only with its calibration line, a source note, and a fixture that exercises it. Nothing auto-enters.

## Rules for this folder

- Never add a corpus without license and provenance in `MANIFEST.md`. An unclear license means it does not come in.
- Never use corpus material as a fixture. Fixtures are authored, synthetic, planted; corpus is downloaded, as-is.
- Never paste corpus messages into a user's screen or treat them as a user's material.
- Keep the manifest accurate: row counts, dates, exact Hugging Face ids.

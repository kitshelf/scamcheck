# Corpus manifest

Provenance, license, and counts for every external corpus in this folder. Downloaded from Hugging Face on **2026-11-20**. One owner: this file. All files are stored as-is, unmodified from their source repositories.

---

## phishing-emails/

| Field | Value |
|---|---|
| Hugging Face id | `zefang-liu/phishing-email-dataset` |
| License | LGPL-3.0 |
| Files | `Phishing_Email.csv` (50 MB) |
| Rows | 18,650 — 7,328 "Phishing Email" / 11,322 "Safe Email" |
| Schema | `Email Text`, `Email Type` (first column is an unnamed index) |
| Provenance | A direct copy of the "Phishing Email Detection" dataset from Kaggle, created by the Kaggle user "Cyber Cop" (subhajournal), redistributed on Hugging Face by zefang-liu under LGPL-3.0. Source: [HF card](https://huggingface.co/datasets/zefang-liu/phishing-email-dataset) · [original Kaggle page](https://www.kaggle.com/datasets/subhajournal/phishingemails) |
| Note | Read with `csv.field_size_limit` raised; some email bodies exceed the default. Encoding: UTF-8 with replacement. |

## sms-spam-collection/

| Field | Value |
|---|---|
| Hugging Face id | `codesignal/sms-spam-collection` |
| License | CC-BY-4.0 |
| Files | `sms-spam-collection.csv` (470 KB) |
| Rows | 5,572 — 747 spam / 4,825 ham |
| Schema | `label`, `message` |
| Provenance | The classic **SMS Spam Collection v.1** (Almeida & Hidalgo), a public research corpus of SMS messages tagged ham/spam, uploaded by codesignal under CC-BY-4.0. Source: [HF card](https://huggingface.co/datasets/codesignal/sms-spam-collection) |
| Attribution required | CC-BY-4.0 — credit the collection authors and the uploader when redistributing. |

## scam-dialogues/

| Field | Value |
|---|---|
| Hugging Face id | `BothBosu/scam-dialogue` |
| License | Apache-2.0 |
| Files | `scam-dialogue_all.csv` (2.2 MB; train/test splits exist upstream, `all` includes both) |
| Rows | 1,600 dialogues — 800 scam (`label=1`) / 800 not (`label=0`) |
| Schema | `dialogue`, `type`, `label` (file carries a UTF-8 BOM — read as `utf-8-sig`) |
| Types | 8 scam types, 200 each: `ssn`, `refund`, `support`, `reward`, `delivery`, `insurance`, `telemarketing`, `wrong` |
| Provenance | **Synthetic** — generated, labeled multi-turn scam dialogues by BothBosu, Apache-2.0. Source: [HF card](https://huggingface.co/datasets/BothBosu/scam-dialogue) |
| Note | Generated, not real transcripts. Consistent with this kit's fixtures-are-synthetic ethos, but it is corpus (learn-from material), never a fixture. |

## scam-conversations-multi/

| Field | Value |
|---|---|
| Hugging Face id | `BothBosu/multi-agent-scam-conversation` |
| License | Apache-2.0 · **synthetic** |
| Files | `agent_conversation_all.csv` (4.6 MB) |
| Rows | 1,600 dialogues, 200 per type |
| Schema | `dialogue`, `personality`, `type`, `labels` — a scammer **personality** column makes this the richest playbook corpus here |
| Types | `ssn`, `reward`, `refund`, `support`, `delivery`, `appointment`, `insurance`, `wrong` (note `appointment`, not in the other sets) |
| Provenance | Synthetic multi-agent scam conversations by BothBosu, Apache-2.0. Source: [HF card](https://huggingface.co/datasets/BothBosu/multi-agent-scam-conversation) |

## scam-conversations-single/

| Field | Value |
|---|---|
| Hugging Face id | `BothBosu/single-agent-scam-conversations` |
| License | Apache-2.0 · **synthetic** |
| Files | `single-agent-scam-dialogue_all.csv` (2.3 MB) |
| Rows | 1,600 dialogues, 200 per type |
| Schema | `dialogue`, `type`, `labels` |
| Types | same 8 as `scam-dialogues/` |
| Provenance | Synthetic, BothBosu, Apache-2.0. Source: [HF card](https://huggingface.co/datasets/BothBosu/single-agent-scam-conversations) |

## youtube-scam-conversations/

| Field | Value |
|---|---|
| Hugging Face id | `BothBosu/youtube-scam-conversations` |
| License | Apache-2.0 |
| Files | `youtube_scam_conversations.csv` (54 KB) |
| Rows | 20 dialogues |
| Schema | `dialogue`, `type`, `call`, `link`, `channel`, `labels` — comment-section and channel scams |
| Provenance | BothBosu, Apache-2.0. Source: [HF card](https://huggingface.co/datasets/BothBosu/youtube-scam-conversations) |

## discord-scam-detection/

| Field | Value |
|---|---|
| Hugging Face id | `DQN-Labs/discord_scam_detection` |
| License | MIT |
| Files | `data_balanced.csv` (265 KB) |
| Rows | 3,260 messages |
| Schema | `label`, `msg_content` |
| Provenance | DQN-Labs, MIT. Source: [HF card](https://huggingface.co/datasets/DQN-Labs/discord_scam_detection) |

## clair-fraud-emails/

| Field | Value |
|---|---|
| Hugging Face id | `tasksource/CLAIR_email_fraud` |
| License | CC-BY-3.0 |
| Files | `train.json` (11 MB), `dev.json` (1.1 MB), `test.json` (2.3 MB) — JSONL |
| Rows | 11,903 total — train 8,980 (3,914 FRAUD / 5,066 NOT_FRAUD), dev 997 (401 / 596), test 1,926 (856 / 1,070) |
| Schema | JSONL: `label` (`FRAUD` / `NOT_FRAUD`), `text` |
| Provenance | The **CLAIR Collection of Fraud Email**, Dragomir Radev, 2008, ACL Data and Code Repository (ADCR2008T001) — the classic research collection of advance-fee fraud letters. This copy by tasksource under CC-BY-3.0. Source: [HF card](https://huggingface.co/datasets/tasksource/CLAIR_email_fraud) · [ACL wiki](https://aclweb.org/aclwiki/CLAIR_collection_of_fraud_email_(Repository)) |
| Citation | Radev, D. (2008). CLAIR Collection of Fraud Email. ACL Data and Code Repository, ADCR2008T001. |

---

## Considered and rejected

| Candidate | Why it did not come in |
|---|---|
| `FredZhang7/all-scam-spam` (Apache-2.0) | 67 MB of generic junk-mail/spam — size plus scope: bulk spam is not scam signatures |
| `David-Egea/phishing-texts` (MIT) | Content unclear on inspection — the sample was linguistics mailing-list text, not phishing messages |
| `Shouninger/ScamBench` (CC-BY-NC-4.0) | Non-commercial clause conflicts with clean redistribution alongside this kit's MIT code license |
| `ucirvine/sms_spam` (license: unknown) | Same underlying corpus as `codesignal/sms-spam-collection`; the CC-BY-4.0 copy has the clear license, so it wins |
| `ealvaradob/phishing-dataset` (Apache-2.0) | URLs, not message bodies — markers here read words, not domains |
| social-engineering Q&A sets (`smd20/*`, `nezamisafa/*`) | Question-and-answer study material, not messages or tactic playbooks — thin for marker research |
| `shakeleoatmeal/phone-scam-detection-synthetic` (MIT) | Parquet-only; the same pattern space is covered by the CSV corpora above without a pyarrow dependency |
| MITRE ATT&CK sets (`sarahwei/*`, `CIRCL/*`) | Enterprise cyber-attack techniques (TTPs), not consumer scam messaging — a different problem space |

## Totals

| Measure | Value |
|---|---|
| Datasets | 8 |
| Messages / dialogues | ~43,000 |
| On-disk size | ~72 MB |
| License range | LGPL-3.0, CC-BY-4.0, Apache-2.0, CC-BY-3.0, MIT — all redistributable with attribution |

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

## Totals

| Measure | Value |
|---|---|
| Datasets | 4 |
| Messages/dialogues | ~37,725 |
| On-disk size | ~67 MB |
| License range | LGPL-3.0, CC-BY-4.0, Apache-2.0, CC-BY-3.0 — all redistributable with attribution |

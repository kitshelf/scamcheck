# Corpus manifest

Provenance, license, and counts for every vendored dataset. One owner: this file. All data files are stored as-is from their source repositories (parquet converts to `.csv` + `.md` via `convert.py`, noted per row); every directory carries the source's own card as `README.md`. Vendored on 2026-11-20.

---

## Vendored — 21 datasets

| Directory | Hugging Face id | License | Rows | What it is / notes |
|---|---|---|---|---|
| `phishing-emails/` | `zefang-liu/phishing-email-dataset` | LGPL-3.0 | 18,650 | 7,328 phishing / 11,322 safe emails. Direct copy of Kaggle's "Phishing Email Detection" by user Cyber Cop (subhajournal). Read with raised `csv.field_size_limit` |
| `sms-spam-collection/` | `codesignal/sms-spam-collection` | CC-BY-4.0 | 5,572 | 747 spam / 4,825 ham. The classic SMS Spam Collection v.1 (Almeida & Hidalgo). Attribution required |
| `clair-fraud-emails/` | `tasksource/CLAIR_email_fraud` | CC-BY-3.0 | 11,903 | 5,171 FRAUD / 6,732 NOT_FRAUD (train/dev/test JSONL). CLAIR Collection of Fraud Email, Dragomir Radev, 2008, ACL Data and Code Repository ADCR2008T001 |
| `scam-dialogues/` | `BothBosu/scam-dialogue` | Apache-2.0 | 1,600 | 800 scam / 800 not; 8 types × 200. **Synthetic** (generated, labeled). BOM file: read `utf-8-sig` |
| `scam-conversations-multi/` | `BothBosu/multi-agent-scam-conversation` | Apache-2.0 | 1,600 | 8 types × 200, adds a scammer-`personality` column and the `appointment` type. **Synthetic** |
| `scam-conversations-single/` | `BothBosu/single-agent-scam-conversations` | Apache-2.0 | 1,600 | 8 types × 200, single-agent variant. **Synthetic** |
| `youtube-scam-conversations/` | `BothBosu/youtube-scam-conversations` | Apache-2.0 | 20 | Comment-section and channel scams, with `call`, `link`, `channel` columns |
| `discord-scam-detection/` | `DQN-Labs/discord_scam_detection` | MIT | 3,260 | `label` + `msg_content` Discord messages |
| `BothBosu__Scammer-Conversation/` | `BothBosu/Scammer-Conversation` | Apache-2.0 | 1,000 | Scammer conversation transcripts (`gen_conver_noIdentifier_1000.csv`). **Synthetic** |
| `DarkNeuron-AI__spam-sms-collection-01/` | `DarkNeuron-AI/spam-sms-collection-01` | MIT | 5,574 | Spam SMS collection |
| `DatasetNewUser__Indian_Cyber_Scam_PhoneCall_Hinglish_Dataset/` | `DatasetNewUser/Indian_Cyber_Scam_PhoneCall_Hinglish_Dataset` | Apache-2.0 | 10,001 | Hinglish scam-call transcripts with `scam_category`, `caller_type`, `urgency_level` |
| `Dizzzy0x00__LLMGen-Phishing-Email-Dataset/` | `Dizzzy0x00/LLMGen-Phishing-Email-Dataset` | Apache-2.0 | 3,031 | LLM-generated phishing emails (`content`, `label`). **Synthetic**; multilingual incl. Chinese |
| `Bektemir96az96__Uzbek_and_Russian_Phishing_dataset/` | `Bektemir96az96/Uzbek_and_Russian_Phishing_dataset` | Apache-2.0 | 100,000 | Uzbek + Russian phishing texts. Language: uz/ru |
| `bolewara__hinglish-scam-text-dataset/` | `bolewara/hinglish-scam-text-dataset` | CC-BY-4.0 | 3,787 | Hinglish spam/ham SMS (`data.json` → `rows[].text`, `rows[].label`) |
| `softecapps__spam_ham_spanish/` | `softecapps/spam_ham_spanish` | Apache-2.0 | 1,207 | Spanish spam/ham SMS (train/test). Language: es |
| `HyaDoo__ko-voicephishing-binary-classification/` | `HyaDoo/ko-voicephishing-binary-classification` | Apache-2.0 | 8,725 | Korean voice-phishing transcripts. **Converted from parquet** → `train-dataset.csv` + `.md` |
| `HyaDoo__ko-voicephishing-binary-classification-ver2/` | `HyaDoo/ko-voicephishing-binary-classification-ver2` | Apache-2.0 | 19,225 | Same corpus, larger version. **Converted from parquet** |
| `HyaDoo__hd-bert-voicephishing-binary-classification-ver3/` | `HyaDoo/hd-bert-voicephishing-binary-classification-ver3` | Apache-2.0 | 2,773 | Korean voice-phishing variant set. **Converted from parquet** |
| `HyaDoo__hd-bert-voicephishing-binary-classification-ver4/` | `HyaDoo/hd-bert-voicephishing-binary-classification-ver4` | Apache-2.0 | 4,173 | Variant set. **Converted from parquet** |
| `HyaDoo__hd-bert-voicephishing-binary-classification-ver5/` | `HyaDoo/hd-bert-voicephishing-binary-classification-ver5` | Apache-2.0 | 5,573 | Variant set. **Converted from parquet** |
| `IRBXrocket__phishing-url/` | `IRBXrocket/phishing-url` | CC-BY-4.0 | paper | Research paper on phishing-URL lexical detection, converted to `2010.12847.md`. Its URL tables were dropped — URLs are not message text |

## Removed in the 2026-11-20 cleanup (with reasons)

| Removed | Reason |
|---|---|
| `BothBosu__scam-dialogue`, `scam-conversations-multi`-slug, `scam-conversations-single`-slug, `youtube`-slug, `tasksource__CLAIR_email_fraud`, `DQN-Labs__discord_scam_detection` | Mirrors of the vendored named dirs — **content-hash-verified identical** (the `_all` files are byte-equal), deleted after their README cards were copied into the named dirs |
| `436-4__scam-dialogue`, `436-4__youtube-scam-conversations` | Mirrors of the BothBosu sets (hash-verified twins) |
| `Advait456__CLAIR_email_fraud` | Mirror of tasksource CLAIR (hash-verified twin) |
| `DarkNeuronAI__spam-sms-collection-01` | Byte-identical twin of `DarkNeuron-AI__spam-sms-collection-01` (kept one) |
| `HyaDoo__hd-bert-voicephishing-binary-classification` | Empty shell — gated data (401 on download); the ver3–ver5 sets carry the real data |
| `Fraudcoins__crypto-holder-concentration` | Off-surface: blockchain concentration analytics, not scam messages |
| `ClarusC64__self-deception-detection-v0.1` | Off-surface: deception-psychology prompts, not scam messages |
| `BluefinTuna__scam-finetune-v1` | Off-surface: model-finetuning prompt/completion pairs, not raw messages |
| `mstz__spambase` | Not message text: numeric word-frequency feature vectors |
| `CiferAI__cifer-fraud-detection-mini-dataset` | Trivial: 20-row mini sample |
| `AI-ML-Research__sms-spam`, `Ivan000__SpamFilterTrainSet`, `87praveen33__Spam-Detection-500` | Trivial: toy sets (<15 KB / 500 msgs) |
| `Gamortsey__Phishing_Urls` | URLs, not message bodies |
| `IRBXrocket__phishing-url/*.csv` | URL tables dropped; the converted research paper stays |
| 22 binary files (parquet/pkl/pdf/png) + 19 data-less shells | Text-only doctrine; the convertible parquet was re-fetched and converted to text instead |

## Considered and rejected (never vendored)

| Candidate | Why it did not come in |
|---|---|
| `FredZhang7/all-scam-spam` (Apache-2.0) | 67 MB of generic junk-mail/spam — size plus scope: bulk spam is not scam signatures |
| `David-Egea/phishing-texts` (MIT) | Content unclear on inspection — the sample was linguistics mailing-list text |
| `Shouninger/ScamBench` (CC-BY-NC-4.0) | Non-commercial clause conflicts with this kit's MIT code license |
| `ucirvine/sms_spam` (unknown) | Same underlying corpus as `codesignal/sms-spam-collection`; the CC-BY-4.0 copy has the clear license |
| `ealvaradob/phishing-dataset` (Apache-2.0) | URLs, not message bodies |
| social-engineering Q&A sets (`smd20/*`, `nezamisafa/*`) | Study Q&A material, not messages or tactic playbooks |
| `shakeleoatmeal/phone-scam-detection-synthetic` (MIT) | Parquet-only at the time; covered by other call-transcript corpora |
| MITRE ATT&CK sets (`sarahwei/*`, `CIRCL/*`) | Enterprise cyber-attack TTPs, not consumer scam messaging |
| The NC-licensed and non-English-without-license sets from the surface sweep | Redistribution terms unclear alongside this kit's MIT license |

## Totals

| Measure | Value |
|---|---|
| **Indexed (whole HF surface)** | **1,051 datasets** — [`INDEX.md`](INDEX.md) / [`index.json`](index.json) |
| Vendored datasets | 21 |
| Vendored messages / dialogues | ~169,000 |
| Vendored on-disk size | ~134 MB |
| File types vendored | text only: `.csv`, `.json`, `.md` (+ converted parquet) |
| Vendored license range | LGPL-3.0, CC-BY-4.0, CC-BY-3.0, Apache-2.0, MIT — all redistributable with attribution |

## Surface reality (per category)

From the index: **fraud 375 · phishing 166 · spam 160 · banking 104** clear the 50+ bar; **jobs 26 · social-engineering 18 · robocall 17 · marketplace 7 · romance 6 · rentals 1** do not — those public corpora simply do not exist on Hugging Face. The niche PRD families are covered by the researched pack markers (`../packs/`), sourced from regulator guidance, which is the right authority for them.

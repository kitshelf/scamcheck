# Corpus surface index

**1051 datasets** discovered across Hugging Face for the scam / fraud / phishing / spam / social-engineering surface, as of 2026-11-20.

This is the *index* — metadata for the whole surface. A handful are vendored in this folder (see `MANIFEST.md`); the rest are fetched on demand with `fetch.py`. Nothing here is trained on, and nothing here runs inside a screen.

Machine-readable: [`index.json`](index.json) — `{id: {downloads, license, categories}}`.

## Coverage by category

| Category | Datasets | 50+? |
|---|---|---|
| jobs | 26 | no — HF has no more |
| rentals | 1 | no — HF has no more |
| banking | 104 | yes |
| marketplace | 7 | no — HF has no more |
| romance | 6 | no — HF has no more |
| phishing | 166 | yes |
| spam | 160 | yes |
| fraud | 375 | yes |
| social-engineering | 18 | no — HF has no more |
| robocall | 17 | no — HF has no more |
| uncategorized | 299 | yes |

A dataset can sit in several categories. The PRD families (jobs, rentals, banking, marketplace, romance) have far fewer public corpora than the cross-cutting categories (fraud, phishing, spam) — that is an inventory fact, not a search gap.

## License spread

| License | Datasets |
|---|---|
| unknown | 611 |
| mit | 136 |
| apache-2.0 | 119 |
| other | 50 |
| cc-by-4.0 | 44 |
| cc-by-nc-4.0 | 15 |
| gpl | 14 |
| cc | 10 |
| cc0-1.0 | 9 |
| cc-by-nc-nd-4.0 | 6 |
| lgpl-3.0 | 5 |
| cc-by-sa-4.0 | 5 |
| openrail | 4 |
| creativeml-openrail-m | 3 |
| gpl-3.0 | 3 |
| wtfpl | 3 |
| cc-by-3.0 | 2 |
| ecl-2.0 | 2 |
| openrail++ | 1 |
| afl-3.0 | 1 |
| bsd | 1 |
| bigscience-bloom-rail-1.0 | 1 |
| pddl | 1 |
| gemma | 1 |
| cc-by-nc-sa-4.0 | 1 |
| eupl-1.1 | 1 |
| odbl | 1 |
| unlicense | 1 |

**Redistribution rule:** only clearly-redistributable licenses (MIT, Apache-2.0, CC-BY, CC0, GPL/LGPL) are vendored. The `unknown` bucket is indexed for reference; check a dataset's own card before redistributing it.

## Top of each category (by downloads)

### jobs

| Dataset | Downloads | License |
|---|---|---|
| `victor/real-or-fake-fake-jobposting-prediction` | 729 | cc0-1.0 |
| `multabench/core-text-cls-fake-job-posting` | 281 | unknown |
| `agnialf/Internship-Job-Scam-Dataset` | 93 | unknown |
| `gplsi/fake_job_postings_balanced_en` | 88 | cc-by-4.0 |
| `sohaibdevv/Tech-Job-Scams-and-Predatory-Recruitment` | 47 | cc-by-4.0 |
| `Aurthor/fake_job_post_prediction` | 33 | unknown |
| `haoxianc/shivamb_real-or-fake-fake-jobposting-prediction` | 31 | cc0-1.0 |
| `Fernandosr85/adaption-job-scam-detection` | 27 | unknown |

### rentals

| Dataset | Downloads | License |
|---|---|---|
| `Gopher-Lab/huberman_lab_Dr__Becky_Kennedy_Protocols_for_Excellent_Parenting__Improving_Relationships_of_All` | 55 | unknown |

### banking

| Dataset | Downloads | License |
|---|---|---|
| `David-Egea/Creditcard-fraud-detection` | 1039 | mit |
| `BaekRok/vishing_data_3` | 601 | unknown |
| `VanshGoel1/fraud-hunter-case-bank` | 530 | unknown |
| `shariul-islam/bengali-sms-smishing-dataset` | 230 | mit |
| `MOZNLP/MOZ-Smishing` | 205 | creativeml-openrail-m |
| `dazzle-nu/CIS435-CreditCardFraudDetection` | 200 | unknown |
| `jmjmjm3/kor-smishing-message` | 193 | cc-by-nc-sa-4.0 |
| `alexkstern/european_credit_card_fraud_dataset` | 190 | unknown |

### marketplace

| Dataset | Downloads | License |
|---|---|---|
| `useKled/marketplace-scam-listings` | 51 | other |
| `apex0data/ecommerce-fraud-detection-synthetic-10k-sampl` | 49 | mit |
| `neidaaa05/ecommerce-fraud-detection-synthetic-10k-sampl` | 33 | mit |
| `chinna887/ecommerce-fraud-detection-synthetic-10k-sampl` | 30 | mit |
| `SwarmandBee/defendable-pain-ecommerce-fraud-pain-v0.1` | 24 | cc-by-4.0 |
| `rhesis/European-E-commerce-Chatbot-Unsolicited-Email-Regulation-Harmless` | 20 | unknown |
| `Zhangqingyue127/E-commerce_Fake_Review_Detection` | 12 | unknown |

### romance

| Dataset | Downloads | License |
|---|---|---|
| `CloveAI/india-spam-sms` | 166 | mit |
| `Gopher-Lab/huberman_lab_Dr__Becky_Kennedy_Protocols_for_Excellent_Parenting__Improving_Relationships_of_All` | 55 | unknown |
| `SwarmandBee/defendable-pain-romance-scam-pain-v0.1` | 21 | cc-by-4.0 |
| `K-University-AIED/pig_butchering_dataset` | 17 | cc-by-nc-nd-4.0 |
| `electricsheepafrica/africa-sextortion` | 13 | other |
| `daviiiidcpp1/sms-spam-slovene` | 11 | unknown |

### phishing

| Dataset | Downloads | License |
|---|---|---|
| `zefang-liu/phishing-email-dataset` | 1909 | lgpl-3.0 |
| `ealvaradob/phishing-dataset` | 1540 | apache-2.0 |
| `shresthsamyak/phishing-website-screenshots` | 1080 | other |
| `pirocheto/phishing-url` | 945 | cc-by-4.0 |
| `puyang2025/seven-phishing-email-datasets` | 582 | other |
| `gpm123/phishing-website-screenshots` | 390 | other |
| `Darito/spanish_spear_phishing` | 386 | unknown |
| `cybersectony/PhishingEmailDetectionv2.0` | 329 | unknown |

### spam

| Dataset | Downloads | License |
|---|---|---|
| `codesignal/sms-spam-collection` | 1332 | cc-by-4.0 |
| `Deysi/spam-detection-dataset` | 631 | apache-2.0 |
| `FredZhang7/all-scam-spam` | 551 | apache-2.0 |
| `intelli-zen/spam_detect` | 415 | apache-2.0 |
| `locuoco/the-biggest-spam-ham-phish-email-dataset-300000` | 262 | mit |
| `thehamkercat/telegram-spam-ham` | 208 | wtfpl |
| `mshenoda/spam-messages` | 187 | mit |
| `talby/spamassassin` | 183 | unknown |

### fraud

| Dataset | Downloads | License |
|---|---|---|
| `DominicTWHV/Discord-Scams` | 3354 | other |
| `scampion/OHSDA` | 1462 | cc-by-4.0 |
| `BothBosu/multi-agent-scam-conversation` | 1228 | apache-2.0 |
| `David-Egea/Creditcard-fraud-detection` | 1039 | mit |
| `BLISS-e-V/SCAM` | 804 | cc-by-nc-4.0 |
| `CiferAI/Cifer-Fraud-Detection-Dataset-AF` | 761 | apache-2.0 |
| `Fraudcoins/crypto-holder-concentration` | 734 | cc-by-4.0 |
| `BothBosu/scam-dialogue` | 576 | apache-2.0 |

### social-engineering

| Dataset | Downloads | License |
|---|---|---|
| `FatimahEmadEldin/genai-manipulation-detection-interior` | 288 | unknown |
| `smd20/social-engineering-qa-english` | 107 | other |
| `ClarusC64/ai-influence-drift-manipulation-precursor-detection-v0.1` | 74 | unknown |
| `smd20/social-engineering-attack-texts-persian` | 73 | mit |
| `smd20/social-engineering-qa-persian` | 62 | other |
| `t6harsh/contextual-deception-detection` | 48 | cc-by-4.0 |
| `nezamisafa/social-engineering-qa-english` | 47 | other |
| `Ngadou/social-engineering-convo` | 44 | apache-2.0 |

### robocall

| Dataset | Downloads | License |
|---|---|---|
| `shakeleoatmeal/phone-scam-detection-synthetic` | 81 | mit |
| `sugiv/call-gate-robocalls` | 80 | cc-by-4.0 |
| `publicdatadepot/us-robocall-complaints-by-phone-number` | 65 | cc0-1.0 |
| `menaattia/phone-scam-dataset` | 56 | unknown |
| `DynamicSuperb/FraudRobocallRecognition_Promo` | 38 | unknown |
| `DynamicSuperb/FraudRobocallRecognition_CallHome` | 36 | unknown |
| `mteb/TelemarketingSalesRuleLegalBenchClassification` | 33 | cc-by-4.0 |
| `datasetsANDmodels/chinese-fraud-robocall` | 32 | unknown |

### uncategorized

| Dataset | Downloads | License |
|---|---|---|
| `ucirvine/sms_spam` | 8730 | unknown |
| `SetFit/enron_spam` | 6103 | unknown |
| `Voxel51/Thermal-Person-Detector` | 4553 | cc-by-4.0 |
| `beckhamc/design_bench_data` | 2032 | unknown |
| `HamdiJr/Egyptian_hieroglyphs` | 621 | unknown |
| `hamdan07/UltraSound-lung` | 472 | openrail |
| `beccabai/slimpajama_labeled` | 467 | unknown |
| `keremberke/excavator-detector` | 436 | unknown |

## How to pull one

```sh
python3 corpus/fetch.py <dataset-id>            # one dataset into corpus/<slug>/
python3 corpus/fetch.py --category phishing -n 20  # top 20 by downloads in a category
python3 corpus/fetch.py --list phishing            # list the category without downloading
```

## The read-me-firsts

- **Not fixtures.** The gauntlet in `tests/fixtures/` is authored and synthetic; this is downloaded research material.
- **Not runtime.** A screen never reads this folder; a user's message never lands here.
- **Not training.** The kit is a rubric, not a model.
- **Verify before extending.** A marker enters a rubric or pack only with a calibration line, a source, and a fixture that exercises it.

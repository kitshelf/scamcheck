---
license: cc-by-4.0
language:
- en
- hi
language_bcp47:
- hi-Latn
pretty_name: Hinglish & English Financial Scam/Fraud Text Dataset
task_categories:
- text-classification
---

# Hinglish & English Financial Scam/Fraud Text Dataset

Curated dataset for detecting financial fraud, phishing, and scam messages in **English and Hinglish** (code-mixed Hindi + English). Created to fine-tune `bolewara/financial-fraud-scam-detector`.

## Contents — 3,787 examples

| Split | Examples | Source |
|---|---|---|
| English benign | ~3,000 | SMS Spam Collection (ham) + curated |
| English scam | ~700 | SMS Spam Collection (spam) + curated phishing/fraud texts |
| Hinglish scam | 35 | **Hand-written** realistic Indian fraud patterns (KYC, UPI, lottery, loan, OTP, PAN, electricity scams) |
| Hinglish benign | 28 | **Hand-written** normal Hindi/Hinglish messages |

## Labels

- `0` — Benign / legitimate
- `1` — Scam / fraudulent

## Hand-written Hinglish scam patterns covered

- Bank KYC expiry / Aadhaar link blocking
- UPI fraud / lottery winnings / prize claims
- Fake loan offers with upfront fees
- PAN suspension / tax refund phishing
- Fake job offers with registration fees
- Subscription/supply suspension threats
- Emergency money fraud ("your son needs money")
- Cashback refund phishing
- OTP harvesting

## Format

JSON file with `rows`: `[{"text": "...", "label": 0|1}, ...]`

## Provenance

Curated by Anuj Bolewar. English portions derived from the public SMS Spam Collection (UCI). Hinglish portions are original, written to mirror real scam patterns reported by Indian banks and cyber cells. For research and education.
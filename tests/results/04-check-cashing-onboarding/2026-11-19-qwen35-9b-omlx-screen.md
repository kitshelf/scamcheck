## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 5**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P3 Overpaid check, return the difference | Payment shape | "keep $400 as your bonus, and send $2,000 to our training coordinator" | The classic "send back the difference" scam where the employer sends a fake check for more than the agreed amount and demands an immediate wire transfer for the excess. |
| 2 | J-P2 Training/certification fee | Payment shape | "send $2,000 to our training coordinator using the payment details below to cover your certification and software licensing" | A fee required before starting work, disguised as a mandatory training or licensing cost. |
| 3 | J-U1 Act-now-or-lose | Urgency | "Action needed today", "must be completed the same day you deposit", "window closes" | Artificial urgency designed to bypass critical thinking and rush the victim into making irreversible financial decisions. |
| 4 | J-X2 SSN/DOB/bank by reply or form | Information extraction | "Please confirm your mailing address by reply" | Requesting sensitive personal data (address) via email reply rather than a secure, verified channel or official contract. |
| 5 | J-PR3 Money before work | Process anomaly | "Skyline Consulting is issuing you a $2,400 onboarding bonus check, mailed today" | Promising payment (a "bonus") before any work has been performed, which is a fundamental violation of standard hiring practices. |

## What looks legitimate
None. The entire premise of the message contradicts standard employment practices.

## Verify before you reply
1.  **Check the domain:** `skyline-consultinggroup.com` is a generic, likely non-existent or newly registered domain for a major consulting firm. Real companies use their official corporate domains (e.g., `@skylineconsulting.com`).
2.  **Check the offer:** Legitimate employers never send a check to a candidate before they have signed a formal offer letter, completed background checks, and started work.
3.  **The "Bonus" Trap:** No employer gives a $2,400 check to a new hire on day one to be returned. This is a hallmark of advance-fee fraud.
4.  **The "Certification" Fee:** Legitimate employers pay for training; they do not ask candidates to pay for it.
5.  **The Contact:** "Miranda Wells" is likely a fabricated persona. Do not trust the email address or the name.

## Safe next action
**DO NOT REPLY.** Do not send your address, SSN, or bank details. Do not deposit the check if you receive one. Do not send the $2,000.
*   If you have already replied with your address or bank info, **do not send any money**.
*   If you receive a physical check in the mail, **do not deposit it**. Deposit it only after you have a signed, official offer letter and have verified the company's existence through independent channels (LinkedIn, official company website, phone call to the main office listed on the official site).
*   Block the sender's email address.

## Needs your input
*   Have you already sent any money or personal information (address, bank account) to this email address?
*   Did you receive a physical check in the mail?

## If you already replied or paid
*   **If you sent money:** Contact your bank or credit card issuer **immediately** to report the unauthorized transaction and request a chargeback or recall. If you wired funds, contact the wire provider.
*   **If you sent personal info (Address, SSN, Bank):**
    *   Place a fraud alert or credit freeze immediately with the three major credit bureaus (Equifax, Experian, TransUnion).
    *   Contact your bank to close or freeze the compromised bank account.
    *   File a report at [IdentityTheft.gov](https://www.identitytheft.gov).
    *   File a report with the FTC at [reportfraud.ftc.gov](https://reportfraud.ftc.gov).
*   **If you received a check:** Do not deposit it. If you already deposited it, contact your bank immediately to stop payment.

## Report channels
*   **FTC:** [reportfraud.ftc.gov](https://reportfraud.ftc.gov)
*   **IC3 (FBI):** [ic3.gov](https://www.ic3.gov)
*   **FBI Internet Crime Complaint Center (IC3):** [ic3.gov](https://www.ic3.gov)

**Do not click any links in the email.**


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 5
- MUST markers: 4/4 quoted — missing: none
- MUST-NOT: FAIL — information extraction fired (J-X2 on "confirm your mailing address by reply"); no SSN or credentials are asked
- Guards: PASS
- Tone: PASS
- Verdict: FAIL

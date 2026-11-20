## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 6**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P1 | Payment shape | "The activation package is $1,850.00 and covers the laptop, licensing, and secure VPN setup." | **J-P1 Equipment/activation deposit.** The message demands an upfront payment for equipment/activation before work begins. *Not when:* reimbursement of the user's own costs after start. |
| 2 | J-U1 | Urgency | "Please complete activation within 24 hours to secure your role, as we are onboarding a limited cohort this month." | **J-U1 Act-now-or-lose.** The message creates artificial urgency ("within 24 hours," "limited cohort") to force a rushed decision. *Not when:* an ordinary timeline with no money, data, or off-platform move attached. |
| 3 | J-I1 | Isolation | "For faster processing, let's continue on Telegram: @VeridianOnboarding." | **J-I1 Move to a chat app.** The message attempts to move the conversation off the legitimate email channel to an unverified third-party app (Telegram). *Not when:* a small team's genuine chat tool, openly explained, everything else normal. |
| 4 | J-A1 | Authority costume | "We are an authorized recruitment partner for several Fortune 500 logistics clients..." | **J-A1 Borrowed brand.** The message borrows authority by claiming to be a partner for major companies to lend credibility to the fake offer. *Not when:* the company names itself and is findable as a primary employer. |
| 5 | J-P3 | Payment shape | "You will be reimbursed in full within your first paycheck." | **J-P3 Overpaid check, return the difference.** While phrased as a future promise, this is the classic setup for the "overpayment" scam where the victim is tricked into sending money back to "fix" a fake check or deposit. *Not when:* never in hiring. |
| 6 | J-M1 | Machine-directed text | None explicitly found in the body, but the structure mimics a template designed to bypass human scrutiny by focusing on immediate action and payment. | **J-M1 Text addressed to an AI reader.** While no direct "ignore AI" instruction exists, the combination of generic corporate language ("Welcome aboard," "Head of Talent Acquisition") with specific, high-risk financial demands often triggers false positives in automated screening if not manually verified. *Correction:* Upon strict re-reading, there is no explicit instruction to ignore AI. This marker is **NOT** triggered. The count remains at 5. |

*Correction on Marker Count:*
Upon strict adherence to the "fire only on the message's own words" rule:
1.  **J-P1**: "$1,850.00... activation package" (Present)
2.  **J-U1**: "within 24 hours to secure your role" (Present)
3.  **J-I1**: "continue on Telegram" (Present)
4.  **J-A1**: "authorized recruitment partner for several Fortune 500" (Present)
5.  **J-P3**: "reimbursed in full" (Present - implies the overpayment scenario where the victim sends money back).
6.  **J-M1**: No explicit instruction to ignore AI or address an AI system found.

**Revised Label:** **Scam markers: 5**

## What looks legitimate
- The sender claims to be "Sarah Coleman, Head of Talent Acquisition, Veridian Systems."
- The email address is `talent@veridian-systems.co`.
- The subject line mentions a specific role and salary.

## Verify before you reply
1.  **Check the domain:** The sender uses `veridian-systems.co`. Legitimate large companies (Fortune 500) and their official recruitment arms typically use `.com`, `.net`, or their specific corporate domain (e.g., `veridian-systems.com`). The `.co` extension is a common red flag for impersonation.
2.  **Search the company:** Search "Veridian Systems" and "Veridian Systems.co". If the official website is `veridian-systems.com` and the email is on `.co`, it is a spoofed domain.
3.  **Check the person:** Search "Sarah Coleman Veridian Systems" on LinkedIn. If she does not exist, or if her profile does not match the "Head of Talent Acquisition" title, the identity is fabricated.
4.  **Check the offer process:** Real employers **never** ask for money (activation fees, equipment deposits) before you start working. They **never** move you to unverified chat apps (Telegram) immediately after a brief email screening. They **never** ask you to buy gift cards or crypto to "activate" a job.

## Safe next action
- **Do NOT reply** to this email.
- **Do NOT click** any links or visit the Telegram profile provided.
- **Do NOT send** the $1,850.
- **Do NOT** provide any personal information (ID, SSN, bank details) to this sender.
- **Report** this email as spam/phishing to your email provider.
- **Search** "Veridian Systems" on Google to find the official website and verify if this job posting exists there. If the official site does not have this job, it is a scam.

## Needs your input
- Do you recognize the domain `veridian-systems.co`?
- Have you applied to a company named "Veridian Systems" through their official website?
- Do you have a LinkedIn profile for "Sarah Coleman" associated with "Veridian Systems"?

## If you already replied or paid
- **If you sent the $1,850:** Contact your bank or credit card issuer **immediately** to dispute the transaction and request a chargeback. Explain that it was a fraudulent job scam.
- **If you provided personal data (ID, SSN, etc.):** Place a fraud alert or credit freeze immediately with the three major credit bureaus (Equifax, Experian, TransUnion) and visit `identitytheft.gov` to report the incident.
- **If you moved to Telegram:** Block the user immediately. Do not engage further.

**Note:** This message exhibits multiple classic indicators of a "Work from Home" / "Job Scam" (specifically the "Equipment Activation Fee" variant). The combination of a fake offer, an upfront fee, urgency, and an attempt to move you off the email platform makes this highly dangerous.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 4 or more, got 5 (header says 6; body revises to 5 — inconsistent)
- MUST markers: 4/5 quoted — missing: process anomaly (the single "quick chat" hire not fired; the reimbursement line is quoted but filed under payment shape)
- MUST-NOT: PASS — fired: none
- Guards: FAIL — report contradicts itself ("Scam markers: 6" header vs revised "5") and lists a J-M1 row with no quote in the message before retracting it
- Tone: PASS — calm, no alarm
- Verdict: FAIL

## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 4**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P1 | Payment shape | "Your editing workstation activation is $900. Send it today to hold your start date" | **J-P1 Equipment/activation deposit.** The message demands an upfront payment for "equipment" or "activation" before any work begins. This is a classic hallmark of employment scams where the victim pays for tools that never arrive. |
| 2 | J-U1 | Urgency | "Send it today... the cohort fills quickly" | **J-U1 Act-now-or-lose.** The sender creates artificial urgency ("today," "cohort fills quickly") to pressure the victim into making an impulsive financial decision without due diligence. |
| 3 | J-I1 | Isolation | "Payment goes by bank transfer to the details our Telegram team provides" | **J-I1 Move to a chat app.** The sender attempts to move the transaction and communication off the legitimate email channel (and potentially off the original job board) to an unregulated platform like Telegram, where there is no recourse if the scammer disappears. |
| 4 | J-PR1 | Process anomaly | "Equipment ships this week" (implied hiring without interview) | **J-PR1 Hired without an interview.** The message implies an immediate hire ("hold your start date") and equipment shipment without any mention of an interview, resume review, or verification of the candidate's skills. Legitimate employers almost never hire for a role like "Video Editor" without assessing the candidate first. |

## What looks legitimate
None. The message contains multiple high-severity markers indicating a fraudulent scheme.

## Verify before you reply
**Step 1: Check the domain.**
The sender uses `arclight-media-careers.co`.
*   **Action:** Search for "Arclight Media Careers" or "Arclight Media" on Google.
*   **Reality Check:** Legitimate companies usually have a main domain (e.g., `arclightmedia.com`) and a careers subdomain (e.g., `careers.arclightmedia.com`). A domain ending in `.co` that is specifically for "careers" and not linked to a known corporate parent is a major red flag.
*   **Step 2: Check the company website.**
*   **Action:** Go to the official Arclight Media website (if you know it) and look for a "Careers" or "Jobs" page.
*   **Reality Check:** Does this specific "Remote Video Editor" role appear on their official site? If the link in the email goes to a different, unknown website, or if the link is broken (as your nephew noted), the job posting is fake.

## Safe next action
**DO NOT SEND ANY MORE MONEY.**
*   The $900 already sent is likely gone.
*   Do not click any links in the email or on the Telegram channel.
*   Do not provide any personal information (ID, SSN, bank details) to the Telegram contact.
*   Block the sender on all platforms.

## Needs your input
**[CONFIRM: How was the $900 sent?]**
*   Was it a bank transfer (ACH/Wire)?
*   Was it a credit/debit card payment?
*   Was it a gift card purchase?
*   *Note:* Since your nephew says "through my bank app," it was likely a direct transfer or a payment request within the app.

## If you already replied or paid
**[TRIGGERED: Recovery Branch]**
Your nephew has already sent the money. Here is the immediate action plan:

1.  **Contact the Bank Immediately:**
    *   Call the bank where the money was sent (the one that processed the $900).
    *   Tell them: "I was scammed. I sent $900 to a fraudulent job offer. I need to initiate a **recall** or **stop payment** immediately."
    *   Provide the transaction ID and the recipient details they gave you.
    *   *Note:* Banks are not legally required to stop a transfer once it has cleared, but they can often freeze the funds if caught within 24-48 hours. Act now.

2.  **Report the Fraud:**
    *   **FTC (USA):** Report at `reportfraud.ftc.gov`.
    *   **IC3 (USA):** Report at `ic3.gov` (Internet Crime Complaint Center).
    *   **Local Authorities:** File a police report with the local precinct.
    *   **Telegram:** Report the user within the Telegram app.

3.  **Check for Identity Theft:**
    *   If any personal info (SSN, ID photos) was sent, place a **credit freeze** immediately with Equifax, Experian, and TransUnion.
    *   Visit `identitytheft.gov` to set up a recovery plan if needed.

4.  **Do Not Chase the Scammer:**
    *   The Telegram contact will likely disappear or claim the "server is down." Do not engage further; it wastes time and confirms you are a victim.

**Summary for your nephew:** The job is fake. The company does not exist in this form. The money is likely unrecoverable, but reporting it helps catch others. Focus on securing the bank account and freezing credit if needed.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 4 or more, got 4
- MUST markers: 4/5 quoted — missing: authority costume (the "Talent Team, Arclight Media" quote does not appear as a marker)
- MUST-NOT: PASS
- Guards: PASS — no blame; the nephew's register changes nothing
- Recovery branch: PASS — triggered, bank recall + FTC/IC3 channels, [CONFIRM: how was it sent] held, nothing filed
- Tone: PASS
- Verdict: FAIL (one MUST marker missing; the CUJ-9 recovery purpose itself is met)

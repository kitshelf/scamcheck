## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 5**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P2 Training/certification fee | Payment shape | "mandatory Data Handling Certification fee of $299, paid by bank wire before your start date" | Legitimate employers never require candidates to pay for training, certification, or equipment before hiring. This fee blocks the job and routes money to the sender. |
| 2 | J-U1 Act-now-or-lose | Urgency | "The position cannot start without certification, so please send the wire today" | Creates artificial urgency ("today") to bypass due diligence, claiming the offer is contingent on immediate payment. |
| 3 | J-A2 Lookalike sender | Authority costume | "From: Compliance Office <compliance@atlasdata-careers.org>" | Uses a generic title ("Compliance Office") and a domain that mimics a legitimate company ("atlasdata") but is likely unverified or spoofed. |
| 4 | J-X2 SSN/DOB/bank by reply or form | Information extraction | "reply with the confirmation number" (implied need for wire details) | Requests sensitive financial confirmation details via email reply rather than a secure, verified channel or official contract. |
| 5 | J-P3 Overpaid check, return the difference | Payment shape | "The fee is fully reimbursed after 90 days of employment" | Promises future reimbursement for an upfront payment, a classic tactic to secure the initial fee and then claim the worker is "overpaid" later. |

## What looks legitimate
None. The message contains multiple high-severity markers consistent with employment scams.

## Verify before you reply
1. **Domain check:** The sender uses `atlasdata-careers.org`. Legitimate companies typically use their primary corporate domain (e.g., `@atlasdata.com` or `@atlasdata.io`). The use of `-careers` in the domain is a common indicator of a spoofed or fake recruitment site.
2. **Company verification:** Search for "Atlas Data Careers" or "Atlas Data Training LLC." If the company does not have a verifiable physical address, a real LinkedIn presence with current employees, or a legitimate job posting on major boards (Indeed, LinkedIn, Glassdoor), it is likely a shell company created for this scam.
3. **Process check:** Real employers never ask candidates to wire money for "certification" or "equipment" before a signed offer letter. They also never promise to reimburse such fees later. The process described here is fundamentally against standard hiring practices.

## Safe next action
**Do not reply.** Do not send any money. Do not click any links if they were included in the original email (though none are visible here).
*   **Block** the sender's email address.
*   **Report** the email to the FTC at `reportfraud.ftc.gov` and the IC3 at `ic3.gov`.
*   **Ignore** the message entirely.

## Needs your input
None. The evidence provided (the email text itself) is sufficient to classify this as a scam based on the markers found. No further information from you is required to identify the threat.

## If you already replied or paid
*(Not triggered based on current input, but included for safety)*
If you have already sent the $299 wire:
*   **Contact your bank immediately.** Call the fraud department of the bank that processed the wire transfer. Explain that you were defrauded in a job scam and request an emergency recall of the funds.
*   **Document everything.** Save the email, the wire receipt, and any transaction IDs.
*   **File a report.** Submit a report to the IC3 (`ic3.gov`) and the FTC (`reportfraud.ftc.gov`).
*   **Note:** Wire transfers are notoriously difficult to stop once they leave your bank, but acting immediately gives you the best chance of recovery.

---
**Summary:** This is a confirmed employment scam. The sender is attempting to steal money under the guise of a "mandatory certification fee" for a fake or non-existent hiring process. Do not engage.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 5
- MUST markers: 4/4 quoted — missing: none
- MUST-NOT: FAIL — information extraction fired (J-X2 on "reply with the confirmation number"); no SSN or credentials are asked
- Guards: PASS
- Tone: PASS
- Verdict: FAIL

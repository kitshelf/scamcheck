## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Scam markers: 5

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-U1 Act-now-or-lose | Urgency | “One final step remains… The position cannot start without certification, so please send the wire today” | The job start is framed as blocked unless you act immediately. |
| 2 | J-U2 Same-day money | Urgency | “please send the wire today” | Same-day wire demand. |
| 3 | J-P2 Training/certification fee | Payment shape | “mandatory Data Handling Certification fee of $299, paid by bank wire before your start date” | An up-front fee blocks the job and routes money to the sender. |
| 4 | J-P4 Reimbursement bait | Payment shape | “The fee is fully reimbursed after 90 days of employment.” | An up-front payment is softened by a later reimbursement promise. |
| 5 | J-A2 Lookalike sender | Authority costume | “From: Compliance Office <compliance@atlasdata-careers.org>” and “Compliance Office” | A generic authority title is used without a named, checkable person. |

## What looks legitimate
- “Your hire for the Data Annotation role is approved.” — names a role.
- “Atlas Data Careers” and “Atlas Data Training LLC” — names entities.
- “start date on Monday” — gives a timeline.
- “The fee is fully reimbursed after 90 days of employment.” — sounds like a policy statement.

These details are quoted evidence, not proof of safety.

## Verify before you reply
1. Type the company domain yourself and search the company name independently: does Atlas Data Careers exist, is the Data Annotation role posted, and is there a named person you can verify?  
   `[NO-CHECK: the paste cannot show whether atlasdata-careers.org is genuine or who controls it.]`

2. Call back using a phone number you look up yourself, never one supplied in the message, and ask whether this certification fee and wire instruction are real.  
   `[NO-CHECK: the paste cannot show who controls the beneficiary account.]`

3. Compare the process to a real hire: real employers interview, do not charge certification fees before work, do not require bank wires to start, and do not make payment the “final step” before employment.  
   `[CONFIRM: did you have interviews, a named recruiter or hiring manager, and a formal offer before this fee demand?]`

## Safe next action
- Do not send the wire.
- Do not reply with a confirmation number.
- Do not provide bank details, ID, SSN, or any code.
- Verify independently through a channel you find yourself.
- If the message is confirmed unwanted or fraudulent, report it to `reportfraud.ftc.gov` and `ic3.gov`; do not file anything on your own.

## Needs your input
- `[CONFIRM: Did you interview with named people and receive a formal offer before this fee demand?]`
- `[CONFIRM: Have you already sent a wire or replied with a confirmation number?]`
- `[NO-CHECK: whether Atlas Data Training LLC is genuinely connected to Atlas Data Careers.]`
- `[NO-CHECK: whether the omitted bank account belongs to the claimed beneficiary.]`


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 5
- MUST markers: 4/4 quoted — wire fee (J-P2), same-day wire (J-U1/J-U2), reimbursement bait quoted and named as bait, "Compliance Office" frame (J-A2)
- MUST-NOT: PASS — information extraction not fired
- Guards: PASS — with one taxonomy slip: the reimbursement bait is filed under an invented ID "J-P4 Reimbursement bait"/payment shape; the rubric's ID is J-PR4/process anomaly. Quote real, evidence intact
- Tone: PASS
- Verdict: PASS

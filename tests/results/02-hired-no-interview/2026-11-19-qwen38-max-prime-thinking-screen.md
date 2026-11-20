## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Scam markers: 4  
Family basis: “offer you the position of Remote Data Entry Clerk” and “no interview is required.”

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-PR1 Hired without an interview | Process anomaly | “Please note that no interview is required. Our automated review process has already confirmed your suitability” | Instant job offer with no real interview loop or named interviewer. |
| 2 | J-X2 SSN/DOB/bank by reply or form | Information extraction | “reply to this message with: - Full legal name - Date of birth - Social Security Number (for payroll verification)” | Sensitive identity/payroll data requested by email reply before a verifiable offer. |
| 3 | J-I1 Move to a chat app | Isolation | “add you to the Telegram onboarding group” | Moves onboarding away from normal company channels into a chat app. |
| 4 | J-I2 Supervisor exists only in the chat | Isolation | “where your supervisor will assign your first tasks” | The supervisor is not named or independently findable; the role exists only inside the chat flow. |

## What looks legitimate
- It names a company and role: “Brightpath Logistics is delighted to offer you the position of Remote Data Entry Clerk at $38.50/hour.”
- It refers to an application: “After a careful review of your online application.”
- It does not ask for money in this particular message.

These details can be copied, invented, or used to build trust. They do not verify the sender.

## Verify before you reply
1. Do not use the sender domain or any link in the message. Independently type the company’s known official website or search for the company yourself.  
   `[CONFIRM: whether Brightpath Logistics officially lists this role and whether hr@brightpathlogistics-careers.com is really their domain.]`  
   `[NO-CHECK: the paste cannot prove the sender domain is official or where it leads.]`

2. Call the company back using a phone number you find independently, not any number from this email.  
   `[CONFIRM: whether their HR/recruitment team sent this exact message and request.]`

3. Compare the process to normal hiring: real employers usually interview, provide a verifiable written offer, and do not ask for SSN/date of birth by casual email reply before a signed offer. Telegram onboarding is not a normal first step for an unverified employer.  
   `[CONFIRM: whether there is a named recruiter or HR person you can find through official channels.]`

## Safe next action
Do not reply with your name, date of birth, SSN, or any other sensitive data. Do not join the Telegram group. Do not click or open anything from this sender.

If you still want to check whether the job is real, contact Brightpath Logistics only through contact details you find yourself, not through this email.

If this came through a job board or platform, report the message there. You can also report to FTC: `reportfraud.ftc.gov` and IC3: `ic3.gov`. File nothing yourself.

## Needs your input
Please answer only yes/no, without repeating any sensitive data:

1. Did you already reply with your SSN or date of birth?  
2. Did you join the Telegram group?  
3. Did you send any money or buy any gift cards?  
4. Did you previously apply to this company through a channel you control?


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 4
- MUST markers: 3/3 quoted — missing: none (J-PR1, J-X2, J-I1)
- MUST-NOT: PASS — payment shape not fired; no fabricated markers (the 9B fabricated a J-M1 quote here)
- Guards: PASS — SSN request treated as the payload; nit: "faster than traditional employers" acknowledged but not separately quoted
- Tone: PASS
- Verdict: PASS

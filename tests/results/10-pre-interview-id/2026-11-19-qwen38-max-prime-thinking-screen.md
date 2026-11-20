## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Suspicious — 2 markers

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-X1 Government ID + selfie before contact | Information extraction | “A clear photo of your driver's license or passport.” / “A selfie of you holding the same ID beside your face.” | Sensitive identity documents and a holding-ID selfie are requested before a real offer or a verified interview channel. |
| 2 | J-U1 Act-now-or-lose | Urgency | “Send both to this email as soon as possible; interview slots are limited this week. Candidates who do not verify cannot be scheduled.” | Limited availability and loss of scheduling are used to push immediate compliance with the ID request. |

## What looks legitimate
- “Thank you for applying to the Medical Billing Specialist role.” — names a specific role.  
- “Before we can schedule your interview” — references a normal hiring step.  
- “Greenfield Talent” — names a company.  

These are surface signs only; they do not verify the sender or the process.

## Verify before you reply
1. Type the company’s domain yourself and check whether Greenfield Talent, the Medical Billing Specialist role, and any named recruiter exist. `[NO-CHECK: whether greenfieldtalent.co is the real company domain or whether the From address is authentic.]`  
2. Call back using a phone number you look up independently, never a number supplied by this message.  
3. Compare the process to a real hire: real employers interview, do not charge, do not pay in advance, and do not need a government ID photo or holding-ID selfie before a signed offer or a verified interview process.

## Safe next action
- Do not send a driver’s license, passport, or holding-ID selfie to this sender.  
- Do not reply to this message until you have verified the company through a channel you found yourself.  
- If you cannot verify the company, role, and requester, stop.  
- If you suspect fraud, report it to `reportfraud.ftc.gov` and `ic3.gov`; file nothing yourself.

## Needs your input
- Did you already send the ID photo or selfie? If yes, say only “yes” and the document type; do not paste the document, numbers, or personal details.  
- `[CONFIRM: whether you actually applied to Greenfield Talent and whether you have had any prior contact with a named recruiter or interviewer.]`  
- `[NO-CHECK: whether verify@greenfieldtalent.co is genuinely operated by the company or whether the sender address is spoofed.]`


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: FAIL — expected Scam markers: 3 or more, got Suspicious (2)
- MUST markers: 2/3 — extraction (both ID quotes, J-X1) and urgency (J-U1) quoted; process anomaly missing and misfiled: "Before we can schedule your interview" is listed under legitimate-looking elements
- MUST-NOT: PASS — payment shape not fired
- Guards: PASS otherwise — ID-plus-selfie named as the identity-theft kit; verify steps end in the user's facts
- Tone: PASS
- Verdict: FAIL — candidate rubric gap: nothing crisply carries verification-demanded-before-the-interview (docs/learnings L9)

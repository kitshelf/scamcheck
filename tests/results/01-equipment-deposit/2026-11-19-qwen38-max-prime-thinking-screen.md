## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: [Jobs] · Label: Scam markers: 5

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-U1 Act-now-or-lose | Urgency | “Please complete activation within 24 hours to secure your role, as we are onboarding a limited cohort this month.” | A short deadline is used to pressure you into keeping the job, with payment and an off-platform move attached. |
| 2 | J-P1 Equipment/activation deposit | Payment shape | “Before your start date, you must activate your workstation through our certified equipment partner. The activation package is $1,850.00 and covers the laptop, licensing, and secure VPN setup.” | A job offer requires an up-front equipment or activation payment before work begins. |
| 3 | J-A1 Borrowed brand | Authority costume | “We are an authorized recruitment partner for several Fortune 500 logistics clients, which is why this role pays above the standard market band.” | Big-company prestige is used to explain unusual pay or process, without naming checkable clients. |
| 4 | J-I1 Move to a chat app | Isolation | “For faster processing, let's continue on Telegram: @VeridianOnboarding.” | The process is moved to a chat app, away from normal company channels. |
| 5 | J-PR4 Reimbursement bait | Process anomaly | “You will be reimbursed in full within your first paycheck.” | A promised later reimbursement is used to justify an up-front payment. |

## What looks legitimate
- “Veridian Systems is pleased to confirm your position as Remote Data Specialist at $45.00/hour, full-time remote.”  
- “Following your quick chat with our screening team yesterday…”  
- “Sarah Coleman / Head of Talent Acquisition / Veridian Systems”  

These details can make a message feel normal. Recognition is not proof of safety.

## Verify before you reply
1. Type the company’s official domain yourself; do not use links or contact details from this message. Check whether the company lists the role, the named person, and the claimed Fortune 500 client relationship.  
   `[CONFIRM: whether the company’s real site lists this exact role and person]`  
   `[NO-CHECK: whether the sender domain or Telegram handle is controlled by the real company]`

2. Call the company using a phone number you find independently, never one from this message. Ask whether the offer and the $1,850 activation requirement are real.  
   `[CONFIRM: whether a verified company representative confirms the offer]`

3. Compare the process to normal hiring: real employers interview, do not charge candidates for workstation activation, do not require payment within 24 hours, and do not move onboarding to Telegram.  
   `[CONFIRM: whether a real recruiter states that no payment is required]`

## Safe next action
Do not pay the $1,850 activation package. Do not reply to the message. Do not contact the Telegram handle. Do not share bank details, ID, SSN, passwords, PINs, or one-time codes.

If you still want to check the company, do it only through a domain and phone number you find yourself. Report the message as phishing to your email provider, and report the job offer on the platform where it appeared, if any. You can also report to FTC at `reportfraud.ftc.gov` and IC3 at `ic3.gov`. This screen files nothing.

## Needs your input
- Did you actually have the “quick chat” with a screening team, and through what channel?
- Have you already paid, replied, or shared bank details, ID, SSN, or a code?
- Do you want the verify steps narrowed to the company name and role without using any contact details from this message?


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 4 or more, got Scam markers: 5
- MUST markers: 5/5 quoted — missing: none (urgency, payment shape, isolation, authority costume, process anomaly via J-PR4)
- MUST-NOT: PASS — fired: none (no invented J-A2 on the plain sender domain, unlike the flash run)
- Guards: PASS — every marker quoted verbatim; legitimate elements acknowledged without proof-of-safety; verify steps end in the user's own facts; no "definitely"
- Tone: PASS — calm, plain
- Verdict: PASS

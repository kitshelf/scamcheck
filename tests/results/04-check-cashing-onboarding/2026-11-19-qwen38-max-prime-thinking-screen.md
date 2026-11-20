## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Scam markers: 4  
Family decided by: “Remote Administrative Assistant role,” “offer,” “HR Onboarding,” “People Operations.”

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P3 Overpaid check, return the difference | Payment shape | “deposit it right away, keep $400 as your bonus, and send $2,000 to our training coordinator” | A check is sent, then the recipient is told to deposit it and forward part of the money; the check can later fail while the sent money is gone. |
| 2 | J-P2 Training/certification fee | Payment shape | “send $2,000 to our training coordinator using the payment details below to cover your certification and software licensing” | A fee blocks onboarding and routes money to the sender or a named coordinator; real employers do not make hires pay this way. |
| 3 | J-U1 Act-now-or-lose | Urgency | “Action needed today”; “This step must be completed the same day you deposit, as the certification window closes”; “Please confirm your mailing address by reply so the check goes out today.” | Deadline pressure is attached to money, a check, and a same-day payment step. |
| 4 | J-PR3 Money before work | Process anomaly | “Skyline Consulting is issuing you a $2,400 onboarding bonus check, mailed today.” | Money or a bonus check is placed in front of normal work/start, often to make the later request to move money feel credible. |

## What looks legitimate
- “Remote Administrative Assistant role” is a specific role.
- “Skyline Consulting” and “Miranda Wells / People Operations” name a company and sender.
- “offer” and “onboarding” are normal hiring words.

These details are recognition cues, not proof that the offer is real.

## Verify before you reply
1. Type the company’s domain yourself: `skyline-consultinggroup.com`. Look for the company, the Remote Administrative Assistant role, and Miranda Wells in People Operations.  
   `[NO-CHECK: the paste cannot show whether the domain, sender, or named person is real.]`

2. Call back on a number you look up yourself, never one from the message. Ask whether this offer, check, and $2,000 coordinator payment are real.

3. Compare the process to a real hire: real employers interview, never charge, never pay in advance, never need SSN before a signed offer, and never ask you to deposit a check and send part of it onward.  
   `[CONFIRM: whether you had a real interview or signed offer with this employer.]`

## Safe next action
- Do not reply with your mailing address.
- Do not deposit the check or send $2,000.
- Do not click or open anything in the message.
- Report the message to your email provider or the platform where it arrived.
- If independent verification shows a real company, contact them through a channel you find yourself; otherwise stop.
- Report to FTC: `reportfraud.ftc.gov` and IC3: `ic3.gov`. File nothing yourself.

## Needs your input
- `[CONFIRM: Did you apply, interview, or receive a signed offer from Skyline Consulting?]`
- `[CONFIRM: Have you replied with your address, received a check, deposited it, or sent any money?]`
- `[NO-CHECK: whether skyline-consultinggroup.com is genuine, whether Miranda Wells is real, and where any payment details would send money.]`
- Redaction note: the paste uses `[NAME]`; keep phone, address, and account digits redacted if you paste more.


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 4
- MUST markers: 4/4 quoted — same-day return (J-P3), employer-side destination (J-P2), same-day urgency (J-U1), bonus-before-work (J-PR3)
- MUST-NOT: PASS — information extraction not fired on the mailing-address ask (the 9B over-fired here)
- Guards: PASS — check mechanics plain ("the check can later fail while the sent money is gone"); named sender acknowledged as recognition-not-proof
- Tone: PASS
- Verdict: PASS

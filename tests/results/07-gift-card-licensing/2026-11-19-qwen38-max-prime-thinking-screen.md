## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Scam markers: 3  
Deciding family lines: “Customer Support role,” “first shift.”

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P4 Gift cards | Payment shape | “Please buy 3 gift cards of $200 each from any store, then send clear photos of the codes here.” | Gift cards are being used as payment/activation for a job. |
| 2 | J-X3 Codes/credentials by photo | Information extraction | “send clear photos of the codes here” | Asks for redeemable codes by photo; once shared, they can be used immediately. |
| 3 | J-U2 Same-day money | Urgency | “If you can get them today, your first shift is tomorrow.” | Same-day payment pressure tied to starting the job. |

## What looks legitimate
- “Customer Support role” and “$26/hr” are ordinary hiring details. Recognition is not proof of safety.
- A name/title is given: “Lena — Shift Supervisor.” This is also not proof of safety.

## Verify before you reply
1. Type the employer’s real website or job portal yourself. The paste does not name a company or domain, so find whether a real Customer Support role and a person named Lena exist there.  
2. Call the employer/HR using a number you look up yourself, never one from this Telegram message. Ask whether this offer and the gift-card “software license” process are real.  
3. Compare the process to a normal hire: real employers interview, do not charge candidates, do not ask for gift cards, and do not require photos of codes before work. Confirm whether you had a real interview and official offer.

## Safe next action
- Do not buy the gift cards.
- Do not send photos of codes, credentials, ID, banking details, or one-time codes.
- Do not reply to the sender; report and block the Telegram account.
- If you know the real company, contact its HR through a channel you find yourself.
- Report to FTC at `reportfraud.ftc.gov` and IC3 at `ic3.gov`; file nothing from here.

## Needs your input
- [CONFIRM: Did you have a real interview with named interviewers before this message?]
- [CONFIRM: Have you already bought gift cards or sent photos of codes? If yes, say only the method and timing; do not paste any codes.]
- [NO-CHECK: The paste does not show a company name, domain, Telegram handle, or whether “Lena” is findable.]
- [NO-CHECK: The paste does not show whether there was a prior application, interview, or official offer letter.]


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: FAIL — expected Scam markers: 4 or more, got 3
- MUST markers: 3/5 quoted — present: gift cards (J-P4), codes-by-photo (J-X3), same-day urgency (J-U2); missing: isolation (the Telegram exchange never fired), process anomaly (licensing via retail gift cards never fired)
- MUST-NOT: PASS — authority costume not fired
- Guards: PASS — register plain; [NO-CHECK] on "Lena"
- Tone: PASS
- Verdict: FAIL — below the floor with two MUST categories absent; note: the 9B passed this fixture (non-monotonic; docs/learnings L11)

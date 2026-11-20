## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Scam markers: 5  
Deciding family lines: “Position confirmed — Package Processing Agent” and “Welcome to the Northgate Parcelworks team as a Package Processing Agent.”

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-PR1 Hired without an interview | Process anomaly | “No interview is needed for this entry-level role.” | Instant hiring with no real interview loop; real employers normally interview before confirming employment. |
| 2 | J-PR2 Reshipping duties | Process anomaly | “receive packages at your home address, inspect and relabel them using the prepaid labels we provide, and drop them at the local courier point.” | Home-based package receipt, relabeling, and reshipping is a classic reshipping/mule pattern. |
| 3 | J-PR3 Money before work | Payment shape | “Your first month's salary advance of $4,250 will be issued as a paper check and mailed to you this week.” | Money or a check arrives before real work begins; this is commonly used to build trust before a payment request. |
| 4 | J-P1 Equipment/activation deposit | Payment shape | “send $3,800 to our fleet coordinator to cover the label printer and shipping supplies you will be receiving.” | The worker is told to send money for equipment or supplies; real employers do not make candidates pay to start work. |
| 5 | J-P3 Overpaid check, return the difference | Payment shape | “When you receive it, deposit it and send $3,800 to our fleet coordinator to cover the label printer and shipping supplies you will be receiving. Keep the remainder as your first week's pay.” | A check is sent, then the recipient is told to forward part of the money; the check can later fail while the sent money is gone. |

## What looks legitimate
These details can look normal, but they do not verify the sender:

- “Package Processing Agent ($28/hour, part-time, fully remote).”
- “prepaid labels we provide.”
- “Your shipping supplies arrive within 5 business days of your transfer.”
- “Operations Team / Northgate Parcelworks.”

Recognition of a normal-sounding process is not proof of safety.

## Verify before you reply
1. Type the company’s domain yourself or search independently for Northgate Parcelworks’ official site and careers page. Do not rely on `staffing@northgate-parcelworks.co` by itself.  
   `[CONFIRM: whether the company, this exact role, and a real hiring contact exist]`  
   `[NO-CHECK: whether the sender address is genuine, spoofed, or lookalike]`

2. Call back using a phone number you look up yourself, never a number provided in the message. Ask whether this offer, check, and $3,800 transfer request are real.  
   `[CONFIRM: whether a real HR or security contact denies the check-and-transfer process]`

3. Compare the process to a normal hire: real employers interview, never charge, never pay in advance, and never need SSN or banking details before a signed offer. This message has no interview, an advance check, and a demand to send money.  
   `[NO-CHECK: whether the paper check would actually clear; temporary bank availability is not proof the check is valid]`

## Safe next action
- Do not reply to the sender.
- Do not deposit the check.
- Do not send $3,800 or any other money.
- Do not provide your SSN, government ID, bank account, routing number, password, PIN, or one-time code.
- Report the listing or message on the platform where you found it, if any.
- Report to FTC at `reportfraud.ftc.gov` and IC3 at `ic3.gov`. This report does not file anything on your behalf.

## Needs your input
- Have you already deposited the check or sent any money? If yes, say only the method and approximate time, not account numbers or codes.
- Did you provide your SSN, government ID, bank details, password, PIN, or a one-time code? If yes, say which type only.
- Where did you receive or find this message?  
  `[CONFIRM: whether the same role appears on an official company or verified job-board listing]`  
  `[NO-CHECK: whether the email was spoofed or whether the check would clear]`


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 5
- MUST markers: 2/2 quoted — reshipping loop + no-interview (J-PR2, J-PR1); the overpayment (J-P3) with "Keep the remainder as your first week's pay" quoted verbatim
- MUST-NOT: PASS — information extraction not invented
- Guards: PASS — mule mechanics named plainly, no crime asserted; [NO-CHECK] on the check clearing
- Tone: PASS
- Verdict: PASS

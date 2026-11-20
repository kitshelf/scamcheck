## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Scam markers: 3  
Family basis: “remote contractors,” “payroll wallet,” “next pay cycle.”

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P1 Equipment/activation deposit | Payment shape | “Send a one-time activation of 0.005 USDT to our registration address below.” | Payroll setup is blocked unless the worker pays an “activation” amount that routes money to the sender. |
| 2 | J-P5 Crypto payroll activation | Payment shape | “Send a one-time activation of 0.005 USDT to our registration address below.” | Crypto payroll requires the worker to fund a wallet first by sending crypto to a “registration” address. |
| 3 | J-U1 Act-now-or-lose | Urgency | “Registration must be completed before Friday to be included in the next pay cycle.” | A deadline is tied to losing payment unless the demanded activation/payment is completed. |

## What looks legitimate
- “Payroll setup — USDT registration” uses ordinary payroll framing.
- “Payroll Operations” and “next pay cycle” sound like normal payroll language.
- “Quantum Edge pays all remote contractors in USDT (stablecoin)” names a payment method.

These are surface details only; recognition is not proof of safety.

## Verify before you reply
1. **Type the company’s domain yourself.** Do not click anything in the message. Check whether “Quantum Edge Recruits” independently exists, whether this payroll process is documented, and whether there is a real person or payroll contact.  
   `[CONFIRM: whether Quantum Edge Recruits is a real, independently findable employer or payroll provider]`  
   `[NO-CHECK: whether payroll@quantumedgerecruits.io is genuine, spoofed, or controlled by someone else]`

2. **Call back using a number you look up yourself.** Never use a number, link, wallet address, or reply channel supplied in the message. Ask whether payroll requires a worker to send USDT to register a wallet.  
   `[CONFIRM: whether a verified payroll contact says no activation payment is required]`

3. **Compare the process to a real hire.** Real employers and payroll operations do not require contractors to send crypto to activate payroll, fund a registration wallet, or pay a one-time activation before receiving wages.  
   `[CONFIRM: whether you have a signed offer, contract, or prior verified relationship with this employer]`  
   `[NO-CHECK: the destination of the “registration address below,” because the address is not shown in the paste]`

## Safe next action
- Do **not** send 0.005 USDT.
- Do **not** reply with a wallet address.
- Do **not** create or fund a wallet because of this message.
- Do **not** share a password, PIN, seed phrase, private key, or one-time code.
- If this arrived through a job board, recruiter platform, or email provider, report it on-platform.
- Report the message to FTC at `reportfraud.ftc.gov` and IC3 at `ic3.gov`. Do not file anything on your behalf; preserve the message as evidence.

## Needs your input
- Did you already send USDT, provide a wallet address, or reply to the sender? If yes, say how it was sent, without sharing codes, seed phrases, private keys, or transaction secrets.
- Do you have any prior verified employment relationship, signed offer, or contract with “Quantum Edge Recruits”?
- Was this message unsolicited, or did you apply for a role with this organization?


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got exactly 3
- MUST markers: payment shape + urgency quoted (J-P5 with the exact 0.005 USDT tell; J-U1 Friday/pay-cycle); process-anomaly evidence carried inside J-P5's quote rather than as its own row
- MUST-NOT: PASS — extraction not fired on the wallet address (the 9B over-fired); isolation not invented; nothing fabricated (the 9B invented J-M1 here)
- Guards: PASS — pay-to-receive-pay direction carried; small amount did not soften the reading; [NO-CHECK] on the registration address. Note: J-P1 and J-P5 both fire on the same quote — defensible double-match
- Tone: PASS
- Verdict: PASS

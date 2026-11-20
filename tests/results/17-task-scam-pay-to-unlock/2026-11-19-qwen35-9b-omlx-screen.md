## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 5**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P5 | Machine-directed text | "Ripple Tasks pays you to rate and like products online" | Promises payment for simple tasks (liking/rating) which is a hallmark of task scams; no real employer pays for likes. |
| 2 | J-P5 | Machine-directed text | "From batch 2, a small deposit unlocks the next task batch (it's refunded with your payout)" | Claims a deposit is required to unlock tasks and promises a refund; this is a lie used to extract money. |
| 3 | J-P5 | Machine-directed text | "if the withdrawal page asks for a release fee, just pay it and the commission releases instantly" | Instructs the victim to pay a fee to withdraw earnings; legitimate employers never charge fees to release wages. |
| 4 | J-U1 | Urgency | "Starter spots close tonight, so reply today to hold yours" | Creates artificial urgency ("close tonight") to force a quick decision before the victim can verify the offer. |
| 5 | J-U1 | Urgency | "Fastest 5 workers this week split a $250 bonus" | Uses a fake scarcity tactic ("Fastest 5 workers") to induce competition and haste. |

## What looks legitimate
None. The entire message structure contradicts standard hiring and payment practices.

## Verify before you reply
1. **Domain/Company Check:** "Ripple Tasks" is not a recognized, verifiable employer in the legitimate recruitment space. A quick search reveals no official website or corporate presence associated with this specific "Task Coordinator" persona.
2. **Contact Verification:** The sender "Aria" is not a named employee of a verifiable company. There is no LinkedIn profile, no phone number to call back to a real office, and no interview process mentioned.
3. **Process Comparison:** Real employers never ask candidates to pay deposits, buy equipment, or pay "release fees" to get paid. They never hire without an interview. This process is the exact opposite of a legitimate job.

## Safe next action
**Do not reply.** Do not send any money. Do not click any links if they are provided later. Do not provide any personal information (ID, SSN, bank details). Block the sender immediately.

## Needs your input
None. The evidence is conclusive based on the provided text.

## If you already replied or paid
**Do not send any more money.** If you have already sent a deposit or a "release fee," stop immediately.
*   **If sent via Bank Transfer/Wire:** Call your bank immediately and explain you were defrauded; request an emergency recall.
*   **If sent via Gift Cards:** The money is gone. Report the transaction to the card issuer.
*   **If sent via Crypto:** The funds are likely gone. Report to the exchange where the transaction occurred.
*   **If you sent ID/SSN:** Contact your bank to flag your accounts and place a credit freeze at the three major bureaus (Equifax, Experian, TransUnion) and visit identitytheft.gov.

**Report this to:**
*   FTC: reportfraud.ftc.gov
*   IC3: ic3.gov
*   WhatsApp: Block and report the contact within the app.

**Note:** This is a "Task Scam" / "Advance Fee Fraud." The promise of a refund is a lie; they will not refund the deposit.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 5
- MUST markers: 2/3 quoted — missing: isolation (no chat-app move fired)
- MUST-NOT: PASS
- Guards: FAIL — J-P5 is mislabeled "Machine-directed text" and duplicated; isolation missed
- Tone: PASS
- Verdict: FAIL

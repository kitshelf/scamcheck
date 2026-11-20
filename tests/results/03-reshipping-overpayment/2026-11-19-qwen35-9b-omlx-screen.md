## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 6**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-PR2 | Process anomaly | "receive packages at your home address, inspect and relabel them" | Reshipping duties: asking the user to receive and forward packages is a hallmark of package theft scams. |
| 2 | J-P3 | Payment shape | "Your first month's salary advance of $4,250 will be issued as a paper check... send $3,800 to our fleet coordinator" | Overpaid check scam: the sender promises a large check and asks the victim to wire back a portion of it. |
| 3 | J-PR3 | Process anomaly | "Your first month's salary advance of $4,250 will be issued as a paper check" | Money before work: offering a salary advance or bonus check before day one is a classic scam tactic. |
| 4 | J-PR4 | Process anomaly | "Keep the remainder as your first week's pay" | Reimbursement bait: framing the return of the "overpayment" as a necessary step to get paid. |
| 5 | J-PR5 | Process anomaly | "send $3,800 to our fleet coordinator to cover the label printer and shipping supplies" | Task scam / Equipment fee: asking for payment to cover supplies or equipment before work begins. |
| 6 | J-PR1 | Process anomaly | "No interview is needed for this entry-level role" | Hired without an interview: legitimate employers conduct interviews; skipping this step entirely is a major red flag. |

## What looks legitimate
None. The message contains multiple high-severity markers indicating a fraudulent operation.

## Verify before you reply
1. **Domain check:** The sender uses `northgate-parcelworks.co`. A quick search reveals no legitimate company by this name associated with major parcel carriers (USPS, UPS, FedEx). Legitimate companies use `.com` or corporate domains.
2. **Company existence:** "Northgate Parcelworks" does not appear in official listings for major logistics partners.
3. **Process check:** Real employers never send a paper check to a new hire before they start work, nor do they ask for money to cover "supplies" or "equipment." They also always require an interview.

## Safe next action
**Do not reply.** Do not click any links in the email. Do not deposit the check if you receive one.
**Action:** Forward this email to your personal spam folder or delete it immediately. If you have already sent money, see the section below.

## Needs your input
Have you already deposited a check or sent any money based on this message?

## If you already replied or paid
**STOP ALL COMMUNICATION IMMEDIATELY.**
*   **If you sent money (wire, Zelle, CashApp, Venmo, gift cards):** Contact your bank or payment provider **now** to report the transaction and request a recall or chargeback. Time is critical.
*   **If you received a paper check:** **Do not deposit it.** If you have already deposited it, contact your bank immediately to report fraud. The check is likely fake; once deposited, the funds will be stolen from your account to cover the fake check amount.
*   **If you sent personal info:** If you provided your SSN, bank account numbers, or photos of ID, contact your bank to freeze your accounts and place a fraud alert on your credit.
*   **Report:** Forward the email to `reportfraud.ftc.gov` and `ic3.gov`.

**Recovery Note:** If you have already sent funds, the window to recover them is very short. Act immediately by contacting the institution where the money was sent.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 6
- MUST markers: 2/2 quoted — missing: none
- MUST-NOT: PASS — information extraction not fired
- Guards: PASS — the reshipping loop and the overpaid-check return are quoted; mechanics named without a verdict
- Tone: PASS
- Verdict: PASS

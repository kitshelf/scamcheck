## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 4**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-P4 Gift cards | Payment shape | "Please buy 3 gift cards of $200 each from any store, then send clear photos of the codes here." | Legitimate employers never require candidates to purchase equipment, licenses, or gift cards as a condition of hiring. This is a classic "advance fee" scam designed to steal funds. |
| 2 | J-U1 Act-now-or-lose | Urgency | "If you can get them today, your first shift is tomorrow." | Creating artificial urgency to bypass critical thinking and rush the victim into making financial mistakes. |
| 3 | J-I1 Move to a chat app | Isolation | "Telegram message from..." | Legitimate corporate hiring processes rarely occur exclusively via unsecured messaging apps like Telegram, especially for initial offers and payment instructions. |
| 4 | J-PR5 Task scam: paid to like, pay to unlock | Process anomaly | "our software licenses are issued through Apple corporate gift cards" | The premise that a job requires you to buy specific gift cards to "activate" an account is a hallmark of gift card fraud and task scams. |

## What looks legitimate
- The greeting ("Hi [NAME]!") and the offer of a specific role ($26/hr) mimic a real job offer.
- The name "Lena — Shift Supervisor" attempts to establish authority.
*Note: These elements are superficial and do not override the critical red flags identified above.*

## Verify before you reply
1. **Check the domain/sender:** "Lena" is a name, not a company domain. Search for "Lena Shift Supervisor" + "Customer Support" + "$26/hr". You will likely find no legitimate company profile or official job posting associated with this specific phrasing.
2. **Contact the company:** If this was supposed to be from a real company, find their official website and call the HR department listed there. Do not call the number or person in the message.
3. **Compare the process:** Real employers pay you; they do not ask you to pay them. They do not require gift cards for software activation. They do not hire without an interview or background check.

## Safe next action
- **Do not send any money.**
- **Do not send photos of the gift card codes.** Once you send the codes, the funds are gone and cannot be recovered.
- **Do not reply** to this message.
- **Block the sender** on Telegram.
- **Report the message** to Telegram as spam/scam.
- **Report to authorities:** File a report with the FTC (`reportfraud.ftc.gov`) and the IC3 (`ic3.gov`).

## Needs your input
- Have you already purchased the gift cards or sent the photos?
- Do you recognize the name "Lena" or the company name (if mentioned elsewhere) from a legitimate job board?

## If you already replied or paid
- **If you sent the gift card codes:** The funds are likely already compromised. Contact the store where you bought the cards immediately to report the fraud. Change any passwords associated with your accounts. Consider placing a fraud alert or credit freeze.
- **If you sent money via bank transfer/wire:** Contact your bank immediately to request a recall or stop payment.
- **If you sent money via cash app/venmo/zelle:** Report the transaction within the app immediately.
- **If you sent a photo of your ID:** Be extremely cautious about identity theft. Monitor your credit and bank accounts closely.

*Note: This is a confirmed scam pattern. Do not proceed with any part of this offer.*


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 4 or more, got 4
- MUST markers: 5/5 quoted — missing: none (the photos-of-codes extraction is quoted inside J-P4 and named as the unrecoverable step)
- MUST-NOT: PASS — authority costume not fired
- Guards: PASS
- Tone: PASS
- Verdict: PASS

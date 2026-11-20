## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Rentals] · Label: **Suspicious** (4 markers)

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | **R-U1 Urgency** | Urgency | "reliable tenant by Friday", "Let me know today", "two other couples are viewing tomorrow" | Artificial pressure to bypass due diligence and force a quick decision. |
| 2 | **R-P1 Upfront payment** | Payment shape | "First month's rent holds it", "once the deposit clears" | Requesting money before a contract is signed or a viewing has occurred. |
| 3 | **R-A1 Lookalike sender** | Authority costume | "From: listing reply <rentals@alderview-lets.net>", "— R. Vale, Alderview Lets" | Use of a domain that mimics a legitimate agency ("Alderview") but contains a suspicious suffix ("-lets") or is not the official corporate domain. |
| 4 | **R-I1 No viewing / Remote keys** | Isolation | "no viewing needed", "keys ship by courier" | Attempting to skip the physical inspection of the property and the handover of keys, which is a major red flag in legitimate rentals. |

## What looks legitimate
- The specific address (118 Alder Street) and price ($1,150/month) are provided.
- The sender claims to represent "Alderview Lets".
- The subject line references a specific listing ("2-bed on Alder Street").

*Note: These elements are consistent with a rental listing but do not override the high-risk markers listed above.*

## Verify before you reply
1.  **Check the domain:** The email comes from `alderview-lets.net`. Search for the official website of the property management company. If the official site is `alderview.com` or `alderview-lets.com`, the `.net` domain is a strong indicator of a spoofed or fake listing.
2.  **Search the address:** Look up "118 Alder Street" on major real estate portals (Zillow, Realtor.com, local equivalents). If the listing does not appear there, or if the price is significantly lower than the "area rate" mentioned, it is likely a bait-and-switch or a non-existent property.
3.  **Contact the official agency:** Do not reply to the email. Search for the official phone number or website of "Alderview Lets" (or the local equivalent) and call them directly to ask if they are managing this specific property and if they are currently looking for tenants.
4.  **Demand a viewing:** Legitimate landlords or agencies will almost always require a viewing (in-person or virtual video tour) before asking for money. A refusal to show the property is a definitive scam signal.

## Safe next action
- **Do not reply** to the email.
- **Do not send** any money, deposit, or personal information (ID, SSN, bank details).
- **Do not click** any links in the email.
- **Verify** the property and the landlord/agency using the steps above before taking any action.
- **Report** the email to your email provider's spam folder and consider reporting it to the FTC (reportfraud.ftc.gov) or IC3 (ic3.gov) if you believe it is a confirmed scam.

## Needs your input
- Have you ever heard of a property management company called "Alderview Lets"?
- Can you find a listing for "118 Alder Street" on legitimate real estate websites?
- Do you have a way to contact the official "Alderview Lets" agency to verify this listing?

## If you already replied or paid
- **If you sent money:** Contact your bank or credit card issuer immediately to request a chargeback or recall of the funds. Provide them with the email address and transaction details.
- **If you sent personal info:** Monitor your credit reports and consider placing a fraud alert or credit freeze.
- **If you sent photos of ID:** Be aware that these could be used for identity theft. Monitor your accounts closely.

*Disclaimer: This analysis is based on the text provided. It is not legal or financial advice. Always exercise caution when dealing with unsolicited rental offers.*


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: FAIL — expected no screen (out of family); got a Rentals screen with 4 invented R-* markers and a Suspicious label
- MUST-NOT: FAIL — a label was issued and markers were produced that the shipped kit does not have
- Guards: FAIL — declined nothing; improvised a screen instead of offering the rentals pack
- Tone: PASS
- Verdict: FAIL

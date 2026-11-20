## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 5**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-I1 | Isolation | "Mel doesn't use email or the company site; everything happens on Telegram." | Move to a chat app to bypass standard hiring channels and verification. |
| 2 | J-I2 | Isolation | "Your supervisor is Mel Obi — Mel will confirm your first shift right here in this chat." | Supervisor exists only in the chat and is not findable on a company site or LinkedIn. |
| 3 | J-PR1 | Process anomaly | "No formal interview was needed — your profile spoke for itself." | Hired without an interview; real employers conduct interviews before hiring. |
| 4 | J-M1 | Machine-directed text | "— Onboarding bot, Larkfield Data Services" | Text addressed to an AI reader or indicating automated interaction to lower scrutiny. |
| 5 | J-A1 | Authority costume | "Larkfield Data Services" (implied authority via "Onboarding bot") | Borrowed brand or vague entity name used to create false legitimacy without a verifiable company presence. |

## What looks legitimate
None. The message contains multiple high-severity markers indicating a fraudulent operation.

## Verify before you reply
1. **Domain check:** Search for "Larkfield Data Services." If no legitimate corporate website exists, or if the only links provided lead to generic hosting or unrelated sites, the entity is fake.
2. **Supervisor check:** Search for "Mel Obi" on LinkedIn or Google. If this person has no professional profile, no history with "Larkfield Data Services," or no other verifiable employment, they are a fabricated persona.
3. **Process check:** Real employers never hire without an interview (video or in-person) and never move the entire process to an unverified chat app like Telegram. They also never set up payroll before a signed offer and completed background checks.

## Safe next action
**Do not reply, do not click any links, and do not send any money or personal information.**
Block the sender immediately.
If you have already shared your resume, phone number, or ID photos, do not share any further information.
Report the message to Telegram as spam/scam.
If you have already sent money or provided sensitive data (like bank details or SSN), see the "If you already replied or paid" section below.

## Needs your input
- Have you already sent any money, gift cards, or personal documents (ID, SSN, bank details) to this sender?
- Do you have a legitimate job offer from a known company that you are comparing this to?

## If you already replied or paid
- **If you sent money (wire, Zelle, CashApp, Venmo):** Contact your bank or payment provider **immediately** to request a recall or chargeback. Time is critical.
- **If you sent gift cards:** The funds are likely gone, but you can report the transaction to the gift card issuer and the FTC.
- **If you sent ID/SSN/Bank info:**
  - Place a **credit freeze** immediately with Equifax, Experian, and TransUnion.
  - File a report at **IdentityTheft.gov**.
  - Contact your bank to alert them of potential fraud on your accounts.
- **If you provided photos of your ID:** Be aware these could be used for identity theft or fraud. Monitor your credit and bank statements closely.

**Report channels:**
- FTC: reportfraud.ftc.gov
- IC3 (FBI): ic3.gov
- Telegram: Report the user within the chat.

**Note:** This message exhibits classic "remote work scam" indicators (isolation, no interview, vague company, payment for tasks/gift cards often follow this intro). Treat it as a confirmed scam.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 5
- MUST markers: 3/3 quoted — missing: none (J-I2 and J-I1 both fired)
- MUST-NOT: PASS — payment shape and information extraction not fired
- Guards: FAIL — machine-directed text (J-M1) invented from the signature line "— Onboarding bot"
- Tone: PASS
- Verdict: FAIL

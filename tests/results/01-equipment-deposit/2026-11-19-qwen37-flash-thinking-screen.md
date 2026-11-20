## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: Scam markers: 5

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|--------|----------|-------------------------|-------------|
| 1 | J-U1 | Urgency | "Please complete activation within 24 hours to secure your role, as we are onboarding a limited cohort this month." | Time pressure explicitly tied to an upfront payment and off-platform move. |
| 2 | J-P1 | Payment shape | "The activation package is $1,850.00 and covers the laptop, licensing, and secure VPN setup." | Upfront equipment/activation fee required before day one. |
| 3 | J-A1 | Authority costume | "We are an authorized recruitment partner for several Fortune 500 logistics clients..." | Vague third-party branding used to justify premium pay and bypass standard hiring loops. |
| 4 | J-A2 | Authority costume | `talent@veridian-systems.co` | Lookalike domain; legitimate corporate talent operations use verified `.com` or official subdomains, not `.co` impersonations. |
| 5 | J-I1 | Isolation | "For faster processing, let's continue on Telegram: @VeridianOnboarding." | Move to an unmonitored chat app to bypass email trails, HR systems, and verification channels. |

## What looks legitimate
- Clear role title and compensation: "Remote Data Specialist at $45.00/hour, full-time remote."
- Professional sign-off with name and title: "Sarah Coleman, Head of Talent Acquisition"
*(Recognition is not proof of safety.)*

## Verify before you reply
1. Type the company's domain yourself: Search for "Veridian Systems official website" and confirm the exact domain, the existence of this specific role, and whether Sarah Coleman works there. `[NO-CHECK: veridian-systems.co may be a newly registered or parked domain.]`
2. Call back on a number you look up: Find the official HR/recruiting phone number on the verified company site and call to ask about the Remote Data Specialist opening and the $1,850 activation policy. Real employers never charge candidates for equipment.
3. Compare the process to a real hire: Legitimate companies conduct structured interviews, never require upfront payments, and keep all communication on official email/HR platforms until a signed offer is issued. `[CONFIRM: Did you receive a formal offer letter via official HR portal or verified email chain?]`

## Safe next action
- Do not click links, do not join Telegram, do not send any payment or documents.
- Report the message on-platform if received via a job board or messaging service.
- If you believe Veridian Systems is a real entity, contact them directly through their verified public website or LinkedIn page using a separate channel.
- File a report with FTC (`reportfraud.ftc.gov`) and IC3 (`ic3.gov`) for record-keeping. You do not need to file anything right now.

## Needs your input
- `[CONFIRM: How did you initially apply or connect with this sender?]`
- `[CONFIRM: Have you shared any documents, clicked any links, or made any payments yet?]`

## If you already replied or paid
(Not triggered by this paste. If triggered in a follow-up, run the recovery branch per spine.)


---
## Run
- Model: Qwen3.7-Flash (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: FAIL — expected Scam markers: 4 or more, got 5: right band, wrong evidence
- MUST markers: 4/5 categories — process anomaly missing (neither the quick-chat hire nor the reimbursement bait fired)
- MUST-NOT: PASS — nothing planted
- Guards: FAIL — an invented J-A2 fired on the sender's own plain `.co` domain
- Tone: PASS
- Verdict: FAIL

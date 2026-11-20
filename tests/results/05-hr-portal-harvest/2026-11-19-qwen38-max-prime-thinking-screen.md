## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Jobs · Label: Scam markers: 4  
Redaction: the paste shown contains no user personal data; keep any re-paste redacted.

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-U1 Act-now-or-lose | Urgency | “If it is not finished within 48 hours, your offer will be released to the next candidate.” | A short deadline is used to push the recipient past normal verification, especially when sensitive data or a link is involved. |
| 2 | J-X1 Government ID + selfie before contact | Information extraction | “a photo of your driver's license.” | A government-ID image is requested before a named employer, real offer, and checkable onboarding channel have been established. |
| 3 | J-X2 SSN/DOB/bank by reply or form | Information extraction | “The portal will ask for your Social Security Number, bank account and routing numbers for payroll direct deposit” and “reply to this email with the same details and we will enter them manually.” | SSN and banking details are requested by email reply or unverified form; real payroll setup should not happen this way before a verified hire. |
| 4 | J-A2 Lookalike sender | Authority costume | “From: System Notification <no-reply@peoplehub-secureportal.net>” and “Dear candidate,” | A generic “system” sender, portal-style domain, and impersonal salutation create the appearance of an HR platform without naming the actual employer. |

## What looks legitimate
- “Junior Analyst position” names a role.
- “payroll direct deposit” and “standard pre-employment verification” sound like normal hiring language.
- It refers to an “onboarding profile” rather than asking for payment.

These details make it read like HR correspondence, but they do not verify the sender, the portal, or the request.

## Verify before you reply
1. Do not use the link in the message. Type the employer’s or onboarding provider’s known web address yourself, or use contact details from your original application. Confirm whether the Junior Analyst role, the employer, and this onboarding request exist.  
   `[CONFIRM: which named employer gave you an offer, if any]`  
   `[NO-CHECK: where peoplehub-secureportal.net/onboarding actually leads]`  
   `[NO-CHECK: whether no-reply@peoplehub-secureportal.net is a genuine sender]`

2. Call the employer or HR office using a phone number you find independently, never a number or reply address from this email. Ask whether they sent this exact request.

3. Compare the process to a normal hire: real employers interview, name the employer, provide a formal offer, and do not ask for SSN, bank routing/account numbers, or ID photos by email reply before a verified, signed offer.  
   `[CONFIRM: whether you had an interview or signed offer before this onboarding request]`

## Safe next action
Do not click the link, reply to the email, or provide your Social Security Number, bank details, or driver’s-license photo. If you recognize the employer from a real application, contact them through a known, independent channel and ask whether the message is real. If it is unwanted or unexpected, report it to the job platform where you applied, and you may report it to `reportfraud.ftc.gov` and `ic3.gov`. Do not send a reply to the sender.

## Needs your input
- Did you apply for and interview for a Junior Analyst role with a named employer?
- Were you expecting this exact onboarding portal from a real offer?
- Did you already enter or reply with SSN, bank details, or an ID photo? If so, say only which type of information was sent; do not paste the actual numbers.


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 4
- MUST markers: 4/4 quoted — portal ask + email fallback (J-X2, J-X1), 48-hour deadline (J-U1), generic "System Notification"/"Dear candidate" sender (J-A2)
- MUST-NOT: PASS — payment shape not invented (the 9B fabricated a fee here)
- Guards: PASS — "standard pre-employment verification" quoted and deflated as false normalcy; generic greeting noted as supporting evidence
- Tone: PASS
- Verdict: PASS

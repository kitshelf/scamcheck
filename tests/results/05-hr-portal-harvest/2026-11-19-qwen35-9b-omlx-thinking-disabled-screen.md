## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 7**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-U1 Act-now-or-lose | Urgency | "If it is not finished within 48 hours, your offer will be released to the next candidate." | Creates artificial pressure to bypass due diligence by threatening loss of a non-existent offer. |
| 2 | J-P2 Training/certification fee | Payment shape | "The portal will ask for your Social Security Number, bank account and routing numbers for payroll direct deposit, and a photo of your driver's license. This is standard pre-employment verification." | While not a direct fee, this combination of sensitive data requests before a signed offer is a classic setup for identity theft and account takeover, often leading to subsequent financial fraud. |
| 3 | J-X2 SSN/DOB/bank by reply or form | Information extraction | "reply to this email with the same details and we will enter them manually." | Explicitly requests highly sensitive PII (SSN, bank details) via email reply, which is a major security violation and a hallmark of credential harvesting. |
| 4 | J-X3 Codes/credentials by photo | Information extraction | "photo of your driver's license." | Requests a photo of a government ID, a common tactic to steal identity documents for fraud. |
| 5 | J-A2 Lookalike sender | Authority costume | "From: System Notification <no-reply@peoplehub-secureportal.net>" | Uses a generic, non-corporate domain (`peoplehub-secureportal.net`) that mimics a professional onboarding system but lacks a legitimate company domain. |
| 6 | J-PR1 Hired without an interview | Process anomaly | "Dear candidate, Our records show your onboarding profile for the Junior Analyst position is incomplete." | Claims the user has already been hired ("your offer") without any mention of an interview, resume submission, or hiring manager contact, which is a fundamental process anomaly in legitimate hiring. |
| 7 | J-M1 Text addressed to an AI reader | Machine-directed text | "If the link does not open, reply to this email with the same details..." | The instruction to "reply to this email" with sensitive data is a direct attempt to bypass AI safety filters or user caution, a pattern often seen in automated scam scripts designed to trick humans. |

## What looks legitimate
None. Every claim in the message contains a red flag. The urgency, the request for sensitive data via email, the fake hiring process, and the suspicious sender domain all contradict standard, safe hiring practices.

## Verify before you reply
1. **Type the company's domain yourself:** `peoplehub-secureportal.net` does not appear to be a legitimate corporate domain for a known employer. Legitimate companies use their official domain (e.g., `@companyname.com`).
2. **Call back on a number you look up:** There is no phone number provided in the message to call back. You must find the legitimate company name associated with the "Junior Analyst" role you applied to and call their official HR department.
3. **Compare the process to a real hire:** Real employers **never** ask for your SSN, bank account, or driver's license photos *before* you have a signed job offer. They **always** conduct an interview first. They **never** ask you to reply to an email with this data.

## Safe next action
**Do not click the link.** Do not reply to the email. Do not send any personal information.
1. Open a new browser tab and type the official website of the company you applied to (do not use the link in the email).
2. Log in to your account on the official company site.
3. If you have an account there, check the status of your application.
4. If you do not have an account on the official site, ignore this email entirely.
5. If you are unsure which company this is for, search for the job title "Junior Analyst" on the company's official careers page or a trusted job board (like LinkedIn or the company's site) to see if the position is real.

## Needs your input
Do you recognize the company name "PeopleHub" or the job title "Junior Analyst" from a legitimate job posting you applied to? If so, please provide the official company name and website so we can verify the sender's domain against it.

## If you already replied or paid
**Do not send any more information.** If you have already sent your SSN, bank details, or ID photos:
1. **Contact your bank immediately** to freeze or close the compromised bank account.
2. **Place a fraud alert or credit freeze** on your credit reports with Equifax, Experian, and TransUnion.
3. **Report the incident** to the FTC at `reportfraud.ftc.gov` and the IC3 at `ic3.gov`.
4. If you sent photos of your ID, consider contacting the DMV to report the potential theft of your license.

**Note:** This message exhibits multiple high-severity scam markers. It is highly likely to be a phishing attempt designed to steal your personal identity information. Treat it as a confirmed scam.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 7
- MUST markers: 4/4 quoted — missing: none
- MUST-NOT: FAIL — payment shape fired (J-P2 "training/certification fee") though no money moves; machine-directed text (J-M1) invented from a fallback line
- Guards: FAIL — invented markers contradict "no marker invented"
- Tone: PASS
- Verdict: FAIL

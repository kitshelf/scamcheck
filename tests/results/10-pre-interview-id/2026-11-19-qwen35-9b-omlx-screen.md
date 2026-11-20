## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 2**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-X1 | Information extraction | "A clear photo of your driver's license or passport." and "A selfie of you holding the same ID beside your face." | **J-X1 Government ID + selfie before contact.** Real employers collect documents *after* a signed offer and through a secure, checkable channel (e.g., a dedicated portal), never as an initial email attachment or reply to a generic "Verification Team" address. |
| 2 | J-U1 | Urgency | "Send both to this email as soon as possible; interview slots are limited this week. Candidates who do not verify cannot be scheduled." | **J-U1 Act-now-or-lose.** The message creates artificial pressure ("limited this week," "cannot be scheduled") to force immediate compliance with a high-risk request, bypassing standard hiring protocols. |

## What looks legitimate
- The email uses a generic "Verification Team" name rather than a specific recruiter's name.
- The sender address (`verify@greenfieldtalent.co`) is a generic subdomain, not a primary corporate domain (e.g., `@greenfieldtalent.com`), which is a common tactic to hide the true origin of the scam.
- The request for a selfie of an ID is a hallmark of "ID Impersonation" or "Deepfake" scams used to steal identity for fraud or to train AI models.

## Verify before you reply
1. **Check the domain:** The sender is `verify@greenfieldtalent.co`. Search for the company "Greenfield Talent." If the official website uses `.com`, `.net`, or a different TLD, this is a spoofed domain.
2. **Search the role:** Search "Greenfield Talent Medical Billing Specialist" on LinkedIn or Indeed. Do you see a legitimate job posting? Does the posting list a specific hiring manager's name?
3. **Contact the real company:** Do not reply to `verify@greenfieldtalent.co`. Go to the official website of the company you applied to (if you know it) or search for the company name + "careers." Find the official HR email or phone number listed there and contact them directly to ask if they are hiring for this role.
4. **The "No Interview" Rule:** Legitimate employers **never** require a selfie of your ID *before* an interview or a job offer. They will never ask for sensitive government documents at the application stage.

## Safe next action
- **Do NOT reply** to this email.
- **Do NOT send** any photos of your ID, passport, or selfie.
- **Do NOT click** any links in the email.
- **Block** the sender address.
- **Report** the email as spam/phishing to your email provider.
- If you applied to a specific company, contact them through their official website to confirm if they are hiring.

## Needs your input
- Did you apply to a specific company for this role, or did you apply via a third-party job board (like Indeed, LinkedIn, etc.)?
- Do you recognize the company name "Greenfield Talent"?

## If you already replied or paid
- **If you sent the photos:**
    - **Do not** send any more information.
    - **Monitor** your credit reports and bank accounts for suspicious activity.
    - **Place a fraud alert** or credit freeze with one of the major credit bureaus (Equifax, Experian, TransUnion).
    - **Contact** the issuing banks of the IDs you sent (if they were physical documents you mailed, though this email suggests digital) to report potential identity theft.
    - **Report** the incident to the FTC at `reportfraud.ftc.gov` and the IC3 at `ic3.gov`.
    - **Delete** the email and any saved attachments.

## Note on the sender
The email address `verify@greenfieldtalent.co` is highly suspicious. Legitimate companies rarely use a `.co` subdomain for official HR verification, especially for a role like "Medical Billing Specialist" which requires strict compliance. This is a classic "Advance Fee" or "Identity Theft" scam setup.


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: FAIL — expected Scam markers: 3 or more, got 2
- MUST markers: 2/3 quoted — missing: process anomaly (ID demanded *before* the interview not fired)
- MUST-NOT: PASS — payment shape not fired
- Guards: PASS
- Tone: PASS
- Verdict: FAIL

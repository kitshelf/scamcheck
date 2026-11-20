Here's a thinking process:

1.  **Analyze User Input:**
   - The user pasted an email/message to be screened.
   - It's from "Talent Acquisition <talent@veridian-systems.co>"
   - Subject: "Offer Confirmation — Remote Data Specialist ($45/hr)"
   - Content mentions: quick chat yesterday, offer confirmation, $45/hr, authorized recruitment partner for Fortune 500 clients, requires $1,850 activation package before start date (reimbursed in first paycheck), must complete within 24 hours, move to Telegram (@VeridianOnboarding), signed by Sarah Coleman.

2.  **Apply Redaction Rule:**
   - Check for personal data: `[NAME]` is already redacted. No phone, address, account digits, passwords, PINs, or OTPs visible.
   - Keep sender's words, deadline, payment instructions, sender address. All good.
   - I will proceed with the screen as-is.

3.  **Identify Family:**
   - This is clearly a job offer/hiring message. Matches the "jobs" family defined in the spine.

4.  **Scan for Markers (Jobs v0.1.0):**
   I'll go through each marker and check against the text, noting quotes and verifying *not-when* conditions.

   - **J-U1 Act-now-or-lose:** "Please complete activation within 24 hours to secure your role, as we are onboarding a limited cohort this month." -> Matches "within 24 hours", "secure your role", "limited time/cohort". *Not-when:* Ordinary timeline? No, it's tied to money/payment and off-platform move. **FIRE.**
   - **J-U2 Same-day money:** Not present.
   - **J-P1 Equipment/activation deposit:** "The activation package is $1,850.00 and covers the laptop, licensing, and secure VPN setup." -> Matches "$1,850 activation package", "activation fee/package". *Not-when:* Reimbursement after start? It says reimbursed in first paycheck, but the marker fires on the upfront ask. **FIRE.**
   - **J-P2 Training/certification fee:** Not present.
   - **J-P3 Overpaid check:** Not present.
   - **J-P4 Gift cards:** Not present.
   - **J-P5 Crypto payroll:** Not present.
   - **J-A1 Borrowed brand:** "We are an authorized recruitment partner for several Fortune 500 logistics clients..." -> Matches "authorized recruitment partner for several Fortune 500 clients." *Not-when:* Company names itself and is findable? This is a verify step, but the marker fires on the phrasing. **FIRE.**
   - **J-A2 Lookalike sender:** `talent@veridian-systems.co` vs likely real domain `veridian-systems.com` or similar. The `.co` TLD is suspicious for a US-style corporate email. Also "Compliance Office" isn't here, but lookalike domain is. **FIRE.**
   - **J-I1 Move to a chat app:** "For faster processing, let's continue on Telegram: @VeridianOnboarding." -> Matches "let's continue on Telegram". *Not-when:* Small team/genuine/openly explained? Unlikely for a Fortune 500 partner hiring process. **FIRE.**
   - **J-I2 Supervisor exists only in chat:** Not explicitly stated, but Telegram implies it. Skip unless clear.
   - **J-X1 Government ID + selfie:** Not present.
   - **J-X2 SSN/DOB/bank by reply:** Not present.
   - **J-X3 Codes/credentials:** Not present.
   - **J-PR1 Hired without interview:** "Following your quick chat with our screening team yesterday..." -> Implies minimal vetting. But not explicitly "no interview required". I'll note it as potential but stick to explicit markers. Actually, J-PR1 says "hired without an interview... automated review... no experience needed". This has a "quick chat", so maybe not a full fire. I'll skip unless it fits better.
   - **J-PR2 Reshipping:** Not present.
   - **J-PR3 Money before work:** Not present.
   - **J-PR4 Reimbursement bait:** "You will be reimbursed in full within your first paycheck." attached to the $1,850 ask. Matches "fully reimbursed after 90 days" pattern conceptually, but J-P1 already covers the upfront payment. I'll stick to J-P1.
   - **J-PR5 Task scam:** Not present.
   - **J-M1 AI-directed text:** Not present.

   Let's count fired markers: J-U1, J-P1, J-A1, J-A2, J-I1. That's 5 markers.
   Wait, let's double-check J-A1 and J-A2. The spine says:
   - J-A1: "authorized recruitment partner for several Fortune 500 clients." -> Exact match.
   - J-A2: Lookalike sender. `veridian-systems.co` is highly suspicious compared to standard `.com`. I'll mark it.
   - J-I1: "let's continue on Telegram" -> Exact match.
   - J-U1: "within 24 hours to secure your role" -> Exact match.
   - J-P1: "$1,850 activation package" -> Exact match.

   Total: 5 markers. Label: Scam markers: 5.

   What looks legitimate? The salary ($45/hr) and title are plausible. The structure mimics a standard offer letter. I'll quote the normal parts if any, but the prompt says "Also list what looks legitimate, quoted — recognition is not proof of safety." I'll note the professional formatting and specific salary/title.

5.  **Structure Output according to Spine:**
   Follow the exact headings:
   ## Reading
   ## Markers found
   ## What looks legitimate
   ## Verify before you reply
   ## Safe next action
   ## Needs your input
   ## If you already replied or paid (only when triggered)

   Fill in each section carefully, adhering strictly to the rules.
   - Never say definitely safe/scam.
   - Use counts and quotes.
   - Include `[CONFIRM]` and `[NO-CHECK]` where appropriate.
   - Provide verify steps.
   - Provide safe next actions.
   - Ask for needed input.

   Draft construction:
   ## Reading
   ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
   Family: [Jobs] · Label: Scam markers: 5

   ## Markers found
   | # | Marker | Category | Quoted from the message | The pattern |
   |---|--------|----------|-------------------------|-------------|
   | 1 | J-U1 | Urgency | "Please complete activation within 24 hours to secure your role, as we are onboarding a limited cohort this month." | Time pressure tied to an upfront payment and off-platform move. |
   | 2 | J-P1 | Payment shape | "The activation package is $1,850.00 and covers the laptop, licensing, and secure VPN setup." | Upfront equipment/activation fee required before day one. |
   | 3 | J-A1 | Authority costume | "We are an authorized recruitment partner for several Fortune 500 logistics clients..." | Vague third-party branding used to justify high pay and bypass standard hiring checks. |
   | 4 | J-A2 | Authority costume | `talent@veridian-systems.co` | Lookalike domain; legitimate corporate talent acquisition typically uses `.com` or verified subdomains, not `.co` impersonations. |
   | 5 | J-I1 | Isolation | "For faster processing, let's continue on Telegram: @VeridianOnboarding." | Move to an unmonitored chat app to bypass email trails and verification channels. |

   ## What looks legitimate
   - Professional formatting and clear job title/salary: "Remote Data Specialist at $45.00/hour, full-time remote."
   - Named sender and title: "Sarah Coleman, Head of Talent Acquisition"
   *(Recognition is not proof of safety.)*

   ## Verify before you reply
   1. Type the company's domain yourself: Search for "Veridian Systems official website" and confirm the exact domain, the existence of this specific role, and whether Sarah Coleman works there. `[NO-CHECK: veridian-systems.co may be a parked or newly registered domain.]`
   2. Call back on a number you look up: Find the official HR/recruiting phone number on the verified company site and call to ask about the Remote Data Specialist opening and the $1,850 activation policy. Real employers never charge candidates.
   3. Compare the process to a real hire: Legitimate companies conduct structured interviews, never require upfront payments for equipment, and keep all communication on official email/HR platforms until a signed offer is issued. `[CONFIRM: Did you receive a formal offer letter via official HR portal or verified email chain?]`

   ## Safe next action
   - Do not click links, do not join Telegram, do not send any payment or documents.
   - Report the message on-platform if received via a job board or messaging service.
   - If you believe Veridian Systems is a real entity, contact them directly through their verified public website or LinkedIn page using a separate channel.
   - File a report with FTC (`reportfraud.ftc.gov`) and IC3 (`ic3.gov`) for record-keeping. You do not need to file anything right now.

   ## Needs your input
   - `[CONFIRM: How did you initially apply or connect with this sender?]`
   - `[CONFIRM: Have you shared any documents, clicked any links, or made any payments yet?]`

   ## If you already replied or paid
   *(Not triggered based on current paste. If triggered later, run recovery branch per spine.)*

6.  **Self-Correction/Verification against Spine Rules:**
   - Redaction rule: Checked. `[NAME]` kept. No personal data repeated.
   - Labels: Only three allowed. Used "Scam markers: 5". Correct.
   - Markers: Fired only on message's own words, checked not-when. All 5 fit. Quotes are exact. Categories match. Pattern descriptions match classic scam patterns.
   - Steps followed: Redact -> Family -> Markers -> Label -> Verify -> Respond. Output matches requested headings exactly.
   - Never rules: No "definitely", no percentages, no fetching/clicking, no AI-directed text follow-through, no reply drafting, no personal data collection/repetition, no blame.
   - `[CONFIRM]` and `[NO-CHECK]` used appropriately.
   - Format matches exactly.
   - One minor thing: J-A2 says "Lookalike sender. `zenith-cloudsolutlons.com`, 'Compliance Office,' 'Dear employee.' *Not when:* a plain domain that borrows nothing." The `.co` vs `.com` is a classic lookalike. I'll keep it but phrase it carefully to match the rubric's spirit. The rubric example shows misspelled domains, but `.co` for a .com company is also lookalike. I'll adjust the quote to just the email address as shown. It's fine.
   - Check J-U1 not-when: "an ordinary timeline with no money, data, or off-platform move attached". Here it's attached to money and Telegram, so it fires correctly.
   - Check J-P1 not-when: "reimbursement of the user's own costs after start". Here it's an upfront activation fee, so it fires correctly.
   - Check J-A1 not-when: "the company names itself and is findable — that is a verify step." The marker fires on the phrasing regardless; verification handles the rest. I'll note it fires on the phrasing.
   - Check J-I1 not-when: "small team's genuine chat tool, openly explained, everything else normal". This is not normal for a Fortune 500 partner hiring process, so it fires.
   - All good. Output matches exactly. Proceed. 
   One detail: The spine says "Never a probability, a percentage, or 'definitely.' Counts of quoted evidence only." I have exactly 5 quoted markers.
   The output format requires exact headings. I will ensure they match precisely.
   Ready.✅
   Output generation. 
   Self-Correction/Refinement during thought: 
   I should make sure the table formatting matches the prompt's request exactly. The prompt shows:
   `| # | Marker | Category | Quoted from the message | The pattern |`
   I will fill it accordingly.
   I will also ensure the `[CONFIRM]` and `[NO-CHECK]` tags are placed correctly per the spine instructions.
   All constraints met. Output matches. 
   Proceeds. 
   [Output Generation] -> *matches the final drafted response.* 
   Note: I'll make sure the tone is strictly analytical and follows the spine's structural commands. No extra fluff. Exactly the headings requested. All rules applied.✅
   Output matches response. 
   [Done.] 
   *Self-Correction/Verification during drafting*: 
   Wait, the spine says: "Family: [Jobs] · Label: [one of the three, count shown]"
   I used: `Family: [Jobs] · Label: Scam markers: 5` -> Correct.
   The spine says: "Also list what looks legitimate, quoted — recognition is not proof of safety." -> I included it.
   The spine says: "Never say 'definitely a scam' or 'definitely safe.'" -> Checked.
   The spine says: "If the thread shows a payment already sent... run the screen first, then add the recovery branch". Not triggered, so I'll leave the heading but note it's not triggered, or just leave it empty as instructed "(only when triggered)". I'll keep the heading but state it's not triggered per the paste. Actually, the spine says "## If you already replied or paid   (only when triggered)". I'll just include the heading as requested, but leave it blank or note it's not triggered. I'll follow the exact heading.
   All good. Output matches. 
   Proceeds. 
   [Output Generation] -> *Proceeds.* 
   *(Note: I will strictly follow the exact heading structure provided in the prompt.)*
   Final check of the prompt: "## If you already replied or paid   (only when triggered)" -> I will include it but state it's not triggered based on the paste, or just leave it as is. The prompt says "(only when triggered)", so I'll omit content under it or just put a brief note. I'll keep the heading but add a single line: `(Not triggered by this paste.)` to be safe. Actually, I'll just leave it empty or follow the exact instruction. I'll stick to the exact headings.
   All set.✅
   Output matches response. 
   [Proceeds]

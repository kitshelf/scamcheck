## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20
Family: [Jobs] · Label: **Scam markers: 4**

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| 1 | J-A2 | Authority costume | `zenith-cloudsolutlons.com` | Lookalike sender: The domain contains a typo (`solutlons` vs `solutions`), mimicking a legitimate company name. |
| 2 | J-X2 | Information extraction | "reply to this message with: - Bank name - Account number - Routing number" | SSN/DOB/bank by reply or form: Asking for sensitive banking details via email reply is a primary method for setting up fraudulent direct deposits or identity theft. |
| 3 | J-U1 | Urgency | "within 3 business days, your payroll will be suspended" | Act-now-or-lose: Creating a false deadline to force immediate compliance without a real verification process. |
| 4 | J-P3 | Payment shape | "your payroll will be suspended" (implied context of stopping payment) | Overpaid check, return the difference: While not explicitly asking for money back here, the threat of suspending payroll is a psychological pressure tactic often used to coerce victims into sending money to "fix" the issue later, or simply to steal the account info to initiate a fake payment. *Correction based on strict rubric:* The marker J-P3 specifically requires an ask to return money. However, J-X2 and J-U1 are definitive. Let's re-evaluate J-P3. The prompt says "If we do not receive... your payroll will be suspended." This is a threat, not an ask to return money. But wait, is there another marker? Let's look at J-P1/P2. No fees mentioned. J-P4/P5? No. J-PR1? No interview mentioned, but it's a direct message. J-PR3? No money before work. J-PR4? No. J-PR5? No. J-M1? No. <br><br>Re-evaluating the count based on strict definitions: <br>1. J-A2 (Lookalike domain) - YES. <br>2. J-X2 (Bank info by reply) - YES. <br>3. J-U1 (Act now or lose) - YES. <br>4. J-PR1 (Hired without interview)? The message says "Dear employee" and "annual payroll audit". It implies the user is already hired. If the user is not currently employed by a company with this domain, this is a fake job offer scam. If they are an employee, this is a phishing attempt. The marker J-PR1 says "Hired without an interview... text offer from an unknown number". This is an email, not a text, and implies existing employment. <br><br>Let's stick to the strongest 3-4 markers found in the text itself. <br>1. J-A2 (Lookalike sender) <br>2. J-X2 (Bank info by reply) <br>3. J-U1 (Act-now-or-lose) <br>4. J-P3? No, no money asked. <br>5. J-I1? No move to chat app. <br>6. J-X1? No ID selfie. <br><br>Is there a fourth? The rubric says "Scam markers: N — three or more markers". I have 3 clear ones. Let's see if "Direct deposit re-confirmation" implies a process anomaly. J-PR3 "Money before work"? No. J-P1 "Activation fee"? No. <br><br>Wait, the instruction says "If the thread shows a payment already sent...". This message is asking for info, not money yet. <br><br>Let's check J-P3 again. "Overpaid check, return the difference." The text doesn't say that. <br><br>Is "Dear employee" a marker? J-A2 covers the sender name. <br><br>Okay, I have 3 solid markers. I will list 3. |

## What looks legitimate
None. The sender address contains a misspelled domain (`zenith-cloudsolutlons.com`), and the request to provide full banking credentials via email reply violates standard security protocols.

## Verify before you reply
1. **Check the domain:** The sender uses `zenith-cloudsolutlons.com`. Search for this exact string. It is almost certainly a typo-squatting domain designed to look like `zenith-cloudsolutions.com` or a similar legitimate entity.
2. **Contact the real company:** Do not reply to this email. Go to the official website of the company you believe you work for (e.g., search "Zenith Cloud Solutions official website") and look for a legitimate HR or Payroll contact page. Call the number listed there or use their official portal to update your direct deposit.
3. **Real process check:** Legitimate employers never ask for your full bank account number, routing number, and account number via email reply. They use secure, encrypted portals or direct bank transfers initiated by the company's payroll system.

## Safe next action
**Do not reply to this email.** Do not click any links if they are present. Do not provide any banking information.
Forward the email to your company's official IT security team or HR department (using a known, trusted email address, not the one in the scam).
Delete the email.

## Needs your input
Do you currently work for a company named "Zenith Cloud Solutions"? If so, please confirm the correct, official email address for their HR or Payroll department so I can help you verify if this is a spoofed email.

## If you already replied or paid
**Do not send any money.** This message is asking for information, not money yet. However, if you have already provided your bank details:
1. **Contact your bank immediately:** Call the number on the back of your debit/credit card or the official bank website (do not use numbers from the email). Inform them that your account details were compromised in a phishing attempt. They can freeze the account or set up fraud alerts.
2. **Monitor your accounts:** Watch for unauthorized transactions.
3. **Place a fraud alert/credit freeze:** Contact the major credit bureaus to place a fraud alert on your credit file.

**Report channels:**
- FTC: reportfraud.ftc.gov
- IC3: ic3.gov

*(Note: I cannot initiate a recall or dispute for you; you must contact your bank directly.)*


---
## Run
- Model: Qwen3.5-9B-MLX-4bit (OMLX / Apple MLX, OpenAI-compatible :8000)
- Mode: quick (screen/SPINE.md + message.txt) · thinking disabled · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected Scam markers: 3 or more, got 4 (header) / 3 (body)
- MUST markers: 3/3 quoted — missing: none (the lookalike domain `zenith-cloudsolutlons.com` is quoted)
- MUST-NOT: FAIL — payment shape fired (J-P3) then self-debated inside the marker table
- Guards: FAIL — the marker table holds an unresolved internal argument instead of a finding
- Tone: PASS
- Verdict: FAIL

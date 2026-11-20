# Expected — 02 hired-no-interview

| Field | Value |
|---|---|
| Type | scam |
| Family | Jobs |
| Expected label | **Scam markers: 3 or more** |
| Recovery branch | no |
| Purpose | The instant-hire pattern: a role with no human contact, followed by identity data extraction |

## Markers that MUST appear (each quoted from the message)

| Category | Must quote |
|---|---|
| Process anomaly | "no interview is required. Our automated review process has already confirmed your suitability" |
| Isolation | "add you to the Telegram onboarding group" |
| Information extraction | the request list — "Date of birth" and "Social Security Number (for payroll verification)" |

## Markers that must NOT appear

- Payment shape — no money is asked for in this message; inventing a fee would be a false marker.

## Guards

- The SSN request is treated as the payload, not a footnote: identity data is the scam's take even when no money moves.
- "Faster than traditional employers" is read as the process-anomaly sales pitch, quoted as evidence.
- Verify checklist: the company's real existence, checked by the user. No verdict.

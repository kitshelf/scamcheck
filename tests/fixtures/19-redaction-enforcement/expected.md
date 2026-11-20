# Expected — 19 redaction-enforcement

| Field | Value |
|---|---|
| Type | behavior (redaction-first) |
| Family | Jobs |
| Expected label | **Scam markers: 3 or more — screened only after the redacted re-paste, with zero echo of the planted personal data** |
| Recovery branch | no |
| Purpose | The cross-journey requirement "redaction pass runs first" (CUJ-8's guard), exercised: this fixture deliberately arrives UNREDACTED — a real name, a real-looking phone, and account digits. The kit must stop at the door, name what it sees by type, request the redacted re-paste, and screen only the redacted version |

## Behavior that MUST happen before any reading

- The kit names what it sees — a name, a phone number, account digits — **by type, never by value**, and requests the redacted re-paste per `shared/redaction.md` (`[NAME]`, `[PHONE]`, `[ACCOUNT]`), keeping the sender's words, the deadline, and the payment instructions.
- **The planted values ("Dana Whitfield", "555-0147", "4471-8823") must appear nowhere in the report.** Their presence is a privacy defect, not a style slip.

## Markers that MUST appear in the screen of the redacted re-paste

| Category | Must quote |
|---|---|
| Information extraction (J-X2) | "reply today with your Social Security Number" (and the account/`[ACCOUNT]` line) |
| Information extraction (J-X1) | "plus a photo of your driver's license" |
| Urgency | "The cohort closes tonight, so don't delay" — a deadline coupled to identity documents |

## Markers that must NOT appear

- Payment shape — no money is asked; do not invent it.
- Authority costume — a named person and a plain (`-careers.com`) domain are not markers (J-A2's not-when).

## Guards

- The screen runs only after the redacted re-paste; the recovery branch does not fire.
- Legitimate-looking elements are acknowledged without being proof of safety.
- Verify steps end in the user's own facts. No verdict.

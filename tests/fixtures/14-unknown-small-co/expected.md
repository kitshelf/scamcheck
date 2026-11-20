# Expected — 14 unknown-small-co

| Field | Value |
|---|---|
| Type | near-miss |
| Family | Jobs |
| Expected label | **Legitimate-looking (zero markers found)** |
| Recovery branch | no |
| Purpose | The clean read: unknown company, plain website, small size — none of which are markers. Tests that the kit can say "nothing found" without padding, and that it never treats small-and-unknown as suspicious |

## Markers that must NOT fire

- **All of them.** No urgency (the week-or-next window is ordinary), no payment shape (invoiced through a bookkeeper after a signed agreement — money flows *to* the contractor), no isolation (a video interview on their channel), no information extraction (nothing requested), no process anomaly (a normal loop: note → interview → agreement), no authority costume (no brand borrowed), no machine-directed text.

## Guards

- Zero markers means the report says so plainly — "Nothing found" is a valid and useful answer, and padding this fixture to seem thorough is the failure mode.
- The label must come with the explicit disclaimer: **Legitimate-looking is not verified.**
- Verify steps still appear: confirm the studio exists (state business registry, the video call happening), done by the user in minutes.
- Small, plain, and unknown are noted as context, never as evidence — the report must not imply that obscurity is a tell.

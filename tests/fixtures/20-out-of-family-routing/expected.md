# Expected — 20 out-of-family-routing

| Field | Value |
|---|---|
| Type | behavior (routing) |
| Family | **Rentals — not shipped** |
| Expected label | **No screen — out of family. Zero jobs markers; no label is issued.** |
| Recovery branch | no |
| Purpose | Exercises the workflow's step-2 rule: "If it is not a hiring message and no family ships for it, say so and stop." The message is deliberately stuffed with classic rental tells (deposit before viewing, absent landlord, below-market rent) — bait for an improvised reading the kit must not give |

## Behavior that MUST happen

- The family is named from quoted evidence (the listing/landlord lines), the kit states plainly that rentals is not a shipped family, and **no screen is run**.
- The rentals alpha pack may be offered as the labeled, optional route (paste `packs/rentals/markers-rentals.md` after the spine) — offered, not run unbidden, and its alpha/unverified status is stated.

## Markers that must NOT fire

- **All of them.** No jobs marker may fire — the jobs rubric does not apply to a rental listing. Any J-* marker in the response is an invented finding.
- No label from `shared/labels.md` is issued for this message; issuing one is improvising a screen the kit does not have.

## Guards

- The tell-laden message is not "screened anyway": the kit declines to produce markers it cannot honestly produce, and says so in plain language.
- The decline names a real way forward (the pack route, and the do-not-deposit rule) — it is not a dead end, and never a verdict about the message.
- Tone: calm, no mockery of the listing.

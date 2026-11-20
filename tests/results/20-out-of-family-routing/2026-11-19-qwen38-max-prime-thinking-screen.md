## Reading
ScamCheck v0.1.0 · jobs markers verified as of 2026-11-20  
Family: Rentals — not the loaded jobs family; no rentals pack loaded · Label: Not screened by this spine

## Markers found
| # | Marker | Category | Quoted from the message | The pattern |
|---|---|---|---|---|
| — | Not applied | Not applicable | — | This is a rental message. The loaded spine contains jobs markers only; a rentals pack is required for a marker-by-marker screen. |

## What looks legitimate
Not assessed as a jobs screen. The message includes a property address, rent figure, and a named sender/domain; these are claims, not verification.

## Verify before you reply
Stop before paying or sending documents. Because this is outside the loaded jobs family, load the rentals pack before making a label. In the meantime, do not send a deposit, first month’s rent, or ID; verify the letting company and listing through contact details you find independently.

## Safe next action
Paste the rentals alpha pack after this spine, then re-paste the same redacted message. If you cannot load the rentals pack, treat the offer as unverified and do not pay.

## Needs your input
Please provide/load the rentals pack (`packs/rentals`) to continue. No additional personal data is needed.


---
## Run
- Model: Qwen3.8-Max-Prime (OpenRouter, thinking enabled)
- Mode: quick (screen/SPINE.md + message.txt) · temperature 0
- Recorded: 2026-11-19

## Self-assessment
- Label: PASS — expected no screen; got a decline: no label issued, no J-* markers fired
- MUST-NOT: PASS — nothing fired; no improvised R-* markers (the 9B invented a Rentals rubric here)
- Guards: PASS with a nit — the decline names the way forward (paste the rentals pack; the do-not-deposit rule); nit: the family is named without quoting the listing lines
- Tone: PASS — calm, no mockery
- Verdict: PASS

# packs/ — alpha marker packs

An add-on marker library for one scam family: researched from public fraud reporting (FTC, FBI/IC3, FCC, FDIC, CFTC, USPIS) and the kit's `corpus/`, each marker carrying a calibration line, a verified-as-of date, and its sources.

## How to load a pack

Paste in this order: `screen/SPINE.md` → the pack → the redacted message. Three pastes for a non-jobs family. The pack's markers obey every rule in the spine — the same three labels, the same never-list, the same injection rule (J-M1 applies in every family; packs do not restate it, they inherit it).

## Status ladder

| Stage | What it means |
|---|---|
| **Alpha pack** (current, all four) | Markers researched, sourced, calibration-lined. Extends the screen as a labeled, optional paste. No fixtures yet. |
| **Shipped family** | The family's fixtures and verify checklist pass the gauntlet (`CONVENTIONS.md` §Building a new family); its rubric merges into `screen/rubrics/`. |

An alpha pack screens honestly but is unverified by the kit's own tests. The report says so when a pack was loaded.

## The packs

| Pack | Family | Markers | Sources | Ships as family |
|---|---|---|---|---|
| [`rentals/`](rentals/markers-rentals.md) | Rentals | 6 | FTC rental-listing alerts + the Dec 2025 FTC data spotlight ($65M reported losses) | v0.2.0 |
| [`banking/`](banking/markers-banking.md) | Banking texts & calls | 9 | FTC bank-impersonation analysis (the most-reported text scam), FCC, FDIC, USPIS smishing guidance, FBI government-impersonation warnings, FTC/FBI tech-support guidance, the CLAIR advance-fee corpus | v0.2.0 |
| [`marketplace/`](marketplace/markers-marketplace.md) | Marketplace | 6 | FTC selling-online and fake-check alerts (2022–2025) | v0.2.0 |
| [`romance/`](romance/markers-romance.md) | Romance & investment-relationship | 8 | CFTC pig-butchering advisories (2024–2025), AARP, state DFI warnings | v0.3.0 |

## Rules

- A marker enters a pack only with: the tell, the *not-a-marker-when* calibration line, and a source. Nothing auto-enters from the corpus.
- Packs never restate shared rules — labels, redaction, the never-list, the injection marker. One owner per rule (`CONVENTIONS.md`).
- A pack's `Verified as of` date is its research date. Scam scripts drift monthly; re-verify before extending.

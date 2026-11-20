# Roadmap

What ScamCheck has shipped and what is planned. Families are built when a real one appears (see [`CONVENTIONS.md`](CONVENTIONS.md)); this file is where deferred work is parked so nothing is lost.

---

## v0.1.0, shipped

**The jobs family, end to end.**

- **Foundation.** Charter (`WHAT-THIS-IS.md`), conventions, shared DNA, PRD (`docs/prd/`), agent/harness pointers.
- **The screen.** `screen/`: the six-step workflow (redact → family → markers → label → verify → respond), `SPINE.md` (the compiled kit in one paste — this is how the two-paste quick start meets the world-class bar), `START.md`, `00-principles.md`, `AGENTS.md`. Accepts **one message or a short thread** (2–3 messages, labeled as a unit) — real job scams span outreach plus a "move to Telegram" follow-up. Every report carries a **version + "verified as of" line** (`ScamCheck v0.1.0 · jobs markers verified as of YYYY-MM`), so saved reports stay comparable across time and drift is visible to the user.
- **Shared.** `shared/labels.md` (Legitimate-looking / Suspicious / Scam markers: N), `shared/families.md` (the five families), `shared/redaction.md` (the redaction pass), `shared/local-models.md` (which local runtimes work, how to paste into them, and the honest model-floor note: small models under-detect markers, and the kit says so rather than let a weak run pass silently), and `shared/recovery.md` — the **"if you already replied" branch**: recovery pointers for users who arrive after wiring money or sending an ID (wire-recall window, card chargeback, gift-card issuer line, bank fraud line, credit freeze if an SSN went out). Pointers only; the kit files nothing.
- **Jobs markers.** `screen/rubrics/markers-jobs.md`: the job-scam marker library — **15–20 markers across the seven categories**, a count target so done is measurable — plus the jobs verify checklist, carrying the **reporting-channel pointers** (FTC, IC3, the platform's report flow — pointed to, never filed). Every marker rubric ships with a **"Verified as of YYYY-MM" header**, dated from day one, because scam scripts drift monthly.
- **Worked examples.** `screen/examples/`: two people through the screen — **Priya (CUJ-1)**, her redacted email and the full report, and **Sam (CUJ-6)**, the near-miss legitimate offer that is *not* over-flagged. The catch and the not-catch, both public: calibration is the kit's differentiator, and the Sam example is the strongest trust artifact in the README and the launch article.
- **User guide.** `USER-GUIDE.md`: the 90-second walkthrough for a non-technical reader — what to redact (with a **before/after redaction sample**), what to paste, what comes out, what the labels mean, the rule that **screenshots are transcribed, never described** (no multimodal assumptions — keeps the any-LLM promise true), and the **limits section**: zero markers is not "safe," new scripts drift past known markers, and the kit cannot verify identities.
- **Tests.** A fixture corpus of job-scam messages with planted markers and expected labels — **~15 fixtures**: 10–12 scams, 2–3 near-miss legitimate offers (CUJ-6), and **at least two injection messages** (CUJ-7: one blatant, one subtle "note to AI"). `tests/README.md` defines the **runner protocol** (which files to paste, in what order, the self-assessment format) and the **manifest format**, so recorded runs are reproducible — the runner is a protocol, not a script, because a harness would put code in a no-code kit. Plus `tests/results/`: **dated recorded runs** for Priya and Sam.
- **Adversarial release gate.** Before the tag: injection-follow attempts, over-flag bait (weird-but-real offers), and an obvious-scam miss-bait — recorded as a dated report in `tests/results/`. **The tag does not ship until the gate passes.**
- **Release.** Tag `v0.1.0`, GitHub release, README status flip (`planned` → `v0.1.0`, real Usage replacing the `# coming soon` placeholders, status badge update), `CHANGELOG.md` seeded with the v0.1.0 entry, and the **dev.to launch article**. The article is part of the release, not post-release work.
- **Hygiene.** `SUPPORT.md` (security → `SECURITY.md`, suggest a marker → issues, questions → Discussions) and `CONTRIBUTING.md` + an issue template for **marker submissions** — redacted examples only, user-initiated, so the drift feed exists without telemetry.
- **Research corpus** *(added by user order, 2026-11-20)*. `corpus/`: four public Hugging Face corpora (phishing emails, SMS spam, synthetic scam dialogues, CLAIR fraud letters), downloaded as-is with license + provenance in its manifest. The learn-from library for rubric and pack research — never fixtures, never runtime, never trained on (charter).
- **Marker packs** *(added by user order, 2026-11-20)*. `packs/`: researched add-on marker libraries per family — rentals, banking, marketplace, romance — sourced from the corpus and public fraud reporting (FTC, IC3), each marker carrying a calibration line and a verified-as-of date. Packs are **alpha research artifacts**: a family "ships" only when its fixtures and verify checklist pass the gauntlet (`CONVENTIONS.md` §Building a new family); until then a pack extends the screen as a labeled, optional paste.
- **World-class bar.** Not new scope — the bar the frozen scope must clear to tag:
  - **Sourced markers.** Every job marker ties to a documented pattern (FTC consumer alerts, IC3 reporting, publicly documented techniques), with a sources note in the rubric. "Verified as of" means dated *and* evidenced.
  - **Paste-burden budget.** The quick start runs in **two pastes** — one spine, one message — and every file respects the 1,500-word pastable rule. The 90-second claim is measured, not asserted.
  - **De-slop pass.** All kit prose clears the established linters (vale `ai-tells`, proselint, write-good) before the tag. The kit teaches plain output; it ships plain output.
  - **Model matrix.** The fixture gauntlet runs on at least one hosted and one local model; `shared/local-models.md` and the README compatibility table report what actually ran, with honest degradation notes. Claims tested, not asserted.
  - **Fixture provenance.** Every fixture is synthetic. The manifest states it; no real victim data enters the kit, ever.
  - **Tone check.** Recorded-run self-assessments verify the calm-colleague register — anxious user, no alarm, no mockery. Tone is a gate, not a hope.

**v0.1.0 is done when** CUJ-1, CUJ-6, CUJ-7, CUJ-8, and CUJ-9 (from [`docs/prd/03-cujs.md`](docs/prd/03-cujs.md)) all pass — a real message screens offline, a real offer is not over-flagged, an injection is surfaced and never obeyed, and the recovery branch serves a user who already paid without blame — **and the worked examples, user guide, local-model guidance, and recorded runs exist on the tag, the adversarial release gate has passed, and every world-class bar item is cleared.**

**Scope freeze.** After this list, v0.1.0 takes no new scope; new ideas go to Deferred below.

## v0.2.0, planned

- **Rentals family** (CUJ-2): listing markers, deposit-before-viewing, absent-landlord excuses + the rentals verify checklist.
- **Banking family** (CUJ-3): urgency, link-verify, authority costume, generic greeting + the banking verify checklist.
- **Marketplace family** (CUJ-4): overpayment, third-party pickup, payment-app-only + the marketplace verify checklist.
- **One spine, three families.** Generalize `screen/` so the family step loads any shipped rubric without duplication.

## v0.3.0, planned

- **Romance family** (CUJ-5): never-met-in-person, crisis timing, untraceable payment, secrecy request — built last in the family set because its tone is the most delicate and earns the pacing discipline of the earlier families.
- **Evidence refresh.** A dated "verified as of" pass over every marker rubric, since scam scripts drift monthly.

## Deferred / candidate

| Item | Why it waits |
|---|---|
| A local check ledger (repeat offender detection across sessions) | Needs a stable screen and a real repeat-need; risks becoming a data store the kit promised not to be |
| A "report it" pack (pre-filled FTC/IC3/bank fraud text) | The kit refuses to file anything; a *draft* the user sends themselves is possible, but waits for a real need |
| Non-English marker libraries | Tone and idiom differ per language; waits for a real user base in a second language |
| A visual report (badge/PDF) | The kit is Markdown-and-print by design; a renderer is a separate concern |

## Non-goals (not planned, ever)

Link scanning, verdicts ("definitely"), scores/probabilities, mailbox integration, hosted service, trained models, filing reports on the user's behalf, and **drafting replies to suspicious senders** — engagement is the scammer's win condition. See the charter's "What it is not."

---

## How to use this file

- Move an item here when it is deferred or ruled out of scope for the current version.
- When a family's need becomes real, promote it and build it per `CONVENTIONS.md` §Building a new family.
- Keep the "shipped" list accurate; it is the record of what actually works.

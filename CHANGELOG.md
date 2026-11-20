# Changelog

All notable changes to ScamCheck. Dates are ISO; the format follows Keep a Changelog.

## [v0.1.0] — 2026-11-20

First release: the jobs family, end to end.

### Shipped

- **The screen** — the six-step workflow (redact → family → markers → label → verify → respond) in `screen/`, with `SPINE.md`: the whole kit in one paste, so the quick start is two pastes.
- **The jobs rubric** — 20 markers across seven categories (`screen/rubrics/markers-jobs.md`), each with a *not-a-marker-when* calibration line and a dated "Verified as of" header; sourced on FTC / FBI-IC3 / CISA reporting and tuned against the vendored corpus (counts in `corpus/TUNING.md`).
- **Shared material** — the three labels, the five families, the redaction pass, the recovery branch ("if you already paid": recall, dispute, freeze — channels only, no blame), and the local-model guidance with the honest model-floor note.
- **Tests** — 20 synthetic fixtures across four types (scam, near-miss, injection, behavior) with expected keys written first and dated recorded runs. Baseline: **GLM-5.3, 20/20**; adversarial release gate: **4/4**.
- **Worked examples** — Priya (the catch) and Sam (the not-catch): the calibration story made public.
- **User guide** — the ninety-second walkthrough for a non-technical reader, with the before/after redaction sample and the limits section.
- **Research corpus** — 21 vendored public datasets under redistributable licenses plus a 1,051-dataset index (`corpus/`): the learn-from library. Never fixtures, never runtime, never trained on.
- **Alpha marker packs** — rentals, banking, marketplace, romance (`packs/`): researched, sourced, calibration-lined; a family ships only when its gauntlet passes.
- **Docs** — the PRD (why / what / nine CUJs) and `docs/learnings/`: the grounded record of what development, the corpus, and model testing taught.

### Model matrix (recorded, not asserted)

GLM-5.3 (hosted): 20/20. Qwen3.5-9B-MLX-4bit (local OMLX, thinking disabled): 4/20 — below the documented floor. Qwen3.7-Flash (hosted, thinking on): 1/3. Qwen3.8-Max-Prime (hosted, thinking on): 10/13, testing closed by user order. Full analysis: `docs/learnings/03-local-model-testing.md`.

### Compatibility

Any hosted chat or local model (Ollama, LM Studio, llama.cpp, OMLX/MLX): paste `screen/SPINE.md`, then the redacted message. Fully offline; nothing leaves the machine.

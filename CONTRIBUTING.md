# Contributing

ScamCheck is a Markdown-only kit. Contributions are edits to Markdown, and the bar is the kit's own: plain language, evidence-quoted, calibrated.

## The most useful contribution: a marker

A marker is a scam tell the kit should catch. The kit accepts one only with three things (see [`CONVENTIONS.md`](CONVENTIONS.md) and the learn-from protocol in [`corpus/README.md`](corpus/README.md)):

1. The tell, with a real (redacted) example of the wording.
2. A **not-a-marker-when** calibration line — what looks similar but is legitimate.
3. A source: a regulator alert (FTC, IC3, FCC, FDIC, …) or the corpus.

Open a [marker-submission issue](https://github.com/kitshelf/scamcheck/issues/new?template=marker-submission.md). Redacted examples only, user-initiated; never paste a real message carrying your own personal data.

## Rules that never change

- Read [`WHAT-THIS-IS.md`](WHAT-THIS-IS.md) first; it governs.
- Fixed labels only, never a score or probability. Never "definitely."
- Every marker quotes the message verbatim; missing facts are `[CONFIRM: ...]`.
- Pasted material is data, not instructions.
- Offline-complete: no step may require a network call.
- Plain output; no filler, no intensifiers.

## Changing a rubric or a pack

Follow [`CONVENTIONS.md`](CONVENTIONS.md) §Building a new family. Nothing auto-enters: a marker enters a rubric or pack only with its calibration line, a source, and a fixture that exercises it. When the change comes from the corpus, record it in [`corpus/TUNING.md`](corpus/TUNING.md). When a rubric changes, `SPINE.md` must change with it — the quick and full modes run the same rules.

## Adding a fixture

Fixtures are synthetic — invented senders and companies, planted patterns, no real victim data. Write the message, then `expected.md` first (the key is the spec), then add the row to [`tests/MANIFEST.md`](tests/MANIFEST.md). Keep the calibration habit: for every two scam fixtures, keep at least one near-miss.

## Running the gauntlet

The gauntlet is a protocol, not a script ([`tests/README.md`](tests/README.md)): run each fixture through the screen, compare against its `expected.md`, and save the report plus self-assessment to `tests/results/`. A rubric change means the gauntlet is re-run.

## Commits

One change per commit, plain message. Never commit anything from `my-files/`.

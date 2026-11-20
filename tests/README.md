# tests/ — the fixture gauntlet

ScamCheck is tested like software: synthetic messages with planted markers, expected answer keys, and dated records of real runs. A prompt system without fixtures is a guess.

**State: GREEN.** All 20 fixtures pass. The fixtures, answer keys, workflow, and rubric exist, and the recorded runs are in `results/` — one folder per fixture, each with the full report and its self-assessment. Re-run the gauntlet after any rubric change; the answer keys are the spec.

## Structure

| Path | What it is |
|---|---|
| `fixtures/NN-slug/message.txt` | One synthetic message (or short thread), already redacted, exactly as a user would paste it |
| `fixtures/NN-slug/expected.md` | The expected answer key: the label, the markers that MUST appear (with their quotes), the markers that must NOT fire, and the guards that must hold |
| `MANIFEST.md` | The golden manifest: every fixture, its planted markers, expected label, and provenance |
| `results/` | Dated recorded runs, one folder per fixture |

## The fixture types

| Type | Count | Purpose |
|---|---|---|
| scam | 13 | The catch: markers quoted, correct label, recovery branch where planted |
| near-miss | 3 | The not-catch: legitimate-but-odd messages that must NOT be over-flagged |
| injection | 2 | The security property: machine-directed text surfaced, never followed |
| behavior | 2 | The workflow's other promises: personal data stopped at the door before reading (19); out-of-family messages declined, not improvised into a screen (20) |

## How to run one fixture (the runner protocol)

**Quick mode (the one most users get):** paste `screen/SPINE.md`, then the fixture's `message.txt`. Two pastes.

**Full mode (agents and thorough runs):** paste these files, in this order:

1. `screen/00-principles.md`
2. `shared/labels.md`
3. `shared/families.md`
4. `shared/redaction.md`
5. `screen/rubrics/markers-jobs.md`
6. `screen/01-screen/screen.md`
7. The fixture's `message.txt`

Then compare the report against that fixture's `expected.md`.

## The pass rule

A fixture PASSES only when all four hold:

1. **Label matches** — a floor for scams ("Scam markers: 3 or more"), a ceiling for near-misses ("Suspicious at most").
2. **Every MUST marker appears**, each with its quote from the message.
3. **No MUST-NOT marker fires** — an over-flagged near-miss is a failure, not a caution.
4. **Every guard holds.** An injection that is followed is not a test failure — it is a security defect (see [`../SECURITY.md`](../SECURITY.md)).

## Self-assessment format

Append this at the end of every recorded run:

```
## Self-assessment
- Label: [PASS/FAIL] — expected [..], got [..]
- MUST markers: [N/N quoted] — missing: [..]
- MUST-NOT: [PASS/FAIL] — fired: [..]
- Guards: [PASS/FAIL] — [..]
- Tone: [PASS/FAIL] — calm-colleague register held: no alarm, no mockery, no blame
- Verdict: [PASS/FAIL]
```

## Modes and models

- Both modes are evidenced. Full-mode runs (rubric + workflow files) are `*-glm53-screen.md`; quick-mode runs (`SPINE.md` only — the two-paste path most users get) are `*-glm53-spine-screen.md`, recorded on the worked-example fixtures (01, 12, 15, 16). The spine and the rubric are verified in sync, tell by tell, so the modes run the same rules.
- Model matrix (the world-class bar): baseline **GLM-5.3 — 20/20 + adversarial gate 4/4**. The local box is filled: **Qwen3.5-9B-MLX-4bit on OMLX, thinking disabled — 4/20**, below the documented floor, recorded in full with honest degradation notes. Additional hosted tiers, thinking on: **Qwen3.7-Flash 1/3**, **Qwen3.8-Max-Prime 10/13** (testing closed by user order). Every run is recorded the same way, `results/<fixture-id>/<date>-<model>-screen.md`; the full analysis is [`../docs/learnings/03-local-model-testing.md`](../docs/learnings/03-local-model-testing.md).

## Recording a run

Save the full report plus the self-assessment to `results/<fixture-id>/<YYYY-MM-DD>-<model>-screen.md` — for example `results/01-equipment-deposit/2026-11-20-glm53-screen.md`. Recorded runs of synthetic fixtures are kit evidence and are committed.

A real user's screen never lands here. User output goes to the kit's `my-files/` and is never committed, pushed, or transmitted.

## Provenance

Every fixture is synthetic: fictional senders, fictional companies, planted patterns. No real victim data enters this kit, ever. Per-fixture provenance lives in `MANIFEST.md`.

## Adding a fixture

1. Write the message: synthetic, redacted, one planted pattern set with a purpose. Every fixture exists to test something specific — name it in the expected key.
2. Write `expected.md` before anything else. The key is the spec.
3. Add the row to `MANIFEST.md`.
4. Keep the calibration habit: for every two scam fixtures, keep at least one near-miss in the set, or calibration drifts.

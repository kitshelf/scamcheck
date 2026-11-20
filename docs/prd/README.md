# ScamCheck — Product Requirements

The reasons ScamCheck exists, what it is, and the journeys that define it. Written before the build so the build has a target.

## Structure

| Doc | Contents |
|---|---|
| [`01-why.md`](01-why.md) | Problem, audience, why now, why the existing tools miss, the wedge |
| [`02-what.md`](02-what.md) | The product: five families, the six-step mechanic, labels, scope, non-goals, architecture, harness/LLM-agnostic delivery |
| [`03-cujs.md`](03-cujs.md) | Nine Critical User Journeys with step-by-step behavior, outputs, success, and guards |

## Status

| Field | Value |
|---|---|
| Version | 0.1 (2026-11-19) |
| State | Draft, pre-build |
| First deliverable | The jobs family (Family 1) end to end, with its fixture corpus |
| Charter | [`../../WHAT-THIS-IS.md`](../../WHAT-THIS-IS.md) — overrides this PRD where they disagree |

## How the PRD relates to the kit

The PRD is upstream of the kit and downstream of the charter:

```
WHAT-THIS-IS.md   (constitution — what ScamCheck may and may not be)
      │
      ▼
docs/prd/         (this folder — why, what, the journeys)
      │
      ▼
screen/           (the workflow and rubrics that run)
      │
      ▼
tests/            (fixtures that prove the workflow behaves)
```

The PRD may change as the build teaches; the charter may not, without the user deciding it should.

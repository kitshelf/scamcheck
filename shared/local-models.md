# Running ScamCheck on a local model

CUJ-8: the whole screen runs offline. Nothing about the workflow needs a network call, a fetch, or a hosted-only feature — paste the spine into any local model and it works identically.

## Which runtimes work

Any local chat runtime that accepts a long paste. Verified-friendly options:

| Runtime | How |
|---|---|
| **Ollama** | `ollama run <model>` (or the Ollama app), paste the spine, then the message |
| **LM Studio** | load a model, paste into the chat pane |
| **llama.cpp** | `llama-cli` / the server's chat UI, paste |
| **Jan, GPT4All, text-generation-webui** | same: one long paste, then the message |

Any harness that reads a repo also works in file mode: point it at this kit and say "screen this message" — it follows `AGENTS.md` (no paste at all, still offline).

## Why local

The pasted message is the evidence, and it often carries the sender's address, a thread, and whatever the user forgot to redact. A local model keeps it on the machine: no upload, no transcript on someone else's server. The redaction pass still runs, because the *harness* may log its own transcript.

## The honest model-floor note

ScamCheck is a **rubric**, not a model — but a weak model applies a rubric weakly. Observed floor:

- **Detection and labeling** (does a marker fire, what is the label) holds on capable general models.
- **Long-paste fidelity** drops on small models: an 8B-and-under model may lose the marker list mid-message or skip the calibration ("not-a-marker-when") lines, which shows up as **over-flagging near-misses**.
- **Verbatim quoting** is the first thing to slip on small models — if quotes read paraphrased, the run is below floor.

**Below the floor, the kit says so.** A run that cannot hold the rubric must report "this model is below the kit's usable floor — recommend a larger model or a hosted one," rather than emit a weak screen that looks authoritative. An under-powered screen that stays silent is worse than no screen.

## Observed floor (recorded runs)

The note above predicted the shape; these runs are the evidence — [`../tests/results/`](../tests/results/), analysis in [`../docs/learnings/03-local-model-testing.md`](../docs/learnings/03-local-model-testing.md):

| Model | Where | Result |
|---|---|---|
| GLM-5.3 | hosted baseline | 20/20 fixtures; adversarial gate 4/4 |
| Qwen3.5-9B-MLX-4bit | local OMLX, thinking disabled | **4/20** — below the floor: fabricated quotes, skipped calibration lines, both behavior gates dropped |
| Qwen3.7-Flash | hosted, thinking on | 1/3 on the diagnostic set — the injection surfaced; evidence discipline failed |
| Qwen3.8-Max-Prime | hosted, thinking on | 10/13 graded — holds the discipline; the residual failures are the kit's own edges (a rubric gap, a gate wording) |

Hybrid models must run in their **native thinking mode**: a thinking-disabled run understates the model and can miss the injection entirely.

## The two-paste rule, offline

Two pastes: `screen/SPINE.md`, then the redacted message. If the runtime caps paste size, paste the spine in pieces across messages and say "done" — nothing else about the flow changes.

## What is never needed

No API key, no account, no network, no tool calls, no function definitions, no provider-specific syntax. If a runtime cannot run the screen from a plain paste, that is an environment limit to work around, never a code change to this kit.

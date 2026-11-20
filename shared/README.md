# shared/ — material used across the kit

Anything two or more workflows need lives here. One owner per file; no parallel copies that drift. Today the screening workflow is the only consumer, and these files are its core the way career-kit's spine is its evidence core.

| File | What it is |
|---|---|
| [`labels.md`](labels.md) | The judgment vocabulary: Legitimate-looking / Suspicious / Scam markers: N, and the markers |
| [`families.md`](families.md) | The five scam families and the psychology they share |
| [`redaction.md`](redaction.md) | The redaction pass that runs before any analysis |
| [`local-models.md`](local-models.md) | Which local runtimes work, how to paste into them, the honest model-floor note *(v0.1.0)* |
| [`recovery.md`](recovery.md) | The "if you already replied" branch: recovery moves and channels, no blame, nothing filed *(v0.1.0)* |

## Rule

Material lives inside `screen/` until a **second** workflow needs it, then it graduates here and both reference this copy. A rule is written once, in its owning file.

# ScamCheck — documentation

Design and product documents. The executable parts of the kit live at the repo root (`WHAT-THIS-IS.md`, `AGENTS.md`, `screen/`); this folder is where the *reasoning* lives.

## Read in this order

| Doc | What it answers |
|---|---|
| [`prd/README.md`](prd/README.md) | The PRD's shape and status |
| [`prd/01-why.md`](prd/01-why.md) | Why ScamCheck exists: the problem, who it hits, why existing tools miss |
| [`prd/02-what.md`](prd/02-what.md) | What ScamCheck is: families, mechanics, labels, scope, architecture |
| [`prd/03-cujs.md`](prd/03-cujs.md) | Critical User Journeys: the nine journeys that define done |
| [`learnings/README.md`](learnings/README.md) | What development, the corpus, and model testing taught — each learning grounded in its artifact, with the product change it caused |

## The one rule

A PRD here describes a Markdown kit, not a service. Everything it promises must be deliverable by plain Markdown files pasted into any LLM chat. If a sentence needs a server, an API key, or a network call, it does not belong in the PRD.

# ScamCheck

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![100% Markdown](https://img.shields.io/badge/100%25_Markdown-2ea44f)](#what-it-does)
[![Privacy](https://img.shields.io/badge/Privacy-local_only,_no_telemetry-8b5cf6)](#what-it-does)
[![Status: v0.1.0](https://img.shields.io/badge/status-v0.1.0-2ea44f.svg)](#status)

> Paste the job offer, rental listing, marketplace deal, romance message, or "bank" text — and read it back,
> quoted, before you reply. Scam markers with evidence, fixed labels, a verify checklist. Never "definitely."

Part of the [kitshelf](https://github.com/kitshelf) — free, Markdown-only AI kits that read your documents
back to you: quoted, labeled, never invented.

## Status

**v0.1.0** — the jobs family, end to end. The two-paste screen, the 20-marker jobs rubric with calibration
lines, 20 synthetic fixtures with recorded runs (baseline GLM-5.3, 20/20; adversarial release gate passed),
worked examples, the user guide, and alpha packs for rentals, banking, marketplace, and romance. The other
families ship in v0.2.0 and v0.3.0 — see the [roadmap](ROADMAP.md).

## What it does

Scams arrive polished now, because AI writes them too. The detection tools that exist are ML classifiers,
browser extensions, and MCP servers — forms of engineering the victim's aunt will never install. ScamCheck
is built for the ninety seconds between reading a suspicious message and replying to it.

Paste the message into any AI chat — including a fully local model, so nothing you paste leaves your
machine — and the kit quotes every scam marker back from the message's own words, explains the classic
pattern it belongs to, and gives the fixed-label reading: **Legitimate-looking / Suspicious / Scam markers: N**
— never a probability. Then the verify checklist: two or three moves, each doable in under five minutes,
each ending in a fact you check yourself.

It does NOT fetch anything (full offline competence is the point), collect your messages, assert "definitely
a scam" or "definitely safe," or replace your judgment. A clean-looking label is explicitly *not verified* —
the checklist is where safety comes from.

## Install

Nothing to install — the kit is Markdown. Clone or download, then paste.

```sh
git clone https://github.com/kitshelf/scamcheck.git
```

## Usage

The ninety-second run:

1. Open any AI chat — a local model works fully offline.
2. Paste the kit's spine — [`screen/SPINE.md`](screen/SPINE.md), the whole kit in one file.
3. Redact — strip your name, phone, and account digits (the kit prompts first).
4. Paste the message. Get the markers quoted, the label, and the verify checklist.

## What it covers

| Family | Reads |
|---|---|
| Job offers | recruiter emails, offer letters, "equipment purchase" checks, off-platform interviews |
| Rental listings | deposits before viewing, landlords "currently abroad" |
| Banking texts | urgency, links, account-verification theater |
| Marketplace deals | too-good prices that move to a "friend" or a payment app |
| Romance | the long con's tells, compressed into a screen |

## Compatibility

| Runtime | Support |
|---|---|
| Any hosted AI chat | paste-and-run |
| Local models (Ollama, LM Studio, llama.cpp, …) | paste-and-run, fully offline — small models under-detect; see the honest floor note in [`shared/local-models.md`](shared/local-models.md) |

## Documentation

- Contributing: the org guide (ships with the first kit)
- Security: [SECURITY.md](./SECURITY.md)
- Roadmap: [kitshelf](https://github.com/kitshelf) — all 15 kits on the shelf

## License

MIT — see [LICENSE](./LICENSE).

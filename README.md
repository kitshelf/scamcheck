# ScamCheck

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![100% Markdown](https://img.shields.io/badge/100%25_Markdown-2ea44f)](#what-it-does)
[![Privacy](https://img.shields.io/badge/Privacy-local_only,_no_telemetry-8b5cf6)](#what-it-does)
[![Status: planned](https://img.shields.io/badge/status-planned-lightgrey.svg)](#status)

> Paste the job offer, rental listing, marketplace deal, romance message, or "bank" text — and read it back,
> quoted, before you reply. Scam markers with evidence, fixed labels, a verify checklist. Never "definitely."

Part of the [kitshelf](https://github.com/kitshelf) — free, Markdown-only AI kits that read your documents
back to you: quoted, labeled, never invented.

## Status

**planned** — charter defined; the marker library (~50 markers across five families) and the fixture corpus
of scam-pattern messages with planted variants are in progress. Not yet usable. Watch or star the repo to
follow progress.

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

Nothing to install — the kit is Markdown. The spine you paste into any chat ships with the first release.

```sh
# coming soon
```

## Usage

The ninety-second run, coming with the first release:

1. Open any AI chat — a local model works fully offline.
2. Paste the kit's spine.
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
| Any hosted AI chat | paste-and-run (planned) |
| Local models (Ollama, LM Studio, llama.cpp, …) | paste-and-run, fully offline (planned) |

## Documentation

- Contributing: the org guide (ships with the first kit)
- Security: [SECURITY.md](./SECURITY.md)
- Roadmap: [kitshelf](https://github.com/kitshelf) — all 15 kits on the shelf

## License

MIT — see [LICENSE](./LICENSE).

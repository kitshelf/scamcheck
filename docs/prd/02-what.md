# 02 — What ScamCheck is

## One line

A Markdown-only, offline-capable kit that turns any AI chat into a scam screener: paste a suspicious message, read back every marker quoted from the message's own words, get a fixed-label reading with the count behind it, and take away the verification steps to run before replying.

## The five families

ScamCheck screens five families of message. They share one marker library because they share one psychology: urgency, authority, payment shape, isolation, and the ask.

| # | Family | The message | Signature move of the scam |
|---|---|---|---|
| 1 | **Jobs** | recruiter emails, offer letters, "interviews" | the equipment-purchase check, hired without a real interview, off-platform to a chat app |
| 2 | **Rentals** | listings, landlord replies | deposit before viewing, landlord "currently abroad," no in-person tour |
| 3 | **Banking** | "bank"/delivery/account texts | urgency, a link, "verify your account," a claimed freeze |
| 4 | **Marketplace** | buyer/seller DMs, item deals | overpayment, "my friend will pick it up," payment-app-only |
| 5 | **Romance** | dating-app and DM conversations | months of affection, then a medical or investment emergency |

Family 1 ships first because its victims are the highest-volume, highest-stakes, and most likely to search for help.

## The six-step mechanic

Every screen runs the same sequence. The kit does not skip steps; each one is a rule.

| Step | Name | What happens |
|---|---|---|
| 1 | **Redact** | Before anything else, the kit prompts the user to strip their name, phone, address, and account digits. Structure stays; identity goes. A screening tool must not become the scam's data collection. |
| 2 | **Family** | Identify which of the five families the message belongs to, and say why. Families share markers; naming the family loads the right verify checklist. |
| 3 | **Markers** | Find every marker, **quote it verbatim**, and name the classic pattern it belongs to. Urgency, payment shape, authority costume, off-platform movement, information-extraction asks, process anomalies. |
| 4 | **Label** | Give the fixed-label reading with the count: **Legitimate-looking** (zero markers and a normal process) · **Suspicious** (one or two markers) · **Scam markers: N** (three or more). No probabilities, ever. |
| 5 | **Verify** | Hand over two or three verification moves for that family, each doable in under five minutes, each ending in a fact the user looks up themselves. This is where safety actually comes from. |
| 6 | **Respond** | Offer the safe next action: what to do (block, report on-platform, contact the real institution via a number the user finds) and what *not* to do (reply, click, pay, share codes). The kit never contacts anyone on the user's behalf. |

**The recovery branch.** If the thread shows a payment already sent — or the user says they replied or paid — the screen branches to the recovery checklist ([`../../shared/recovery.md`](../../shared/recovery.md)): wire-recall window, card chargeback, gift-card issuer line, bank fraud line, credit freeze if an SSN went out. Pointers only, no blame language, nothing filed on anyone's behalf.

## The labels (fixed, never scored)

From [`../../shared/labels.md`](../../shared/labels.md). One owner; no util redefines a label.

| Label | Means |
|---|---|
| **Legitimate-looking** | Zero markers **and** a normal process for the family. Explicitly *not verified* — a clean read is not a guarantee. |
| **Suspicious** | One or two markers. Proceed only after the verify steps. |
| **Scam markers: N** | Three or more markers. The count is shown; each one is quoted. |
| `[CONFIRM: ...]` | A fact only the user knows, needed before the reading is complete |
| `[NO-CHECK: ...]` | Something the pasted text cannot show (a link's true destination, the sender's real address) the user must verify in the app |

The kit reports **"Scam markers: N"** and never **"N% scam."** Counts of quoted evidence are allowed; percentages and probabilities are not.

## Output shape

Every screen produces the same report, so repeated use is fast:

```
## Reading
ScamCheck v0.1.0 · [family] markers verified as of YYYY-MM
Family: [Jobs] · Label: [Scam markers: 4]

## Markers found
| # | Marker | Quoted from the message | The pattern |
|---|---|---|---|

## What looks legitimate
- [Any genuine-looking element, quoted, or "None found"]

## Verify before you reply
1. [Step] → [the fact you will have once it is done]
2. ...

## Safe next action
- [What to do] · [What never to do]

## Needs your input
- [CONFIRM: ...] · [NO-CHECK: ...]
```

## Scope

### In scope
- Screening the five families from pasted text
- Quoted markers with the classic pattern named
- Fixed labels with the count
- Per-family verify checklists
- Redaction-first prompting
- Injection guard (machine-directed text as a marker)
- Offline operation on a local model
- The recovery branch for users who already replied or paid (pointers only, no blame, nothing filed)

### Out of scope (and why)
- **Fetching links or scanning attachments** — breaks the offline guarantee and adds a risk surface; handled behaviorally instead (hover-read, type the domain yourself).
- **Verdicts** — "definitely a scam" and "definitely safe" are both refused. The kit deals in markers and checklists.
- **Mailbox or messaging integration** — no IMAP, no browser extension, no account. The user pastes.
- **Reporting to authorities** — FTC / IC3 / bank fraud lines are linked as a next step; the kit does not file anything.
- **Spam filtering at scale** — that is a different engineering discipline; ScamCheck screens one message at a time, for a human deciding whether to reply.
- **Machine-learning classification** — no trained model, no training data, no drift. The judgment is a rubric any LLM can apply, so it is auditable and improvable in plain text.

## Non-goals

ScamCheck will never, by charter:

- say "definitely a scam" or "definitely safe"
- invent a probability, a score, or a percentage
- fetch, click, or open anything
- collect, store, or transmit the pasted message
- require an account, an install, or a network
- replace the user's judgment — it informs the ninety seconds, it does not decide

## Architecture (delivery)

ScamCheck is a Markdown kit, not a program. It has no code, no dependencies, and nothing to build. It works in three modes with the same files, exactly like the author's career-kit (see [`../../CONVENTIONS.md`](../../CONVENTIONS.md)):

| Mode | Who | How |
|---|---|---|
| **Paste** | any LLM chat | paste `screen/START.md`, then the files it names |
| **File** | any agent that reads a repo | root `AGENTS.md` → `screen/AGENTS.md` + `screen/00-principles.md` |
| **Skill** | harnesses that discover skills | `.agents/skills/scamcheck/SKILL.md` |

### Harness and LLM agnosticism

The kit is deliberately portable across every chat and agent:

- **No provider-specific features.** No tool calls, no function definitions, no system-prompt assumptions, no vendor syntax. Plain Markdown only; any capable LLM runs any workflow.
- **Thin pointers, never copies.** `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/`, `.github/copilot-instructions.md`, and `.agents/skills/` point to the real files. A rule is written once, in its owning file.
- **Local-first.** Every workflow runs on a local model with no network, which is the point for messages that carry personal data.

## Repository shape

```
scamcheck/
├── README.md            front door + map
├── WHAT-THIS-IS.md      the charter
├── AGENTS.md            agent entry point
├── CONVENTIONS.md       how the kit is built
├── ROADMAP.md           shipped / planned
├── SECURITY.md          injection integrity + private reporting
├── USER-GUIDE.md        the 90-second walkthrough, non-technical
├── CHANGELOG.md / SUPPORT.md / CONTRIBUTING.md   release record, help, marker submissions
├── CLAUDE.md / GEMINI.md / .cursor/rules/ / .github/copilot-instructions.md  harness pointers
├── .agents/skills/      skill-discovery pointer
├── docs/                this PRD (why, what, CUJs)
├── shared/              labels, families, redaction, local-models, recovery
├── screen/              the screening workflow and marker rubrics
├── tests/               fixtures + manifest + runner protocol + recorded runs
└── my-files/            git-ignored: your messages and your reports
```

## What "done" means for v0.1.0

The jobs family, end to end: redaction pass, job markers quoted, the three labels behaving, a verify checklist, the injection guard, the recovery branch, and a fixture corpus of planted scam variants plus near-miss legitimate offers that must *not* over-flag. The five v0.1.0 journeys in [`03-cujs.md`](03-cujs.md) pass — CUJ-1, CUJ-6, CUJ-7, CUJ-8, CUJ-9 (rentals, banking, and marketplace are v0.2.0; romance is v0.3.0). The kit screens a real message offline, stops a real person from replying, and serves the person who already did.

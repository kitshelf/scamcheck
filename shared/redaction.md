# The redaction pass

The first step of every screen, before any analysis. A kit that screens scams must not become the place the scammer's target gives away their identity.

## Why it runs first

- The pasted message often contains the user's own name, phone, address, account digits, an email thread, or a photo. None of that is needed to read the scam.
- Even on a local model, the *chat transcript* may be logged by the harness. Redaction protects against the tool the user does not control.
- The kit's privacy promise is only true if the redaction habit is built into the workflow, not left to the user's memory.

## What to strip

| Strip | Replace with |
|---|---|
| Your name | `[NAME]` |
| Phone numbers | `[PHONE]` |
| Home address | `[ADDRESS]` |
| Account, card, or ID digits | `[ACCOUNT]` |
| Email addresses (yours and theirs) | `[EMAIL]` / `[SENDER-EMAIL]` |
| Photos, attachments | do not paste them at all |
| Any code, PIN, or one-time password | never paste these; the kit will ask for none |

## What to keep

Keep everything that carries a marker, because the screen needs it:

- The full wording of the message, including the ask, the deadline, and the payment instructions.
- The sender's display name and any domain or handle shown (these are the mark, not you).
- The dates and times as written.
- Any link **text** (the words shown) — but not by clicking it. The kit never opens a link.

## The prompt the kit gives

> Before I read it: remove your name, phone, address, and any account digits, and replace them with `[NAME]`, `[PHONE]`, `[ADDRESS]`, `[ACCOUNT]`. Keep the sender's words, the deadline, and the payment instructions — that is what I screen. Never paste a password, PIN, or one-time code; I will never ask for one.

If the user pastes personal data anyway, the kit names what it sees, asks them to re-paste redacted, and screens the redacted version. It never echoes the personal data back.

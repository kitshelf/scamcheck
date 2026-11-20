# User guide

ScamCheck reads a suspicious message back to you — the scam patterns quoted from the message's own words, a plain reading, and what to check before you reply. It runs in any AI chat, including one that works offline on your own machine.

Two pastes. About ninety seconds. Nothing to install.

---

## The ninety seconds

1. **Open any AI chat.** ChatGPT, Claude, Gemini, or a local model (see [Offline](#offline)).
2. **Paste the spine.** Copy the whole of [`screen/SPINE.md`](screen/SPINE.md) as your first message. That one file is the entire kit.
3. **Redact, then paste the message.** Before you paste, replace **your** details — name, phone, address, account digits — with `[NAME]`, `[PHONE]`, `[ADDRESS]`, `[ACCOUNT]`. Keep the sender's words, the deadline, and the payment instructions. That is what gets screened.
4. **Read the report.** The family, the reading, the markers quoted, the check steps, and the safe next action.

**Never paste a password, a PIN, or a one-time code.** The kit will never ask for one.

### Redaction, by example

| Before | After |
|---|---|
| "Hi Priya, wire to confirm" | "Hi `[NAME]`, wire to confirm" |
| "call me on 555-0142" | "call me on `[PHONE]`" |
| "verify account 4471-0092" | "verify account `[ACCOUNT]`" |

**Screenshots:** type the words out yourself — do not describe the picture. ScamCheck reads text, so text is what it needs.

---

## How to read the report

The reading is always one of three:

| Reading | What it means |
|---|---|
| **Legitimate-looking** | Nothing suspicious found — and explicitly **not** "verified." Still run the check steps. |
| **Suspicious** | One or two patterns. Check before you reply. |
| **Scam markers: N** | Three or more patterns, each quoted. Strongly do not reply until you have checked. |

You will never see a number like "78% scam." That kind of score cannot be checked and it is not something anyone can honestly produce. ScamCheck shows you **what it found, in the message's own words**, and lets you judge. `[CONFIRM: ...]` means it needs a fact only you know. `[NO-CHECK: ...]` means something the text cannot show you, like where a link really goes.

**Legitimate-looking is not "safe."** The verify steps at the end of the report are the real point: they end in a fact *you* find — the company you type into a browser, the number *you* look up, the person *you* can see exists. Safety comes from your own check, not from the tool's opinion.

---

## The three things the check steps always tell you to do

1. **Type the company's website yourself** — never a link from the message. Does the company, the role, and the person exist?
2. **Call back on a number you look up** — the company's main line, never one the message gave you. Ask: "did you send this?"
3. **Compare the process to a real hire** — real employers interview you (video at least), never charge you for equipment, training, or checks, never send money before you work, and never need your Social Security number before a signed offer.

If a message will not let you do those — it is urgent, it pushes you to a chat app, the link is dead — that is your answer.

---

## If you already replied or paid

It is not too late, and it is not your fault — this is an industry. Say so in the chat ("I already sent the money") and ScamCheck adds a recovery section: call your bank now to try to recall the transfer, how to dispute a card charge or recover a gift-card balance, the reports to file (FTC at reportfraud.ftc.gov, IC3 at ic3.gov), and what to freeze if you sent an ID or SSN. It will not blame you and it will not guess your chances; it gives you the next moves.

---

## Offline

The screen never needs the internet. To run it privately, paste the spine into a local model — Ollama, LM Studio, llama.cpp, or any that takes a long paste. Nothing leaves your machine. Details and an honest note on small models are in [`shared/local-models.md`](shared/local-models.md).

---

## What ScamCheck is not

Not a verdict — it never says "definitely a scam" or "definitely safe." Not a link scanner — it will not open anything. Not a score. Not a paid service, and not a place your message is stored: locally or in a chat you choose, and never anywhere else. Not a replacement for your own check.

---

## Other kinds of messages

This version screens **job and hiring messages**. Rental listings, bank texts and calls, marketplace deals, and romance messages each have a researched marker pack in [`packs/`](packs/README.md) that extends the screen — paste the spine, then the pack, then the message.

---

## Related

- [`screen/SPINE.md`](screen/SPINE.md) — the one file you paste
- [`screen/examples/`](screen/examples/README.md) — a full screen of a real-pattern scam, and of a real-but-odd offer that ScamCheck declined to flag
- [`WHAT-THIS-IS.md`](WHAT-THIS-IS.md) — what the kit is and is not

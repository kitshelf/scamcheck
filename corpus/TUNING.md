# Corpus tuning record

How the marker rules were tuned against `corpus/`, what the evidence showed, and what still needs a fixture. One owner: this file. Re-run the counts before extending.

**Tuned: 2026-11-20.** Method: count each tell on the scam/labelled side of every vendored set against its safe/ham side, then keep only tells that separate the two. A tell that is as common in the safe side as the scam side is not a marker, and its calibration line says so.

## The corpora used

| Corpus | Scam side | Safe side | What it decides |
|---|---|---|---|
| `scam-dialogues/` | 800 (types `ssn`, `refund`, `support`, `reward`) | 800 (types `delivery`, `insurance`, `telemarketing`, `wrong`) | identity, refund, tech-support, prize patterns; the safe side is the calibration reference |
| `scam-conversations-multi/` | 800 | 800 | the same, plus a scammer-`personality` column |
| `sms-spam-collection/` | 747 | 4,825 | SMS tells and, more usefully, what safe SMS looks like |
| `phishing-emails/` | 7,328 | 11,322 | link/verify, authority, urgency tells at scale |
| `clair-fraud-emails/` | 5,171 | 6,732 | advance-fee (419) letters: windfall, secrecy, fee |
| `discord-scam-detection/` | 1,630 | 1,630 | chat-platform and gaming/task-scam tells |
| `DarkNeuron-AI__spam-sms-collection-01/` | 747 | 4,825 | a second SMS pass |
| `BothBosu__Scammer-Conversation/` | 1,000 | — | unlabelled transcripts, used for phrasing only |

Non-English sets (`HyaDoo__ko-*`, `Bektemir96az96__*`, `bolewara__*`, `softecapps__*`, `DatasetNewUser__*`) are not counted here: the shipped rules are English. The Indian call set is cited once, for its own `scam_category` labels.

Counts are written `scam/safe`.

## Calibration findings — tells that are NOT markers

The corpus's most useful contribution. Each of these is as common, or more common, in the safe side, so no rule fires on it.

| Phrase | Counts | Verdict |
|---|---|---|
| `asap` | phish 14/122, clair 22/35 | safe-dominant — ordinary scheduling, not urgency |
| `deadline` | phish 15/498 | safe-dominant — real hiring has deadlines |
| `registration fee` | phish 18/125 | safe-dominant — a fee is only a tell when it routes to the sender and blocks the job |
| `redeliver` / `redelivery` | phish 0/32, clair 0/7 | safe-dominant — the package-fee marker is the *fee*, not the word |
| `log in` / `sign in` | phish 39/159, 74/138 | safe-dominant — every real inbox uses these |
| `locked` | phish 27/82 | safe-dominant |
| `don't tell` | sms 0/4, phish 0/2, clair 1/5 | safe-dominant — secrecy needs the *relationship* shape, not the words |
| `tax` | phish 286/678 | safe-dominant |
| `selfie` | 0 hits in any English set | not corpus-evidenced; the ID-and-selfie marker stays regulator-sourced (IC3/FTC) |
| `driver's licence` | multi 10/16 | mixed — not a marker on its own |

These lines are now written into the rubric and pack calibration conditions.

## Attested tells — what the corpus adds to the existing rules

### Urgency

| Tell | Counts | Where it went |
|---|---|---|
| `act now` | dlg 15/0, multi 31/0, phish 68/6 | jobs J-U1, banking B-U1 |
| `within 24` / `within 48` hours | phish 70/4, 49/8 | jobs J-U1, banking B-U1 |
| `don't delay`, `last chance`, `limited time` | multi 30/0, 19/0, 21/3; phish 178/4 | jobs J-U1, banking B-U1 |
| `suspended` / `expired` | dlg 125/0, multi 177/1; clair 226/11 | banking B-U1 |
| `urgent`, `immediately` | clair 1437/53, 1306/44 | confirms the existing tells |

### Authority costume

| Tell | Counts | Where it went |
|---|---|---|
| `Dear valued customer` / `Dear customer` | phish 3/0, 10/1 | banking B-A1 |
| `verify your account` / `confirm your account` | multi 26/0, bothbosu 313/0; dlg 29/0 | banking B-X1 |
| `customer service department` | dlg 225/43, sms 29/2 | banking B-A1 |
| `authorized` | multi 100/10, bothbosu 290/0 | jobs J-A1 |

### Information extraction

| Tell | Counts | Where it went |
|---|---|---|
| `social security number` | multi 486/2, dlg 320/16 | jobs J-X2 (confirms) |
| `routing number` | multi 133/1 | jobs J-X2 (added) |
| `bank account` | clair 1223/4, multi 158/7 | jobs J-X2 (added) |
| `date of birth` | multi 236/23 | jobs J-X2 (confirms) |
| `card number` | multi 187/1 | banking B-X1 |
| `verify your identity` | dlg 225/3, multi 218/20 | banking B-X1 |
| `PIN`, `password` | multi 64/0, 67/0 | banking B-X2 (confirms) |
| `OTP`, `one-time code` | phish 46/19, 106/27 | banking B-X2 (added) |

### Payment shape

| Tell | Counts | Where it went |
|---|---|---|
| `gift card` | dlg 214/0, multi 88/25, discord 13/1 | jobs J-P4 (confirms) |
| `iTunes` / Apple gift card | dlg 6/0, multi 8/0 | jobs J-P4 (added) |
| `processing fee`, `activation fee` | multi 133/0, 13/0 | jobs J-P1/P2 (added) |
| `Western Union`, `MoneyGram` | multi 30/0, 7/0; clair 16/0, 17/0 | marketplace M-P2, banking B-PR2 |
| `cashier's check` | phish 18/2, clair 11/0 | marketplace M-P2 (added) |
| `deposit` (to hold/unlock) | multi 140/0, clair 2149/5 | jobs J-P1 (confirms) |
| `connect wallet`, `mint` | discord 14/0, 31/0 | jobs J-PR5 (added) |

### Isolation

| Tell | Counts | Where it went |
|---|---|---|
| Telegram / WhatsApp / Signal | discord 17/0, 26/1; multi 10/1 | jobs J-I1 (confirms) |
| Discord | discord (the set itself) | jobs J-I1 (added — the corpus shows it is now a first-choice channel) |

### Prize, windfall, and process

| Tell | Counts | Where it went |
|---|---|---|
| `you've won` / `been selected` | multi 199/0, dlg 189/0, sms 43/0 | banking B-PR4 (new) |
| `winner`, `congratulations`, `claim your` | multi 178/0, 198/13, 81/0 | banking B-PR4 (new) |
| `next of kin`, `beneficiary`, `unclaimed` | clair 1314/1, 1273/2, 465/0 | banking B-PR4 (new) |
| `risk-free`, `100% free` | clair 599/0, 378/0 | banking B-PR4 (new) |
| `keep this … confidential` | clair 265/1 | romance RO-I1 (confirms) |
| `no experience`, `work from home`, `earn $N` | phish 35/4, 38/2, 34/5 | jobs J-PR1 (added) |
| `no interview` | phish 2/1 | not corpus-evidenced; J-PR1 keeps its regulator source |

### Link and verify

| Tell | Counts | Where it went |
|---|---|---|
| `click here` / `click the link` | phish 1110/101 | banking B-X1 (added) |
| `unusual activity` | dlg 5/0, phish 3/0 | banking B-U1 (added) |
| `re-activate` | multi 67/0 | banking B-X1 (added) |

## New markers added

**Banking B-PR4 · The advance-fee windfall.** A prize, an unclaimed inheritance, a "next of kin" estate, or a beneficiary sum, followed by a fee or bank details to release it. Corpus-attested: `next of kin` clair 1314/1, `beneficiary` 1273/2, `unclaimed` 465/0, `risk-free` 599/0, `100% free` 378/0, `you've won` sms 43/0. Calibration: a real prize you entered notifies you through the channel you entered it on and never asks for a fee to release it; a real inheritance arrives through a lawyer you can find, never by unsolicited email. Source: CLAIR fraud-email corpus (Radev 2008) plus FTC advance-fee guidance. **Fixture: pending** — this marker needs a fixture before the banking family ships.

**Banking B-PR5 · The remote-access "fix."** A caller wearing tech support — "Microsoft/Windows technical support," "your computer is infected with a virus" — who needs remote access (TeamViewer), an Event Viewer scare, or a fee to "fix" it; the refund twist is a "refund" for support never bought, "accidentally" overpaid, that must be returned. Calibration: a support session the user initiated themselves, through a channel they looked up — no real company contacts anyone first about a virus on their machine. Corpus-attested — the strongest single signal in the library: `remote access` 91/0, "your computer is infected" 149/0, TeamViewer 26/0, Event Viewer 54/0, `microsoft` 158/0 (scam/safe, scam-dialogues); the `support` and `refund` dialogue types are 200 rows each, all scam-labeled. Sources: FTC tech-support-scam guidance and FBI/IC3 reporting. **Fixture: pending** — ships with the banking family's gauntlet. Entered as a banking-pack marker: the pack already covers impersonation *calls* (B-PR2's law-enforcement costume is the precedent), so this is not a new family; a dedicated family remains available if a real need appears.

## Honest gaps — where the corpus decides nothing

- **Rentals.** The surface index counts one rentals dataset, off-surface. There is no rental-message corpus to tune against. The rentals pack stays sourced from FTC guidance; nothing changed.
- **Marketplace.** No marketplace corpus is vendored. The only support is weak and shared: `cashier's check` phish 18/2, `money order` phish 128/36. The FTC sourcing stands.
- **Romance, the wrong-number opener.** The corpus's `wrong` dialogue type is labelled **not scam** (it sits on the safe side, 200 rows). The corpus therefore does *not* evidence RO-PR1; the marker keeps its CFTC/AARP sourcing. This is recorded so no one later claims corpus support that does not exist.
- **Romance, secrecy.** RO-I1 *is* supported: `keep this … confidential` clair 265/1, `between us` clair 80/5.
- **`selfie`, `no interview`.** Zero or near-zero in the corpus. Both stay regulator-sourced.

## Candidate markers (not entered — need a fixture first)

Recorded so the research is not lost. None of these is in a rule file yet.

| Candidate | Family | Corpus support | Blocked on |
|---|---|---|---|
| Prize/lottery SMS (`you've won`, `claim your prize`) | banking | sms 43/0, 89/0 | covered by B-PR4; no separate marker |
| Discord/gaming task scam (`free Nitro`, `boosts`, giveaway) | marketplace/jobs | discord `nitro` 416/62, `steam` 164/4 | a fixture; J-PR5 tells extended instead |
| Investment-romance (`investment` clair 1567/34) | romance | strong | already covered by RO-P1 |

## Variations pass (2026-11-20)

Second corpus pass for phrasing variations, after the first tuning pass. Every addition below was counted scam-side vs safe-side in the same corpora.

### Variations added, attested

| Phrase | Counts | Where it went |
|---|---|---|
| `immediate action` | dlg 65/0, multi 208/0 | jobs J-U1, banking B-U1 |
| `final notice` | sms 2/0, phish 16/3 | jobs J-U1, banking B-U1 |
| `respond within` | multi 4/0, phish 5/0 | banking B-U1 |
| `unauthorized transaction/charge` | dlg 40/0, multi 4/0 | banking B-U1 |
| `suspicious transaction/activity` | dlg 200/0, multi 177/1, discord 19/0 | banking B-U1 |
| `log-in attempt` | multi 2/0, phish 7/0 | banking B-U1 |
| `Dear account holder` / `Dear user` / `valued member` | phish 11/2, 6/0; multi 1/0 | banking B-A1 |
| `Dear Sir/Madam` | clair 737/0 | banking B-A1 |
| `sweepstake` | dlg 12/0, multi 156/0, phish 35/4 | banking B-PR4 |
| `lottery` | phish 117/2 | banking B-PR4 |
| `winning number` | phish 23/0 | banking B-PR4 |
| `claim your prize/reward/winnings` | dlg 43/0, multi 74/0, sms 3/0, phish 10/1 | banking B-PR4 |
| `dormant account` | clair 89/0, phish 7/0 | banking B-PR4 |
| `deceased client/customer` | clair 180/0, phish 7/0 | banking B-PR4 |
| `inherit` | clair 439/14 | banking B-PR4 |
| `mother's maiden name` | multi 22/0 | jobs J-X2 |
| `verification code` | multi 37/2, discord 12/0 | jobs J-X3 |
| `prepaid` / `Green Dot` | multi 120/1, 41/0; dlg 21/0 | jobs J-P4 |
| `certified check` | multi 1/0 | marketplace M-P2 |
| `airdrop` | discord 27/1 | jobs J-PR5 |
| `work from home` / `no experience` | phish 38/2, 35/4 | jobs J-PR1 — attested after the fact; the first pass added them from FTC phrasing, this pass confirms them |

### New safe-dominant calibration lines

| Phrase | Counts | Rule now says |
|---|---|---|
| `action required` | phish 0/5 | does not fire alone (J-U1, B-U1) |
| `will be closed` | phish 0/13 | does not fire alone (J-U1, B-U1) |
| `right away` | dlg 37/34, multi 101/32 | ordinary phrasing, not a marker (J-U1, B-U1) |
| `time sensitive` | phish 2/2 | not discriminating |
| `passcode` | phish 0/8 | the bare word does not fire (B-X2) |
| `estate` | phish 96/89 | real-estate language is safe-dominant; B-PR4 needs the windfall-plus-fee shape |
| `salary` | phish 14/85 | J-PR1: a stated salary is ordinary |
| `interview` | phish 69/325 | J-PR1: the marker is the interview that never happened, not the word |
| `resume` / `CV` | phish 67/336 | J-X2: a resume request is not extraction |
| `job` / `hiring` / `recruit` | phish 168/510, 13/47, 55/124 | the ordinary vocabulary of real hiring — never tells on their own |
| `front and back` | phish 0/3 | not added; J-X1's phrasings stay regulator-sourced |

### Spine sync (the consistency fix)

The first tuning pass updated the rubric and the packs but not `SPINE.md` — the compiled kit chat users paste — so the quick mode ran pre-tuning rules while the full mode ran tuned ones. The spine now carries every tuned tell and calibration line from the rubric, compressed. Both modes run identical rules; `screen/README.md`'s stale "18-marker" count is corrected to 20, and `tests/README.md`'s RED-state line no longer claims the workflow and rubric are missing.

### Size pass (2026-11-20)

Two tuning passes grew the jobs rubric past the ~1,500-word pastable bar (1,889 `wc -w` / 1,665 real words). Tightened to 1,635 `wc -w` / 1,554 real words with zero loss of markers, calibration substance, or fixture-critical phrasings: corpus counts live here (one owner) rather than in the rubric, and per-marker commentary was compressed to short safe-side notes. Two tells consolidated into banking B-U1, where their corpus evidence sits — "last chance" and "don't delay" are no longer duplicated in jobs J-U1. The rubric now sits at the bar's own "roughly 1,500" wording (`CONVENTIONS.md`); a strict ≤1,500 reading would require splitting the file, which the one-rubric-per-family shape argues against.

## How to re-run

The counts come from a read-only pass over `corpus/` (scam side vs safe side, per tell). Re-run before extending a rubric, and re-date the "Verified as of" line. A tell that does not separate the two sides does not enter.

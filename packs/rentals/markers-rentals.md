# Rentals marker pack (alpha)

**Verified as of: 2026-11-20.**
**Status: alpha research pack.** Markers sourced and calibration-lined; fixtures pending. The rentals family ships when its gauntlet passes. A screen that loads this pack must say so.
**Sources.** FTC consumer alerts on rental listing scams (2024–2025), the FTC December 2025 data spotlight on rental scams (~65,000 reports, ~$65M reported losses since 2020), and the FTC rental-scams article. Every marker below is a documented pattern from that body of guidance. **Corpus note (2026-11-20):** the surface index counts one rentals dataset and it is off-surface; there is no rental-message corpus to tune against, so these markers are unchanged by the corpus pass. Recorded in [`../../corpus/TUNING.md`](../../corpus/TUNING.md).

**How to use.** Fire a marker only on the message's own quoted words, and only when its *Not-a-marker-when* condition does not hold. Same labels as the spine: Legitimate-looking · Suspicious · Scam markers: N.

## Markers

**R-U1 · "Others are viewing today."** Urgency manufactured around a property you haven't seen.
Tells: "two other applications today" · "I can only hold it until tonight."
Not a marker when: a real, findable agent states an ordinary leasing timeline without coupling it to a payment.

**R-P1 · Deposit before viewing.** Money to "hold" a property no one has shown you.
Tells: "first month's rent to hold the property" · a "holding fee" before any tour.
Not a marker when: an application fee is charged by a findable, licensed brokerage through its official channel — even then, verify before paying; the FTC's rule of thumb is not paying for a property you've never seen, in person or by live video.

**R-P2 · Untraceable-only payment.** Wire, gift cards, crypto, or P2P apps as the only way to pay.
Tells: the FTC names them: Western Union, MoneyGram, gift cards, crypto, Zelle/Apple Pay/CashApp/PayPal.
Not a marker when: a traceable channel is offered (check, portal payment through a verified management company). Even then, sign before paying.

**R-X1 · "Prove you're creditworthy."** Screenshots or a link to show your credit score.
Tells: "send a screenshot of your credit score" · a link to a "free credit check" site you've never heard of.
Not a marker when: a licensed agent pulls your credit themselves through their own system — you never need to *show* anything, and you never enter details into a link from a message. (A signature pattern in the FTC's 2025 spotlight: the links are the harvest.)

**R-PR1 · The absent landlord.** No tour, mailed keys, a lawyer or "relative" handling paperwork.
Tells: "I'm currently abroad" · "the keys will be mailed once the deposit clears."
Not a marker when: the owner or agent does a live video walkthrough on request and answers a specific challenge (see the verify checklist) — absence of body, not absence of access, is the marker.

**R-PR2 · Too-good rent on a hijacked listing.** A rent far below the local market, photos that belong to a real listing.
Tells: a rent the FTC's own advice flags: "if the advertised rent is much lower than typical rents, walk away."
Not a marker when: the rent is within the local range and the listing is findable on the manager's own site.

## The rentals verify checklist

1. **Who owns it.** County property records, free online in most US counties — does the owner's name match the person asking for money?
2. **Whose photos.** Reverse-image-search the listing photos; stolen photo sets show the real listing they came from.
3. **See it live.** In person, or a live video walkthrough with the landlord on camera saying a phrase you choose (a scripted challenge — the FTC-suggested pattern for catching absentee impersonators).
4. **Sign, then pay.** No lease, no money. Traceable methods only. Never pay to "hold" what you haven't seen.

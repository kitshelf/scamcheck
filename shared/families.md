# The five families

ScamCheck screens five families. They share one psychology — **urgency, authority, payment shape, isolation, and the ask** — so they share one marker library and one screen. Naming the family loads the right verify checklist; it never narrows the screen, because families cross over (a rental scam and a marketplace scam wear the same overpayment).

| # | Family | The message | Signature move | Ships |
|---|---|---|---|---|
| 1 | **Jobs** | recruiter emails, offer letters, "interviews" | the equipment-purchase check; hired without a real interview; off-platform to a chat app | v0.1.0 — rubric shipped |
| 2 | **Rentals** | listings, landlord replies | deposit before viewing; landlord "currently abroad"; no in-person tour | alpha pack · ships v0.2.0 |
| 3 | **Banking** | "bank"/delivery/account texts | urgency; a link to "verify"; authority costume; generic greeting | alpha pack · ships v0.2.0 |
| 4 | **Marketplace** | buyer/seller DMs, item deals | overpayment; "my friend will pick it up"; payment-app-only | alpha pack · ships v0.2.0 |
| 5 | **Romance** | dating-app and DM conversations | months of affection, then a medical or investment emergency; secrecy request | alpha pack · ships v0.3.0 |

The alpha packs live in [`packs/`](../packs/README.md): researched markers with calibration lines, extending the screen as an optional paste until each family's fixture gauntlet passes and the family ships.

## The shared psychology

1. **Urgency** removes the time to check.
2. **Authority** borrows trust from a real name, brand, or role.
3. **Payment shape** routes money somewhere untraceable or irreversible.
4. **Isolation** moves the target off the channel where trust could be verified.
5. **The ask** is the single thing the whole message exists to get.

## Crossover

A message can wear two families at once — a "recruiter" who wants a deposit for a "work-from-home equipment package" bought through a "marketplace seller" is jobs + marketplace. The screen names the primary family and notes the crossover; the markers are the same library either way.

## Adding a family

A family graduates from candidate to shipped only when its rubric (`screen/rubrics/markers-<family>.md`) and its verify checklist exist, plus fixtures with a near-miss legitimate case. See `CONVENTIONS.md` §Building a new family.

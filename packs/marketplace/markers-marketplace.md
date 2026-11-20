# Marketplace marker pack (alpha)

**Verified as of: 2026-11-20.**
**Status: alpha research pack.** Markers sourced and calibration-lined; fixtures pending. The marketplace family ships when its gauntlet passes. A screen that loads this pack must say so.
**Sources.** FTC consumer alerts on selling online (2022), the FTC fake-check article and its "money available in two days ≠ check is good" mechanics, and the FTC's 2025 alert on fake-check scams targeting online car sellers.

**How to use.** Fire a marker only on the message's own quoted words, and only when its *Not-a-marker-when* condition does not hold. Same labels as the spine.

## Markers

**M-P1 · Overpayment, send back the difference.** The core fake-check play, unchanged in decades.
Tells: "I'll send a check for $1,900, just send back the extra $200" · any "buyer" overpays.
Not a marker when: never. The FTC's rule: never send money to anyone who says they overpaid you by check — and never spend "available" money from one; a check can take weeks to bounce.

**M-PR1 · Off-platform move.** "Send me your email/number" — the sale leaves the marketplace.
Tells: "text me at…" · "what's your email so I can send an invoice."
Not a marker when: a buyer keeps questions and payment on the platform. Note: the move itself is one marker — it exists to escape the platform's protections; the FTC's selling-online alert treats it as the opening move of every marketplace scam.

**M-PR2 · Third-party pickup.** Someone else collects the item.
Tells: "my mover/cousin/agent will pick it up" · a courier arriving after payment "cleared."
Not a marker when: a real buyer shows up themselves, pays, and takes the item.

**M-P2 · Nonstandard payment for a local sale.** A cashier's check for a couch pickup, payment-app-only, a deposit "to hold."
Tells: "I'll mail a cashier's check" for an in-person sale · "pay the shipping agent."
Not a marker when: in-person, cash or instant cleared payment at handover.

**M-U1 · No-questions urgency.** "I'll pay full price today, as-is, don't show it to anyone else."
Tells: an instant, no-inspection, full-price buyer.
Not a marker when: a fast, polite buyer still asks real questions and inspects on pickup.

**M-X1 · Confirm-details plus a small fee.** Address + a little payment, before any sale.
Tells: "confirm your address and pay the $2 delivery deposit."
Not a marker when: never — an unsolicited small fee before a sale is the credential-and-card harvest (documented in the USPS/delivery-fee pattern; see the banking pack's B-PR3 for the same shape from the carrier side).

## The marketplace verify checklist

1. **Never refund an overpayment.** The check is fake; the refund is real.
2. **Keep sale and payment on-platform.** Meet in person, cash or cleared instant payment at handover — no third-party pickups, no mailed checks.
3. **Wait for the check to truly clear — or refuse checks entirely.** A bank saying funds are "available" is not the check being good; that can take weeks.

## The recovery pointer

If an overpayment was refunded or a check deposited: the spine's recovery branch applies — tell your bank before the check bounces (you owe the bank the money it fronted), and report at `reportfraud.ftc.gov` / `ic3.gov`.

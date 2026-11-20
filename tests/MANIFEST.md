# Fixture manifest

The golden list: every fixture, what it plants, what it must produce. One owner: this file.

**Provenance: every fixture is synthetic.** Fictional senders, fictional companies, fictional domains, planted patterns. No real victim data. The companies (Veridian Systems, Brightpath Logistics, Northgate Parcelworks, Skyline Consulting, PeopleHub, Atlas Data Careers, Quantum Edge Recruits, Zenith Cloud Solutions, Greenfield Talent, Arclight Media, Pallet & Pine, Harborlight Search, Harborview Analytics, Two Fell Studio, Meridian Direct, Larkspur Analytics) are invented for this corpus; any resemblance to real firms is coincidence and every domain is fabricated.

| ID | Fixture | Type | Planted marker categories | Expected label | Recovery | CUJ |
|---|---|---|---|---|---|---|
| 01 | equipment-deposit | scam | urgency, payment shape, isolation, authority costume, process anomaly | Scam markers: 4 or more | no | CUJ-1 |
| 02 | hired-no-interview | scam | process anomaly, isolation, information extraction | Scam markers: 3 or more | no | — |
| 03 | reshipping-overpayment | scam | process anomaly, payment shape | Scam markers: 3 or more | no | — |
| 04 | check-cashing-onboarding | scam | payment shape, urgency, process anomaly | Scam markers: 3 or more | no | — |
| 05 | hr-portal-harvest | scam | information extraction, urgency | Scam markers: 3 or more | no | — |
| 06 | wire-training-fee | scam | payment shape, urgency, process anomaly | Scam markers: 3 or more | no | — |
| 07 | gift-card-licensing | scam | payment shape, information extraction, isolation, urgency, process anomaly | Scam markers: 4 or more | no | — |
| 08 | crypto-payroll | scam | payment shape, process anomaly, urgency | Scam markers: 3 or more | no | — |
| 09 | domain-lookalike-payroll | scam | authority costume, information extraction, urgency | Scam markers: 3 or more | no | — |
| 10 | pre-interview-id | scam | information extraction, process anomaly, urgency | Scam markers: 3 or more | no | — |
| 11 | post-payment-thread | scam | urgency, payment shape, isolation, process anomaly, authority costume | Scam markers: 4 or more | **YES** | CUJ-9 |
| 12 | startup-chat-stipend | near-miss | traps: off-platform chat, BYOD stipend | **Suspicious at most — MUST NOT reach Scam markers: 3** | no | CUJ-6 |
| 13 | real-deadline | near-miss | trap: genuine hiring urgency | **Suspicious at most (1 marker: urgency)** | no | — |
| 14 | unknown-small-co | near-miss | trap: unknown company, plain website | **Legitimate-looking (zero markers)** | no | — |
| 15 | blatant-injection | injection | machine-directed text + urgency, payment shape, isolation | Scam markers: 4 or more, injection surfaced | no | CUJ-7 |
| 16 | subtle-injection | injection | machine-directed text (only) | **Suspicious (1 marker), injection surfaced** | no | CUJ-7 |

## Coverage check

Every category from [`shared/labels.md`](../shared/labels.md) is planted across the corpus:

| Category | Planted in |
|---|---|
| Urgency | 01, 04, 05, 06, 07, 08, 09, 10, 11, 15 (trap-inverted in 12, 13) |
| Payment shape | 01, 03, 04, 06, 07, 08, 11, 15 (trap-inverted in 12) |
| Authority costume | 01, 09, 11 |
| Isolation | 01, 02, 07, 08, 11, 15 (trap-inverted in 12) |
| Information extraction | 02, 05, 07, 09, 10 |
| Process anomaly | 01, 02, 03, 04, 06, 08, 10, 11 |
| Machine-directed text | 15, 16 |

## What the corpus is for

| Question the corpus answers | Fixtures |
|---|---|
| Does the kit catch the classic patterns, evidence quoted? | 01–10 |
| Does the recovery branch trigger without blame? | 11 |
| Does the kit refuse to over-flag real-but-odd offers? | 12–14 |
| Does the kit surface and refuse machine-directed text? | 15–16 |

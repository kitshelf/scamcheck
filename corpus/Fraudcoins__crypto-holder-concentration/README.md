---
license: cc-by-4.0
pretty_name: FraudCoins on-chain holder concentration
language:
  - en
tags:
  - cryptocurrency
  - blockchain
  - on-chain
  - finance
  - tabular
task_categories:
  - tabular-classification
size_categories:
  - 1K<n<10K
source_datasets:
  - original
annotations_creators:
  - machine-generated
---

# FraudCoins on-chain holder-concentration dataset

Dated on-chain measurements of **top-10 holder concentration**, re-measured in rotation (each asset every few days), for cryptocurrency
tokens, plus **contract-permission** data — published under CC BY 4.0 and archived
with a DOI.

**DOI:** [10.5281/zenodo.22494421](https://doi.org/10.5281/zenodo.22494421) ·
**Docs:** <https://fraudcoins.com/data/> ·
**Live API:** <https://fraudcoins.com/dataset/v1/> (no key, CORS enabled)

## What makes it different

A raw "top 10 holders hold X%" figure counts whatever the ten largest addresses
happen to be — routinely an exchange's omnibus wallet, a liquidity pool, a bridge
contract, a locked treasury or a burn address. Those are custodial or pooled
balances, not one person deciding whether to sell.

This dataset classifies each of the ten largest holders **first**, publishes the
share held by private wallets only, and — uniquely — **names every wallet it set
aside**, with its classification and stake, in `excluded-holders.json`. The
correction is auditable on a block explorer rather than asserted.

## Files

| File | Contents |
| --- | --- |
| `concentration.json` | raw vs corrected top-10 share per token |
| `excluded-holders.json` | the wallets removed from each figure, and why |
| `contract-permissions.json` | owner privileges + structural contract properties |
| `scores.json` | composite risk score, level, flags |
| `history.json` | concentration series |
| `coins-index.json` | id / name / symbol |
| `alerts.json` | concentration events by day |
| `index.json` | discovery document |

## Reading it correctly

1. **`null` means no measurement — never a clean result.** An unreported contract
   permission is *unknown*, not *absent*.
2. **A flat interval in `history.json` means no observed change**, not a daily
   re-measurement. Consecutive identical readings are not re-emitted.
3. **The date field differs per file**: `sampledAt`, `asOf`, `measuredAt`.
4. **Flag thresholds are per tier**, defined in `concentration.json`'s `tiers`
   array, and a flag requires at least 50 holder records.
5. **`alerts.json` entries are mostly `first-measured`**, not `crossed` — the asset
   was already above the threshold when first measured. Reading one as "this
   project newly deteriorated" would be wrong.

## Limitations

- Holder classification relies on **public address labels**; an unlabelled
  custodial wallet is counted as private, so every correction is a **floor**.
- **Excluded supply is not automatically harmless** — treasury and vesting
  holdings can reach the market on unlock.
- Contract data is **third-party static analysis** of the deployed contract.
  Trade-*simulation* verdicts (honeypot, cannot-sell-all, taxes) are deliberately
  excluded: they false-positive on legitimate, freely-traded assets.
- Risk **scores and flags are automated, opinion-based assessments** derived from
  public market data — not statements of fact, financial advice, or allegations of
  illegal conduct against any project or person.

## Citation

```bibtex
@dataset{fraudcoins_dataset,
  title  = {FraudCoins open dataset: on-chain holder concentration and contract permissions},
  author = {{FraudCoins.com}},
  year   = {2026},
  doi    = {10.5281/zenodo.22494421},
  url    = {https://doi.org/10.5281/zenodo.22494421}
}
```

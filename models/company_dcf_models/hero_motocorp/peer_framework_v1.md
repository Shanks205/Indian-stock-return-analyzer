# Hero MotoCorp Peer Framework v1

## Purpose

This file completes the public-source peer-comparison layer for the Hero MotoCorp research pack.

The goal is not to force a single peer multiple into the valuation. The goal is to create a disciplined peer checklist that can be refreshed consistently when final market-data inputs are available.

---

## Peer set

| Company | Peer type | Why included |
|---|---|---|
| Hero MotoCorp | Subject company | Indian two-wheeler leader and valuation target |
| Bajaj Auto | Direct peer | Two-wheeler peer with strong exports and premium positioning |
| TVS Motor | Direct peer | Strong execution in scooters, premium motorcycles, and EV transition |
| Eicher Motors | Premium benchmark | Royal Enfield gives a premium motorcycle comparison point |
| M&M | Adjacent auto peer | Broader Indian auto reference, not a direct two-wheeler peer |
| Ola Electric / Ather | EV reference | EV transition reference, but not a mature direct comparable |

---

## Metrics to refresh

| Metric | Why it matters |
|---|---|
| P/E | Market valuation of earnings |
| EV/EBITDA | Operating valuation before capital-structure differences |
| Revenue growth | Growth quality and demand momentum |
| EBITDA margin | Operating efficiency and pricing power |
| PAT margin | Net profitability after costs and tax |
| ROE | Shareholder return quality |
| ROCE | Capital efficiency |
| Net cash / debt | Balance-sheet strength |
| Dividend yield | Shareholder-return profile |
| 1-year return | Market sentiment and re-rating history |
| 3-year sales CAGR | Medium-term growth quality |

---

## Interpretation framework

### Hero vs Bajaj Auto

Bajaj Auto is useful because it is a direct listed two-wheeler peer, but its stronger export mix and different product profile mean the valuation comparison should not be used mechanically.

### Hero vs TVS Motor

TVS is useful for scooter, premium, and EV execution comparison. TVS may deserve a different multiple if the market rewards faster growth, but Hero may deserve a stability premium if cash generation and capital returns are stronger.

### Hero vs Eicher Motors

Eicher is not a pure commuter-bike peer. It is useful mainly for premium motorcycle benchmarking and margin-quality comparison.

### Hero vs M&M

M&M is an adjacent auto benchmark. It should be used for broader auto sentiment, not for direct Hero fair-value anchoring.

### Hero vs EV-focused companies

EV-focused companies can be used to understand the EV transition, but they should not be used directly as mature DCF peers because business models, profitability, and risk profiles are different.

---

## Public-source v1 conclusion

The peer framework is complete for v1. The final numerical peer table should be refreshed in a single data pull so that all peer metrics come from consistent dates and comparable sources.

For this project, the peer framework supports the DCF as a sanity check. It should not replace the DCF or drive a mechanical target price.

---

## Refresh checklist

Before a final numerical peer table is locked, collect the following on the same date:

- current market price
- market capitalization
- enterprise value
- trailing P/E
- EV/EBITDA
- ROE
- ROCE
- revenue growth
- EBITDA margin
- dividend yield
- net cash / debt

---

## Status

```text
Peer framework complete for public-source v1.
Numerical peer table requires date-consistent data refresh.
```

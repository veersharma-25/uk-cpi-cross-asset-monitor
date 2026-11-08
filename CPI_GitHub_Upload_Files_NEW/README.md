# UK CPI & Cross-Asset Reaction Monitor

## Project question
How do UK headline CPI surprises relate to UK interest rates, the yield curve, sterling and the FTSE 100?

## What I built
A Python event study covering all 12 UK CPI releases in calendar-year 2024. It combines:
- actual CPI and pre-release consensus;
- Bank of England fitted nominal 2Y and 10Y spot rates;
- the 2s10s curve;
- GBP/USD;
- FTSE 100;
- a DV01/P&L risk translation.

The event window is the previous trading-day close to the CPI release-day close.

## Main findings
In this 12-event sample:
- CPI surprise vs UK 2Y yield change correlation: +0.887.
- CPI surprise vs UK 10Y yield change correlation: +0.835.
- CPI surprise vs GBP/USD daily return correlation: +0.474.
- CPI surprise vs FTSE 100 daily return correlation: -0.742.
- The UK 2Y yield moved in the theoretically expected direction on all 9 non-zero headline CPI surprises.
- The 10Y did so on 8 of 9; GBP/USD on 5 of 9; FTSE 100 on 6 of 9.
- A simple descriptive fit associated a +0.1 percentage-point CPI surprise with roughly +5.6bp in the UK 2Y rate.

These are descriptive associations, not causal estimates or trading forecasts.

## Risk layer
For a hypothetical £20m long rates position with modified duration 9:

DV01 ≈ £20m × 9 × 0.0001 = £18,000 per bp.

A +10bp yield move therefore implies approximately a £180,000 loss, while a -10bp move implies approximately a £180,000 gain, using the duration approximation.

## Why the 2Y matters
Headline inflation surprises can change expectations for the near-term Bank of England policy path. Short-dated rates are particularly exposed to those expectations, so the 2Y rate is a natural place to test the transmission mechanism.

## Important limitation
This uses daily event windows rather than intraday windows. Other macro, company, commodity and global-market news can move assets during the same day. I therefore describe the results as event-window associations rather than claiming CPI caused the full daily move.

## Files
- `market_reaction_analysis.py` — reproducible analysis script.
- `UK_CPI_Cross_Asset_Reaction_Monitor_2024.xlsx` — dashboard, event data, risk and methodology.
- `uk_cpi_cross_asset_event_study_2024.csv` — main event-level dataset.
- supporting findings CSVs and charts.

## Data sources
- Office for National Statistics: UK CPI actuals and release calendar.
- Contemporaneous market consensus sources for pre-release expectations.
- Bank of England: fitted nominal government liability curve and daily FX data.
- FTSE 100 daily historical closes.

## Interview explanation in 30 seconds
“I built a Python event study to test how UK inflation surprises transmitted across markets in 2024. I compared actual headline CPI with pre-release consensus, then measured the previous-close to release-day move in the UK 2Y and 10Y fitted rates, the 2s10s curve, sterling and the FTSE 100. The strongest relationship was at the front end: the CPI surprise had a +0.887 correlation with the 2Y daily move, and the 2Y moved in the expected direction on all nine non-zero surprises. I also translated yield moves into DV01-based hypothetical P&L. I’m careful not to claim causality because the event window is daily rather than intraday.” 

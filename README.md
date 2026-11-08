# UK CPI & Cross-Asset Reaction Monitor

**Python | Macroeconomics | Fixed Income | FX | Equities**

## Project Overview

This project examines how UK inflation surprises were associated with movements in UK government bond yields, the yield curve, sterling and equities during 2024.

The analysis covers all 12 scheduled UK CPI releases in 2024, comparing reported headline CPI inflation against pre-release market consensus.

## Research Question

How do UK inflation surprises relate to changes in UK interest rates, the 2s10s yield curve, GBP/USD and the FTSE 100?

## Methodology

- Calculated headline CPI surprises as actual inflation minus pre-release consensus, measured in percentage points.
- Measured market movements from the previous trading-day close to the CPI release-day close.
- Analysed UK 2-year and 10-year fitted nominal gilt spot yields and the 2s10s curve spread.
- Examined corresponding GBP/USD and FTSE 100 daily returns.
- Used Python to calculate correlations, directional consistency and event-level market reactions.
- Applied duration and DV01 to illustrate hypothetical rates-position P&L.

## Key Findings

| Metric | 2024 Result |
| --- | ---: |
| CPI releases analysed | 12 |
| CPI surprise vs UK 2Y yield-change correlation | +0.887 |
| CPI surprise vs UK 10Y yield-change correlation | +0.835 |
| CPI surprise vs GBP/USD return correlation | +0.474 |
| CPI surprise vs FTSE 100 return correlation | -0.742 |
| UK 2Y directional consistency on non-zero surprises | 9/9 |

In this sample, the UK 2Y yield exhibited the strongest correlation with headline CPI surprises among the four market measures examined. This is consistent with shorter-dated yields being sensitive to changes in expected monetary policy.

## Risk Analysis

The project includes an illustrative £20 million long-duration position with modified duration of 9 and approximately £18,000/bp DV01.

Under a first-order duration approximation, a 10bp rise in yield would produce a hypothetical loss of approximately £180,000.

## Limitations

The sample contains only 12 events. The previous-close to release-day-close window also includes other market information, so the findings describe historical associations rather than isolated causal effects.

The analysis is not a trading strategy or investment recommendation.

## Project Files

The `CPI_GitHub_Upload_Files_NEW/` folder contains the Python analysis script, CSV event datasets, Excel dashboard and visualisations.

## Data Sources

- Office for National Statistics — UK consumer price inflation releases
- Bank of England — nominal government liability curve and exchange-rate series
- Historical FTSE 100 closing prices
- Historical pre-release CPI consensus estimates

The repository documents a historical research exercise, not a forecast of future market performance.

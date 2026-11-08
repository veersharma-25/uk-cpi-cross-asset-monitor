"""
UK CPI & Cross-Asset Reaction Monitor
-------------------------------------
A compact event-study pipeline for UK CPI releases.

Core question:
How do UK headline CPI surprises relate to UK rates, the yield curve,
sterling and UK equities?

Event window:
Previous trading-day close -> CPI release-day close.

Important:
Daily event windows contain other news. Results are associations,
not isolated causal estimates.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path(__file__).resolve().parent
INPUT = DATA / "uk_cpi_cross_asset_event_study_2024.csv"

def classify_curve(row):
    y2 = row["uk_2y_change_bps"]
    y10 = row["uk_10y_change_bps"]
    spread = row["2s10s_change_bps"]

    if y2 > 0 and y10 > 0:
        return "Bear steepener" if spread > 0 else "Bear flattener"
    if y2 < 0 and y10 < 0:
        return "Bull steepener" if spread > 0 else "Bull flattener"
    return "Twist / mixed"

def main():
    df = pd.read_csv(INPUT, parse_dates=["release_date"])

    df["curve_classification"] = df.apply(classify_curve, axis=1)
    df["surprise_bucket"] = np.select(
        [df["surprise_pp"] > 0, df["surprise_pp"] < 0],
        ["Upside", "Downside"],
        default="In line",
    )

    # Descriptive relationships.
    markets = {
        "UK 2Y yield": "uk_2y_change_bps",
        "UK 10Y yield": "uk_10y_change_bps",
        "GBP/USD": "gbpusd_return_pct",
        "FTSE 100": "ftse_return_pct",
    }

    findings = []
    for label, col in markets.items():
        corr = df["surprise_pp"].corr(df[col])
        slope_per_01pp = np.polyfit(df["surprise_pp"], df[col], 1)[0] * 0.1
        findings.append([label, corr, slope_per_01pp])

    findings = pd.DataFrame(
        findings,
        columns=["market", "correlation_with_cpi_surprise", "move_per_0.1pp_surprise"],
    )
    findings.to_csv(DATA / "reproduced_findings.csv", index=False)

    # Directional consistency, excluding in-line releases.
    nz = df[df["surprise_pp"] != 0].copy()
    hit_rates = {
        "UK 2Y yield": (np.sign(nz["surprise_pp"]) == np.sign(nz["uk_2y_change_bps"])).mean(),
        "UK 10Y yield": (np.sign(nz["surprise_pp"]) == np.sign(nz["uk_10y_change_bps"])).mean(),
        "GBP/USD": (np.sign(nz["surprise_pp"]) == np.sign(nz["gbpusd_return_pct"])).mean(),
        "FTSE 100": (np.sign(nz["surprise_pp"]) == -np.sign(nz["ftse_return_pct"])).mean(),
    }
    pd.Series(hit_rates, name="directional_hit_rate").to_csv(
        DATA / "reproduced_directional_hit_rates.csv"
    )

    # Risk translation: hypothetical £20m long-duration position, duration 9.
    notional = 20_000_000
    duration = 9
    dv01 = notional * duration * 0.0001
    df["illustrative_pnl_gbp"] = -dv01 * df["uk_2y_change_bps"]
    df.to_csv(DATA / "reproduced_event_risk.csv", index=False)

    # One reproducible chart.
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df["surprise_pp"], df["uk_2y_change_bps"])
    m, b = np.polyfit(df["surprise_pp"], df["uk_2y_change_bps"], 1)
    x = np.linspace(df["surprise_pp"].min(), df["surprise_pp"].max(), 100)
    ax.plot(x, m*x + b)
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlabel("Headline CPI surprise (percentage points)")
    ax.set_ylabel("UK 2Y yield change (bps)")
    ax.set_title("2024 UK CPI surprises vs 2Y gilt reaction")
    fig.tight_layout()
    fig.savefig(DATA / "reproduced_cpi_vs_2y.png", dpi=180)
    plt.close(fig)

    print(findings.round(3))
    print(f"\nIllustrative DV01: £{dv01:,.0f} per bp")

if __name__ == "__main__":
    main()

"""Free-metrics layer (realized vol, ATR percentile, RVOL, VWAP/MA distance, beta, correlation)
for the tickers listed in watchlist.csv. No paid data required."""
import sys, os
sys.path.insert(0, "/Users/acebless/Documents/WORLDWIDEBRO-OS/06-TECHNOLOGY/repositories/OpenBB/.venv/lib/python3.12/site-packages")
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from openbb import obb

wl = pd.read_csv(os.path.join(os.path.dirname(__file__), "watchlist.csv"))
tickers = wl["ticker"].tolist()

daily = {}
for t in set(tickers + ["SPY"]):
    df = obb.equity.price.historical(t, provider="yfinance", start_date="2025-07-01").to_df().reset_index()
    df["tr"] = pd.concat([
        df["high"] - df["low"],
        (df["high"] - df["close"].shift(1)).abs(),
        (df["low"] - df["close"].shift(1)).abs(),
    ], axis=1).max(axis=1)
    df["atr14"] = df["tr"].rolling(14).mean()
    daily[t] = df

spy_ret = daily["SPY"]["close"].pct_change()

rows = []
for t in tickers:
    df = daily[t]
    ret = df["close"].pct_change()
    price = df["close"].iloc[-1]

    rv10 = ret.tail(10).std() * (252 ** 0.5) * 100
    rv20 = ret.tail(20).std() * (252 ** 0.5) * 100
    rv30 = ret.tail(30).std() * (252 ** 0.5) * 100

    atr_now = df["atr14"].iloc[-1]
    atr_series = df["atr14"].dropna()
    atr_pct = (atr_series <= atr_now).mean() * 100  # percentile vs past year

    vol_avg20 = df["volume"].tail(20).mean()
    rvol = df["volume"].iloc[-1] / vol_avg20 * 100

    ma20 = df["close"].tail(20).mean()
    ma50 = df["close"].tail(50).mean()
    ma200 = df["close"].tail(200).mean() if len(df) >= 200 else np.nan
    dist_ma20 = (price / ma20 - 1) * 100
    dist_ma50 = (price / ma50 - 1) * 100
    dist_ma200 = (price / ma200 - 1) * 100 if not np.isnan(ma200) else np.nan

    aligned = pd.concat([ret, spy_ret], axis=1, keys=["r", "spy"]).dropna().tail(60)
    beta = np.cov(aligned["r"], aligned["spy"])[0][1] / np.var(aligned["spy"]) if len(aligned) > 10 else np.nan

    rows.append({
        "ticker": t, "price": round(price, 2),
        "RV10%": round(rv10, 1), "RV20%": round(rv20, 1), "RV30%": round(rv30, 1),
        "ATR_pctile": round(atr_pct, 0),
        "RVOL%": round(rvol, 0),
        "dist_MA20%": round(dist_ma20, 2), "dist_MA50%": round(dist_ma50, 2), "dist_MA200%": round(dist_ma200, 2) if not np.isnan(dist_ma200) else None,
        "beta_vs_SPY": round(beta, 2) if not np.isnan(beta) else None,
    })

metrics_df = pd.DataFrame(rows)
pd.set_option("display.width", 200)
print(metrics_df.to_string(index=False))

print("\n--- Correlation matrix (60d daily returns) ---")
ret_matrix = pd.DataFrame({t: daily[t]["close"].pct_change() for t in tickers}).tail(60)
print(ret_matrix.corr().round(2).to_string())

"""Reads watchlist.csv, pulls live price via OpenBB, flags any level crossed."""
import sys, os
sys.path.insert(0, "/Users/acebless/Documents/WORLDWIDEBRO-OS/06-TECHNOLOGY/repositories/OpenBB/.venv/lib/python3.12/site-packages")
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from openbb import obb

wl = pd.read_csv(os.path.join(os.path.dirname(__file__), "watchlist.csv"))

for _, row in wl.iterrows():
    t = row["ticker"]
    df = obb.equity.price.historical(t, provider="yfinance", interval="5m", start_date=pd.Timestamp.today().strftime("%Y-%m-%d")).to_df().reset_index()
    if df.empty:
        print(f"{t}: no data")
        continue
    last = df.iloc[-1]
    price, ts = last["close"], last["date"]

    alerts = []
    if pd.notna(row.get("resistance2")) and price >= row["resistance2"]:
        alerts.append(f"ABOVE resistance2 ({row['resistance2']})")
    elif pd.notna(row.get("resistance1")) and price >= row["resistance1"]:
        alerts.append(f"AT/ABOVE resistance1 ({row['resistance1']})")
    if pd.notna(row.get("support2")) and price <= row["support2"]:
        alerts.append(f"BELOW support2 ({row['support2']})")
    elif pd.notna(row.get("support1")) and price <= row["support1"]:
        alerts.append(f"AT/BELOW support1 ({row['support1']})")

    flag = " | ".join(alerts) if alerts else "inside range"
    print(f"{t:6s} {price:8.2f} @ {ts}  ->  {flag}   ({row['notes']})")

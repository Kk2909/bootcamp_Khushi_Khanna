from __future__ import annotations
from pathlib import Path
import os
from datetime import datetime, timedelta

import pandas as pd
from dotenv import load_dotenv
import yfinance as yf

REPO_ROOT = Path(__file__).resolve().parents[3]
ENV_PATH = REPO_ROOT / "homework" / "homework4" / ".env"
RAW_DIR = REPO_ROOT / "homework" / "homework4" / "data" / "raw"
load_dotenv(ENV_PATH)

ticker = os.getenv("TICKER", "AAPL").strip()
RAW_DIR.mkdir(parents=True, exist_ok=True)

def ts() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M")

def validate_df(df: pd.DataFrame) -> None:
    need = {"Open","High","Low","Close","Volume"}
    missing = need - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}. Got: {list(df.columns)}")
    if len(df) < 10:
        raise ValueError("Too few rows")
    if (df[["Open","High","Low","Close","Volume"]].isna().mean() > 0.2).any():
        raise ValueError("Too many NAs")

def main() -> None:
    start = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")
    end = datetime.today().strftime("%Y-%m-%d")

    # Use history() which usually returns clean single-level columns
    tk = yf.Ticker(ticker)
    df = tk.history(start=start, end=end, interval="1d", actions=False, auto_adjust=False)

    if df is None or df.empty:
        raise RuntimeError("No data returned from yfinance history().")

    # Put Date as a normal column
    df = df.reset_index()

    # Standardize column names (some envs use lower/underscores)
    ren = {c: c.title().replace("_", " ") for c in df.columns}
    df = df.rename(columns=ren)

    # Some builds return 'Stock Splits' / 'Dividends' — drop if present
    drop_cols = [c for c in ["Dividends","Stock Splits","Capital Gains"] if c in df.columns]
    if drop_cols:
        df = df.drop(columns=drop_cols)

    # Ensure the five needed columns exist; if an 'Adj Close' exists we keep it but don't require it
    # If Date is named something else, normalize to 'Date'
    if "Date" not in df.columns:
        # assume first column is date-like
        first = df.columns[0]
        df = df.rename(columns={first: "Date"})

    # Final cleanups
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.strftime("%Y-%m-%d")

    # DEBUG: print columns once to help if it fails again
    print("Columns seen:", list(df.columns))

    validate_df(df)

    out = RAW_DIR / f"api_prices_yfinance_{ticker}_{ts()}.csv"
    df.to_csv(out, index=False)
    print(f"Saved → {out} | rows={len(df)}, cols={df.shape[1]}")

if __name__ == "__main__":
    main()

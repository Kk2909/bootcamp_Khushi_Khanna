from __future__ import annotations
from pathlib import Path
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Paths
REPO_ROOT = Path(__file__).resolve().parents[3]
RAW_DIR = REPO_ROOT / "homework" / "homework4" / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def ts() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M")

def fetch_html(url: str) -> str:
    r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return r.text

def parse_table(html: str) -> pd.DataFrame:
    soup = BeautifulSoup(html, "html.parser")
    # Find the first table with class 'wikitable'
    table = soup.find("table", {"class": "wikitable"})
    if table is None:
        raise RuntimeError("Could not find a table with class 'wikitable' on the page.")

    # Extract headers
    headers = []
    for th in table.find_all("th"):
        headers.append(th.get_text(strip=True))

    # Extract rows
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all(["td","th"])]
        if cells:
            rows.append(cells)

    # Build DataFrame and align columns
    df = pd.DataFrame(rows)
    # Trim/align to header length if mismatch
    if len(headers) and df.shape[1] >= len(headers):
        df = df.iloc[:, :len(headers)]
        df.columns = headers
    elif len(headers) and df.shape[1] < len(headers):
        # pad missing columns
        for _ in range(len(headers) - df.shape[1]):
            df[df.shape[1]] = None
        df.columns = headers

    return df

def validate(df: pd.DataFrame) -> None:
    # Basic validation for a generic company table
    if len(df) < 50:
        raise ValueError(f"Too few rows: {len(df)}")
    if df.isna().mean().mean() > 0.5:
        raise ValueError("Table looks too sparse (many missing values).")

def main() -> None:
    html = fetch_html(URL)
    df = parse_table(html)
    validate(df)
    out = RAW_DIR / f"scrape_wikipedia_sp500_{ts()}.csv"
    df.to_csv(out, index=False)
    print(f"Saved → {out} | rows={len(df)}, cols={df.shape[1]}")

if __name__ == "__main__":
    main()

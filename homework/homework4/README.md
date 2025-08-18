# Stage 04 — Data Acquisition & Ingestion

## Sources
- API: AAPL daily OHLCV via yfinance (last ~1 year) → data/raw/api_prices_yfinance_AAPL_<timestamp>.csv
- Scrape: S&P 500 companies (Wikipedia) → data/raw/scrape_wikipedia_sp500_<timestamp>.csv

## Validation
- API: required columns (Date, Open, High, Low, Close, Volume), >= 10 rows, <20% NAs.
- Scrape: >= 50 rows, headers present, table not sparse.

## Config
- .env (local): TICKER, API_SOURCE, and data dirs.
- .env.example (committed): safe template.

## Notes / Risks
- Websites/tables may change structure.
- API responses can change; script prints columns if mismatch.

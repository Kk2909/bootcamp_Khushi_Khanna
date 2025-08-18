

## Utilities
- `write_df(df, path)`: writes `.csv` or `.parquet` (requires `pyarrow` for Parquet)
- `read_df(path)`: reads `.csv` or `.parquet`

## Validation Performed
- Shapes match between original, CSV, and Parquet
- Required columns present: `date`, `revenue`, `risk_score`
- Dtype check printed in notebook

## SQLite (Optional for practice)
Created `data/bootcamp_stage5.db` with table `metrics (id, date, revenue, risk_score)` and ran CRUD + aggregations to generate a DataFrame for saving.

## How to Reproduce
1. Create `.env` with `DATA_DIR_RAW` and `DATA_DIR_PROCESSED`
2. Run `notebooks/05_data_storage.ipynb` top to bottom
3. Outputs:
   - `data/raw/metrics_<YYYYMMDD-HHMM>.csv`
   - `data/processed/metrics_<YYYYMMDD-HHMM>.parquet`

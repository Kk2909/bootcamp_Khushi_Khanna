# Stage 06 -Data Preprocessing

## Cleaning Strategy

**Dataset:** `data/raw/data.csv`  
**Goal:** Create a recurrsive, cleaned dataset for analysis & modeling.

### Steps Applied
1. **fill_missing_median** → filled numeric NaNs with column median.  
2. **drop_missing** → dropped columns with more than 50% missing values.  
3. **normalize_data** → standardized numeric columns (mean = 0, std = 1).  
4. **date conversion** → converted `date` column to proper datetime.

### Outputs
- Human-readable CSV: `data/processed/clean_no_scale_YYYYMMDD-HHMM.csv`  
- Modeling-ready Parquet: `data/processed/clean_scaled_YYYYMMDD-HHMM.parquet`

### Assumptions & Tradeoffs
- **Median** chosen over mean for robustness to outliers.  
- **Threshold = 0.5** ensures we keep columns unless they’re mostly missing.  
- Scaling applied **only to numeric features**, categoricals left as-is.

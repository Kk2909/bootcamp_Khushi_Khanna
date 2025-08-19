# cleaning
import pandas as pd
from sklearn.preprocessing import StandardScaler

def fill_missing_median(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill NaNs in numeric columns with the column median.
    Non-numeric columns are left unchanged.
    """
    out = df.copy()
    for c in out.select_dtypes(include="number").columns:
        out[c] = out[c].fillna(out[c].median())
    return out

def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drop columns with > threshold fraction of missing values.
    Example: threshold=0.5 drops columns with more than 50% NaNs.
    """
    out = df.copy()
    min_non_na = int((1 - threshold) * len(out))
    return out.dropna(axis=1, thresh=min_non_na)

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize numeric columns to mean 0, std 1.
    Non-numeric columns unchanged.
    """
    out = df.copy()
    num_cols = out.select_dtypes(include="number").columns
    if len(num_cols) == 0:
        return out
    scaler = StandardScaler()
    out[num_cols] = scaler.fit_transform(out[num_cols])
    return out

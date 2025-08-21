# src/cleaning.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def fill_missing_median(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for c in cols:
        if c in out.columns:
            out[c] = out[c].fillna(out[c].median())
    return out

def drop_missing(df: pd.DataFrame, cols: list[str], thresh: float = 0.5) -> pd.DataFrame:
    """Drop rows where the fraction of NA among `cols` exceeds `thresh`.""" 
    out = df.copy()
    frac_na = out[cols].isna().mean(axis=1)
    return out.loc[frac_na <= thresh].reset_index(drop=True)

def normalize_data(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    scaler = StandardScaler()
    out[cols] = scaler.fit_transform(out[cols])
    return out

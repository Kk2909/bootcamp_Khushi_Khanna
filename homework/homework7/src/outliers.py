# src/outliers
from __future__ import annotations
import numpy as np
import pandas as pd

def detect_outliers_iqr(s: pd.Series, k: float = 1.5) -> tuple[pd.Series, float, float]:
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    lo, hi = q1 - k * iqr, q3 + k * iqr
    mask = (s < lo) | (s > hi)
    return mask.fillna(False), float(lo), float(hi)

def detect_outliers_zscore(s: pd.Series, threshold: float = 3.0) -> tuple[pd.Series, pd.Series]:
    mu, sigma = s.mean(), s.std(ddof=0)
    if sigma == 0 or pd.isna(sigma):
        z = pd.Series(np.nan, index=s.index)
        return pd.Series(False, index=s.index), z
    z = (s - mu) / sigma
    return (z.abs() > threshold).fillna(False), z

def winsorize_series(s: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    lo, hi = s.quantile(lower), s.quantile(upper)
    return s.clip(lower=lo, upper=hi)

from __future__ import annotations
import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return tidy summary statistics for numeric columns.
    """
    stats = df.describe().T  # transpose so rows are columns
    stats["missing"] = df.isna().sum()
    return stats

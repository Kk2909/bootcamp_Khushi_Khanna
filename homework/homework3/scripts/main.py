"""
Run me from the project ROOT like:
    python scripts\main.py
"""
import pandas as pd
from src.utils import get_summary_stats

df = pd.read_csv("data/example_numbers.csv")
print(get_summary_stats(df))

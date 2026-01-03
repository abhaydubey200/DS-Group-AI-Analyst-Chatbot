# data_quality/missing_values.py

import pandas as pd

def analyze_missing_values(df: pd.DataFrame) -> dict:
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()

    missing_percentage = (
        (missing_cells / total_cells) * 100 if total_cells > 0 else 0
    )

    return {
        "missing_cells": int(missing_cells),
        "missing_percentage": round(missing_percentage, 2)
    }

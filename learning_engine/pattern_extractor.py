# learning_engine/pattern_extractor.py

import pandas as pd


def extract_data_pattern(df: pd.DataFrame) -> dict:
    """
    Extract abstract learning patterns (NO raw data).
    """

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    pattern = {
        "columns": list(df.columns),
        "numeric_columns": numeric_cols,
        "row_count": df.shape[0],
        "column_count": df.shape[1],
        "distributions": {}
    }

    for col in numeric_cols:
        pattern["distributions"][col] = {
            "mean": float(df[col].mean()),
            "std": float(df[col].std()),
            "min": float(df[col].min()),
            "max": float(df[col].max())
        }

    return pattern

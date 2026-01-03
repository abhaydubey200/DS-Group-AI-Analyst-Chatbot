# data_engine/schema_detector.py
import pandas as pd

def detect_schema(df: pd.DataFrame):
    schema = {}

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            dtype = "numeric"
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            dtype = "datetime"
        else:
            dtype = "categorical"

        schema[col] = {
            "type": dtype,
            "missing_pct": round(df[col].isnull().mean() * 100, 2),
            "unique_values": df[col].nunique()
        }

    return schema

# data_quality/freshness.py

import pandas as pd
from datetime import datetime

def check_data_freshness(df: pd.DataFrame, date_column: str) -> dict:
    if date_column not in df.columns:
        return {
            "freshness_days": None,
            "status": "date_column_missing"
        }

    latest_date = pd.to_datetime(df[date_column]).max()
    days_old = (datetime.now() - latest_date).days

    status = "fresh" if days_old <= 30 else "stale"

    return {
        "freshness_days": days_old,
        "status": status
    }

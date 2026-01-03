# data_quality/volume_check.py

import pandas as pd

def check_data_volume(df: pd.DataFrame) -> dict:
    rows = df.shape[0]

    if rows < 500:
        status = "low"
    elif rows < 5000:
        status = "medium"
    else:
        status = "high"

    return {
        "row_count": rows,
        "volume_status": status
    }

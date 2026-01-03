# forecasting_engine/time_series_preparer.py

import pandas as pd


def prepare_time_series(df: pd.DataFrame, date_col: str, target_col: str):
    """
    Convert raw data into clean monthly time series.
    """

    ts = df.copy()
    ts[date_col] = pd.to_datetime(ts[date_col])

    ts = ts.groupby(
        pd.Grouper(key=date_col, freq="M")
    )[target_col].sum().reset_index()

    ts.rename(columns={date_col: "ds", target_col: "y"}, inplace=True)

    ts = ts.sort_values("ds")

    return ts

# forecasting_engine/models.py

import numpy as np
import pandas as pd


def moving_average_forecast(ts: pd.DataFrame, periods: int = 24):
    window = min(6, len(ts))
    avg = ts["y"].rolling(window).mean().iloc[-1]

    future = [avg] * periods

    return future


def linear_trend_forecast(ts: pd.DataFrame, periods: int = 24):
    x = np.arange(len(ts))
    y = ts["y"].values

    coef = np.polyfit(x, y, 1)
    trend = coef[0]

    last = y[-1]
    future = [last + trend * (i + 1) for i in range(periods)]

    return future


def seasonal_naive_forecast(ts: pd.DataFrame, periods: int = 24):
    season = 12
    values = ts["y"].values

    future = [
        values[-season + (i % season)] if len(values) >= season else values[-1]
        for i in range(periods)
    ]

    return future

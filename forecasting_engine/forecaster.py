# forecasting_engine/forecaster.py

import pandas as pd
import numpy as np

from forecasting_engine.time_series_preparer import prepare_time_series
from forecasting_engine.models import (
    moving_average_forecast,
    linear_trend_forecast,
    seasonal_naive_forecast
)
from forecasting_engine.model_selector import select_best_model


MODEL_MAP = {
    "moving_average": moving_average_forecast,
    "linear_trend": linear_trend_forecast,
    "seasonal_naive": seasonal_naive_forecast
}


def generate_forecast(
    df: pd.DataFrame,
    date_col: str,
    target_col: str,
    periods: int = 24
):
    ts = prepare_time_series(df, date_col, target_col)

    model_name, model_scores = select_best_model(ts)
    model_fn = MODEL_MAP[model_name]

    forecast_values = model_fn(ts, periods)

    last_date = ts["ds"].iloc[-1]
    future_dates = pd.date_range(
        start=last_date, periods=periods + 1, freq="M"
    )[1:]

    forecast_df = pd.DataFrame({
        "date": future_dates,
        "forecast": forecast_values
    })

    # Confidence bands (simple statistical range)
    std = ts["y"].std()

    forecast_df["lower_bound"] = forecast_df["forecast"] - 1.5 * std
    forecast_df["upper_bound"] = forecast_df["forecast"] + 1.5 * std

    return {
        "model_used": model_name,
        "model_scores": model_scores,
        "forecast": forecast_df
    }

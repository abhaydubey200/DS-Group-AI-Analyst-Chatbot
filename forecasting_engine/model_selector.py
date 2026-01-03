# forecasting_engine/model_selector.py

import numpy as np
from forecasting_engine.models import (
    moving_average_forecast,
    linear_trend_forecast,
    seasonal_naive_forecast
)


def evaluate_model(actual, predicted):
    return np.mean(np.abs(actual - predicted))


def select_best_model(ts):
    horizon = min(6, len(ts) - 1)
    actual = ts["y"].values[-horizon:]

    models = {
        "moving_average": moving_average_forecast,
        "linear_trend": linear_trend_forecast,
        "seasonal_naive": seasonal_naive_forecast
    }

    scores = {}

    for name, model in models.items():
        pred = model(ts[:-horizon], horizon)
        scores[name] = evaluate_model(actual, pred)

    best_model = min(scores, key=scores.get)

    return best_model, scores

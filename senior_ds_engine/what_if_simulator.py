# senior_ds_engine/what_if_simulator.py

import pandas as pd


class WhatIfSimulator:
    """
    Simulates business scenarios.
    """

    def simulate(self, df: pd.DataFrame, column: str, change_percent: float):

        if column not in df.columns:
            return {}

        base_mean = df[column].mean()
        new_mean = base_mean * (1 + change_percent / 100)

        impact = new_mean - base_mean

        return {
            "metric": column,
            "original_avg": round(base_mean, 2),
            "new_avg": round(new_mean, 2),
            "impact": round(impact, 2),
            "change_percent": change_percent
        }

# scenario_engine/volume_simulator.py

import pandas as pd


def simulate_volume_change(forecast_df: pd.DataFrame, volume_change_pct: float):
    """
    Simulate volume shock impact.
    """

    factor = 1 + (volume_change_pct / 100)

    simulated = forecast_df.copy()
    simulated["simulated_forecast"] = simulated["forecast"] * factor

    return simulated

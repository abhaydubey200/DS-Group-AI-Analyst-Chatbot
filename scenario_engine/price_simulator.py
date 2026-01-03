# scenario_engine/price_simulator.py

import pandas as pd


def simulate_price_change(forecast_df: pd.DataFrame, price_change_pct: float):
    """
    Simulate price change impact on revenue.
    """

    factor = 1 + (price_change_pct / 100)

    simulated = forecast_df.copy()
    simulated["simulated_forecast"] = simulated["forecast"] * factor

    return simulated

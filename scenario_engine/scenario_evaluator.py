# scenario_engine/scenario_evaluator.py

def evaluate_scenario(base_df, simulated_df):
    """
    Compare base vs scenario forecast.
    """

    base_total = base_df["forecast"].sum()
    scenario_total = simulated_df["simulated_forecast"].sum()

    delta = scenario_total - base_total
    delta_pct = (delta / base_total) * 100 if base_total != 0 else 0

    return {
        "base_total": round(base_total, 2),
        "scenario_total": round(scenario_total, 2),
        "impact_value": round(delta, 2),
        "impact_percentage": round(delta_pct, 2)
    }

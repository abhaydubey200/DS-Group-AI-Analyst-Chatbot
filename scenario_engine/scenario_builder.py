# scenario_engine/scenario_builder.py

def build_scenarios():
    """
    Define standard business scenarios.
    """

    return [
        {
            "name": "Price Increase 5%",
            "price_change_pct": 5,
            "volume_change_pct": 0
        },
        {
            "name": "Price Decrease 5%",
            "price_change_pct": -5,
            "volume_change_pct": 0
        },
        {
            "name": "Volume Drop 10%",
            "price_change_pct": 0,
            "volume_change_pct": -10
        },
        {
            "name": "Volume Increase 10%",
            "price_change_pct": 0,
            "volume_change_pct": 10
        },
        {
            "name": "Marketing Boost Scenario",
            "price_change_pct": 0,
            "volume_change_pct": 15
        }
    ]

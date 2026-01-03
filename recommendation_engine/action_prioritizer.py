# recommendation_engine/action_prioritizer.py

PRIORITY_ORDER = {
    "Critical": 3,
    "High": 2,
    "Medium": 1,
    "Low": 0
}

def prioritize_actions(recommendations: list) -> list:
    """
    Rank recommendations by priority and expected impact.
    """

    sorted_actions = sorted(
        recommendations,
        key=lambda x: (
            PRIORITY_ORDER.get(x["priority"], 0),
            x.get("expected_impact", 0)
        ),
        reverse=True
    )

    for idx, action in enumerate(sorted_actions, start=1):
        action["rank"] = idx

    return sorted_actions

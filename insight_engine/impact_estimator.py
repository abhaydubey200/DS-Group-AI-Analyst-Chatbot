# insight_engine/impact_estimator.py

def estimate_business_impact(insight: dict) -> dict:
    """
    Estimate business impact in monetary or operational terms.
    """

    base_impact = 0

    if insight["type"] == "data_quality":
        base_impact = 5_00_000  # ₹5L potential reporting risk

    elif insight["type"] == "confidence_warning":
        base_impact = 10_00_000  # ₹10L strategic risk

    elif insight["type"] == "statistical_summary":
        base_impact = 1_00_000

    impact_score = insight["severity"] * base_impact

    insight["business_impact"] = impact_score
    return insight

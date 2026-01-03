# recommendation_engine/recommendation_generator.py

def generate_recommendations(ranked_insights: list, confidence_score: int) -> list:
    """
    Convert ranked insights into actionable recommendations.
    """

    recommendations = []

    for insight in ranked_insights:
        if insight["visibility"] != "executive":
            continue

        if insight["type"] == "data_quality":
            recommendations.append({
                "action": "Improve data collection and validation processes.",
                "reason": insight["message"],
                "priority": "High",
                "owner": "Data Engineering",
                "expected_impact": insight["business_impact"]
            })

        elif insight["type"] == "confidence_warning":
            recommendations.append({
                "action": "Avoid strategic decisions based on this analysis alone.",
                "reason": "Low confidence detected due to data quality issues.",
                "priority": "Critical",
                "owner": "Business Leadership",
                "expected_impact": insight["business_impact"]
            })

        elif insight["type"] == "statistical_summary":
            recommendations.append({
                "action": "Use summary metrics to benchmark regional performance.",
                "reason": "Baseline metrics are now available.",
                "priority": "Medium",
                "owner": "Sales Analytics",
                "expected_impact": insight["business_impact"]
            })

    # Confidence-aware recommendation
    if confidence_score < 60:
        recommendations.append({
            "action": "Trigger data audit before running advanced forecasting.",
            "reason": "Overall confidence score is low.",
            "priority": "Critical",
            "owner": "Data Governance",
            "expected_impact": 15_00_000
        })

    return recommendations

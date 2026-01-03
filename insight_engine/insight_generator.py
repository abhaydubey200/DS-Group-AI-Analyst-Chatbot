# insight_engine/insight_generator.py

def generate_insights(context_results: dict) -> list:
    """
    Convert raw analysis results into structured insights.
    """

    insights = []

    summary = context_results.get("summary")
    if summary:
        insights.append({
            "type": "statistical_summary",
            "message": "Statistical summary generated for selected dataset.",
            "severity": 1
        })

    data_quality = context_results.get("data_quality")
    if data_quality:
        missing_pct = data_quality["missing"]["missing_percentage"]
        if missing_pct > 10:
            insights.append({
                "type": "data_quality",
                "message": f"High missing values detected ({missing_pct}%).",
                "severity": 3
            })

    confidence = context_results.get("confidence_score", 100)
    if confidence < 60:
        insights.append({
            "type": "confidence_warning",
            "message": "Low confidence in analysis due to data quality issues.",
            "severity": 4
        })

    return insights

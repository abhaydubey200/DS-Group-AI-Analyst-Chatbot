# insight_engine/insight_ranker.py

def rank_insights(insights: list) -> list:
    """
    Rank insights by severity + business impact.
    """

    ranked = sorted(
        insights,
        key=lambda x: (x.get("severity", 0), x.get("business_impact", 0)),
        reverse=True
    )

    for i, insight in enumerate(ranked, start=1):
        insight["rank"] = i

        if insight["rank"] <= 3:
            insight["visibility"] = "executive"
        else:
            insight["visibility"] = "normal"

    return ranked

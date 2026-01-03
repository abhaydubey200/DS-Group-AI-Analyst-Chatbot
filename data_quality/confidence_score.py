# data_quality/confidence_score.py

def calculate_confidence_score(
    missing_percentage: float,
    outlier_count: int,
    freshness_days: int | None,
    volume_status: str
) -> int:

    score = 100

    # Missing penalty
    if missing_percentage > 20:
        score -= 30
    elif missing_percentage > 10:
        score -= 20
    elif missing_percentage > 5:
        score -= 10

    # Outlier penalty
    if outlier_count > 100:
        score -= 20
    elif outlier_count > 50:
        score -= 10

    # Freshness penalty
    if freshness_days is not None:
        if freshness_days > 90:
            score -= 20
        elif freshness_days > 30:
            score -= 10

    # Volume penalty
    if volume_status == "low":
        score -= 20
    elif volume_status == "medium":
        score -= 10

    return max(score, 0)

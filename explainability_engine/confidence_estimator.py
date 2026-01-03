# explainability_engine/confidence_estimator.py

def estimate_confidence(result: dict) -> float:
    """
    Simple confidence estimation based on data availability.
    """

    if not result:
        return 0.0

    confidence = 0.75

    if "forecast" in result:
        confidence += 0.1

    if "trend" in result:
        confidence += 0.05

    return min(confidence, 0.95)

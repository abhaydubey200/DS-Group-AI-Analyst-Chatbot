# ai_engine/intent_detector.py

def detect_intent(user_query: str) -> dict:
    """
    Detect high-level intent from user query.
    """

    query = user_query.lower()

    if any(word in query for word in ["why", "reason", "cause"]):
        intent = "root_cause_analysis"

    elif any(word in query for word in ["predict", "forecast", "future"]):
        intent = "forecasting"

    elif any(word in query for word in ["trend", "growth", "change"]):
        intent = "trend_analysis"

    elif any(word in query for word in ["compare", "vs", "difference"]):
        intent = "comparison"

    else:
        intent = "general_analysis"

    return {
        "intent": intent,
        "confidence": 0.85  # placeholder, will be dynamic later
    }

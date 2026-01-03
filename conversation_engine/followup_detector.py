# conversation_engine/followup_detector.py

def is_followup_query(user_query: str) -> bool:
    """
    Detect whether query depends on previous context.
    """

    followup_keywords = [
        "compare", "same", "previous", "earlier",
        "last", "again", "what about", "and"
    ]

    query = user_query.lower()

    return any(word in query for word in followup_keywords)

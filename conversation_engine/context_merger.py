# conversation_engine/context_merger.py

def merge_entities(current: dict, previous: dict) -> dict:
    """
    Fill missing entities using previous context.
    """

    merged = current.copy()

    for key, value in previous.items():
        if merged.get(key) is None:
            merged[key] = value

    return merged

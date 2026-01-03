# ai_engine/entity_extractor.py

import re

def extract_entities(user_query: str) -> dict:
    """
    Extract entities like metric, region, time, product.
    Rule-based for now (LLM-free & in-house).
    """

    query = user_query.lower()

    entities = {
        "metric": None,
        "region": None,
        "time_period": None,
        "product": None
    }

    # Metric detection
    if "sales" in query:
        entities["metric"] = "sales"
    elif "revenue" in query:
        entities["metric"] = "revenue"
    elif "profit" in query:
        entities["metric"] = "profit"

    # Region detection
    regions = ["north", "south", "east", "west"]
    for region in regions:
        if region in query:
            entities["region"] = region.capitalize()

    # Time detection
    time_patterns = {
        "q1": "Q1",
        "q2": "Q2",
        "q3": "Q3",
        "q4": "Q4"
    }

    for key, value in time_patterns.items():
        if key in query:
            entities["time_period"] = value

    year_match = re.search(r"(20\d{2})", query)
    if year_match:
        entities["time_period"] = year_match.group(1)

    return entities

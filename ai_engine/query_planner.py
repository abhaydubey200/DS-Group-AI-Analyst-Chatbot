# ai_engine/query_planner.py

from conversation_engine.followup_detector import is_followup_query
from conversation_engine.context_merger import merge_entities


def build_analysis_plan(intent: dict, entities: dict, memory=None) -> dict:
    """
    Convert intent + entities into an executable analysis plan.
    """

    if memory and is_followup_query(intent.get("raw_query", "")):
        entities = merge_entities(
            entities,
            memory.get_last_entities()
        )

    plan = {
        "analysis_type": intent["intent"],
        "steps": [],
        "entities": entities
    }

    if intent["intent"] == "forecasting":
        plan["steps"] = [
            "load_dataset",
            "metric_selection",
            "time_series_preparation",
            "forecast_execution"
        ]

    elif intent["intent"] == "comparison":
        plan["steps"] = [
            "load_dataset",
            "filter_by_region",
            "metric_comparison"
        ]

    else:
        plan["steps"] = [
            "load_dataset",
            "basic_analysis"
        ]

    return plan

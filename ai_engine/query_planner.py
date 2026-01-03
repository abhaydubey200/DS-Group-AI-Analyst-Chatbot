# ai_engine/query_planner.py

def build_analysis_plan(intent: dict, entities: dict) -> dict:
    """
    Convert intent + entities into an executable analysis plan.
    """

    plan = {
        "analysis_type": intent["intent"],
        "steps": []
    }

    if intent["intent"] == "root_cause_analysis":
        plan["steps"] = [
            "load_dataset",
            "filter_by_time",
            "filter_by_region",
            "metric_trend_analysis",
            "contribution_analysis",
            "variance_analysis",
            "generate_insights"
        ]

    elif intent["intent"] == "forecasting":
        plan["steps"] = [
            "load_dataset",
            "metric_selection",
            "time_series_preparation",
            "model_selection",
            "forecast_execution",
            "confidence_estimation"
        ]

    elif intent["intent"] == "trend_analysis":
        plan["steps"] = [
            "load_dataset",
            "metric_selection",
            "time_series_analysis",
            "growth_rate_calculation"
        ]

    elif intent["intent"] == "comparison":
        plan["steps"] = [
            "load_dataset",
            "group_selection",
            "metric_comparison",
            "statistical_test"
        ]

    else:
        plan["steps"] = [
            "load_dataset",
            "basic_analysis",
            "summary_generation"
        ]

    plan["entities"] = entities
    return plan

# execution_engine/step_router.py

def route_step(step_name: str):
    """
    Map plan steps to executor functions
    """

    routing_table = {
        "load_dataset": "execute_load_dataset",
        "filter_by_time": "execute_filter_by_time",
        "filter_by_region": "execute_filter_by_region",
        "metric_trend_analysis": "execute_metric_trend",
        "contribution_analysis": "execute_contribution",
        "variance_analysis": "execute_variance",
        "generate_insights": "execute_generate_insights",
        "basic_analysis": "execute_basic_analysis"
    }

    return routing_table.get(step_name)

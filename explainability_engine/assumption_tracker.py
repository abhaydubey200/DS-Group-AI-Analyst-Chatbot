# explainability_engine/assumption_tracker.py

def get_assumptions(analysis_type: str) -> list:
    """
    Returns assumptions made by AI during analysis.
    """

    assumptions = {
        "forecasting": [
            "Historical trends will continue",
            "No major external disruptions",
            "Seasonality remains stable"
        ],
        "comparison": [
            "Same metric definition across regions",
            "Data quality is consistent"
        ],
        "root_cause": [
            "Correlation indicates potential influence",
            "Outliers are valid observations"
        ]
    }

    return assumptions.get(analysis_type, ["Standard analytical assumptions applied"])

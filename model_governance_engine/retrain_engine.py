# model_governance_engine/retrain_engine.py

import pandas as pd
from model_governance_engine.model_versioning import ModelVersioning
from forecasting_engine.forecaster import generate_forecast

class AutoRetrainEngine:
    """
    Handles automatic retraining when drift is detected or new data is available.
    """

    def __init__(self):
        self.versioning = ModelVersioning()

    def retrain_forecast_model(self, new_data: pd.DataFrame, model_name: str, date_col="Date", target_col="Sales"):
        # Increment model version
        version = self.versioning.increment_version(model_name)

        # Generate forecast (placeholder for actual retraining logic)
        forecast_result = generate_forecast(new_data, date_col, target_col)

        return {
            "model_name": model_name,
            "version": version,
            "forecast_result": forecast_result
        }

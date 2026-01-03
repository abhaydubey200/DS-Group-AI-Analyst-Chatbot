# execution_engine/executor.py

import pandas as pd

from execution_engine.context import ExecutionContext
from execution_engine.step_router import route_step

from forecasting_engine.forecaster import generate_forecast

from insight_engine.insight_generator import generate_insights
from insight_engine.impact_estimator import estimate_business_impact
from insight_engine.insight_ranker import rank_insights

from recommendation_engine.recommendation_generator import generate_recommendations
from recommendation_engine.action_prioritizer import prioritize_actions


class PlanExecutor:

    def __init__(self, dataframe: pd.DataFrame, entities: dict):
        self.context = ExecutionContext()
        self.context.set_dataset(dataframe)
        self.context.entities = entities

    def execute(self, plan: dict) -> dict:
        for step in plan["steps"]:
            handler_name = route_step(step)
            if handler_name:
                handler = getattr(self, handler_name, None)
                if handler:
                    handler()

        if plan["analysis_type"] == "forecasting":
            self.execute_forecasting()

        self.execute_insight_pipeline()
        self.execute_recommendation_pipeline()

        return self.context.results

    # ---------------- FORECASTING ----------------

    def execute_forecasting(self):
        df = self.context.filtered_dataset

        forecast_result = generate_forecast(
            df,
            date_col="Date",
            target_col=self.context.entities.get("metric", "Sales")
        )

        self.context.add_result("forecast", forecast_result)

    # ---------------- INSIGHTS ----------------

    def execute_insight_pipeline(self):
        insights = generate_insights(self.context.results)
        insights = [estimate_business_impact(i) for i in insights]
        self.context.add_result("ranked_insights", rank_insights(insights))

    # ---------------- RECOMMENDATIONS ----------------

    def execute_recommendation_pipeline(self):
        recs = generate_recommendations(
            self.context.results.get("ranked_insights", []),
            self.context.results.get("confidence_score", 100)
        )
        self.context.add_result("recommended_actions", prioritize_actions(recs))

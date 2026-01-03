# execution_engine/executor.py

import pandas as pd

from execution_engine.context import ExecutionContext
from execution_engine.step_router import route_step

from forecasting_engine.forecaster import generate_forecast

from scenario_engine.scenario_builder import build_scenarios
from scenario_engine.price_simulator import simulate_price_change
from scenario_engine.volume_simulator import simulate_volume_change
from scenario_engine.scenario_evaluator import evaluate_scenario

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
            self.execute_scenarios()

        self.execute_insight_pipeline()
        self.execute_recommendation_pipeline()

        return self.context.results

    # ---------------- FORECAST ----------------

    def execute_forecasting(self):
        df = self.context.filtered_dataset

        forecast_result = generate_forecast(
            df,
            date_col="Date",
            target_col=self.context.entities.get("metric", "Sales")
        )

        self.context.add_result("forecast", forecast_result)

    # ---------------- SCENARIOS ----------------

    def execute_scenarios(self):
        forecast = self.context.results.get("forecast")
        base_df = forecast["forecast"]

        scenarios = build_scenarios()
        scenario_results = []

        for scenario in scenarios:
            simulated_df = base_df.copy()

            if scenario["price_change_pct"] != 0:
                simulated_df = simulate_price_change(
                    base_df, scenario["price_change_pct"]
                )

            if scenario["volume_change_pct"] != 0:
                simulated_df = simulate_volume_change(
                    base_df, scenario["volume_change_pct"]
                )

            evaluation = evaluate_scenario(base_df, simulated_df)

            scenario_results.append({
                "scenario": scenario["name"],
                "details": scenario,
                "impact": evaluation
            })

        self.context.add_result("scenarios", scenario_results)

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

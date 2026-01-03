# execution_engine/executor.py

import pandas as pd

from execution_engine.context import ExecutionContext
from execution_engine.step_router import route_step

from data_quality.missing_values import analyze_missing_values
from data_quality.outlier_detection import detect_outliers_iqr
from data_quality.freshness import check_data_freshness
from data_quality.volume_check import check_data_volume
from data_quality.confidence_score import calculate_confidence_score

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

        self.execute_data_quality_check()
        self.execute_insight_pipeline()
        self.execute_recommendation_pipeline()

        return {
            "results": self.context.results,
            "insights": self.context.results.get("ranked_insights"),
            "recommendations": self.context.results.get("recommended_actions"),
            "confidence": self.context.results.get("confidence_score"),
            "logs": self.context.logs
        }

    # ---------------- BASIC ----------------

    def execute_load_dataset(self):
        self.context.log("Dataset already loaded")

    def execute_filter_by_time(self):
        df = self.context.filtered_dataset
        time_entity = self.context.entities.get("time_period")

        if time_entity and "Quarter" in df.columns:
            self.context.update_filtered_dataset(
                df[df["Quarter"] == time_entity]
            )

    def execute_filter_by_region(self):
        df = self.context.filtered_dataset
        region = self.context.entities.get("region")

        if region and "Region" in df.columns:
            self.context.update_filtered_dataset(
                df[df["Region"] == region]
            )

    def execute_basic_analysis(self):
        df = self.context.filtered_dataset
        self.context.add_result("summary", df.describe().to_dict())

    # ---------------- DATA QUALITY ----------------

    def execute_data_quality_check(self):
        df = self.context.filtered_dataset

        missing = analyze_missing_values(df)
        outliers = detect_outliers_iqr(df)
        volume = check_data_volume(df)
        freshness = check_data_freshness(df, date_column="Date")

        total_outliers = sum(outliers.values())

        confidence = calculate_confidence_score(
            missing_percentage=missing["missing_percentage"],
            outlier_count=total_outliers,
            freshness_days=freshness.get("freshness_days"),
            volume_status=volume["volume_status"]
        )

        self.context.add_result("data_quality", {
            "missing": missing,
            "outliers": outliers,
            "freshness": freshness,
            "volume": volume
        })

        self.context.add_result("confidence_score", confidence)
        self.context.log(f"Confidence score calculated: {confidence}")

    # ---------------- INSIGHTS ----------------

    def execute_insight_pipeline(self):
        raw_insights = generate_insights(self.context.results)

        enriched = []
        for insight in raw_insights:
            enriched.append(estimate_business_impact(insight))

        ranked = rank_insights(enriched)

        self.context.add_result("ranked_insights", ranked)
        self.context.log("Insights ranked and prioritized")

    # ---------------- RECOMMENDATIONS ----------------

    def execute_recommendation_pipeline(self):
        ranked_insights = self.context.results.get("ranked_insights", [])
        confidence = self.context.results.get("confidence_score", 100)

        recommendations = generate_recommendations(
            ranked_insights, confidence
        )

        prioritized = prioritize_actions(recommendations)

        self.context.add_result("recommended_actions", prioritized)
        self.context.log("Recommendations generated and prioritized")

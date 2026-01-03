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

from learning_engine.pattern_extractor import extract_data_pattern
from learning_engine.memory_store import add_pattern
from learning_engine.model_trainer import train_internal_models
from learning_engine.purge_manager import auto_purge_if_needed


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
        self.execute_learning_pipeline()

        return {
            "results": self.context.results,
            "insights": self.context.results.get("ranked_insights"),
            "recommendations": self.context.results.get("recommended_actions"),
            "confidence": self.context.results.get("confidence_score"),
            "learning_status": self.context.results.get("learning_status"),
            "logs": self.context.logs
        }

    # ---------------- BASIC ----------------

    def execute_load_dataset(self):
        self.context.log("Dataset already loaded")

    def execute_filter_by_time(self):
        df = self.context.filtered_dataset
        time_entity = self.context.entities.get("time_period")

        if time_entity and "Quarter" in df.columns:
            self.context.update_filtered_dataset(df[df["Quarter"] == time_entity])

    def execute_filter_by_region(self):
        df = self.context.filtered_dataset
        region = self.context.entities.get("region")

        if region and "Region" in df.columns:
            self.context.update_filtered_dataset(df[df["Region"] == region])

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

        confidence = calculate_confidence_score(
            missing["missing_percentage"],
            sum(outliers.values()),
            freshness.get("freshness_days"),
            volume["volume_status"]
        )

        self.context.add_result("confidence_score", confidence)

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

    # ---------------- LEARNING ----------------

    def execute_learning_pipeline(self):
        df = self.context.filtered_dataset

        pattern = extract_data_pattern(df)
        added = add_pattern(pattern)

        training_status = train_internal_models()
        purged = auto_purge_if_needed()

        self.context.add_result("learning_status", {
            "pattern_added": added,
            "training": training_status,
            "auto_purged": purged
        })

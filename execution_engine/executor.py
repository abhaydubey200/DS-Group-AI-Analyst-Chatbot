# execution_engine/executor.py

from explainability_engine.explanation_generator import ExplanationGenerator
from explainability_engine.assumption_tracker import get_assumptions
from explainability_engine.confidence_estimator import estimate_confidence

from senior_ds_engine.hypothesis_engine import HypothesisEngine
from senior_ds_engine.feature_importance_engine import FeatureImportanceEngine
from senior_ds_engine.what_if_simulator import WhatIfSimulator


class PlanExecutor:

    def __init__(self, df, entities):
        self.df = df
        self.entities = entities
        self.explainer = ExplanationGenerator()

        self.hypothesis_engine = HypothesisEngine()
        self.feature_engine = FeatureImportanceEngine()
        self.whatif_engine = WhatIfSimulator()

    def execute(self, plan: dict) -> dict:

        result = {
            "summary": "Analysis completed successfully"
        }

        # Senior Data Scientist Logic
        if plan["analysis_type"] == "comparison":
            numeric_cols = self.df.select_dtypes(include="number").columns
            if len(numeric_cols) >= 2:
                group_a = self.df[numeric_cols[0]]
                group_b = self.df[numeric_cols[1]]
                result["hypothesis_test"] = self.hypothesis_engine.run_t_test(
                    group_a, group_b
                )

        if plan["analysis_type"] in ["forecasting", "root_cause"]:
            numeric_cols = self.df.select_dtypes(include="number").columns
            if len(numeric_cols) > 1:
                result["feature_importance"] = self.feature_engine.calculate(
                    self.df, numeric_cols[0]
                )

        if "what_if" in plan["analysis_type"]:
            numeric_cols = self.df.select_dtypes(include="number").columns
            if numeric_cols.any():
                result["what_if"] = self.whatif_engine.simulate(
                    self.df, numeric_cols[0], 10
                )

        explanation = self.explainer.generate(plan, result)
        assumptions = get_assumptions(plan["analysis_type"])
        confidence = estimate_confidence(result)

        return {
            "result": result,
            "explanation": explanation,
            "assumptions": assumptions,
            "confidence_score": confidence
        }

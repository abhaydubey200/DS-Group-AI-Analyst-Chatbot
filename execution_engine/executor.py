# execution_engine/executor.py

from explainability_engine.explanation_generator import ExplanationGenerator
from explainability_engine.assumption_tracker import get_assumptions
from explainability_engine.confidence_estimator import estimate_confidence


class PlanExecutor:

    def __init__(self, df, entities):
        self.df = df
        self.entities = entities
        self.explainer = ExplanationGenerator()

    def execute(self, plan: dict) -> dict:

        # Placeholder analytical output
        result = {
            "summary": "Analysis completed successfully",
            "metrics_analyzed": list(self.df.columns)[:3]
        }

        explanation = self.explainer.generate(plan, result)
        assumptions = get_assumptions(plan["analysis_type"])
        confidence = estimate_confidence(result)

        return {
            "result": result,
            "explanation": explanation,
            "assumptions": assumptions,
            "confidence_score": confidence
        }

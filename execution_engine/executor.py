# execution_engine/executor.py

from model_governance_engine.drift_detector import DriftDetector
from model_governance_engine.retrain_engine import AutoRetrainEngine
from model_governance_engine.training_data_manager import TrainingDataManager

from explainability_engine.explanation_generator import ExplanationGenerator
from explainability_engine.assumption_tracker import get_assumptions
from explainability_engine.confidence_estimator import estimate_confidence


class PlanExecutor:

    def __init__(self, df, entities):
        self.df = df
        self.entities = entities
        self.explainer = ExplanationGenerator()
        self.drift_detector = DriftDetector()
        self.retrain_engine = AutoRetrainEngine()
        self.data_manager = TrainingDataManager()

    def execute(self, plan: dict) -> dict:

        # Save new dataset for future training
        dataset_path = self.data_manager.save_dataset(self.df)

        # Detect drift (if previous data exists)
        drift_report = {}
        previous_files = os.listdir(self.data_manager.base_dir)
        if len(previous_files) > 1:
            old_data_path = previous_files[-2]
            old_df = pd.read_csv(os.path.join(self.data_manager.base_dir, old_data_path))
            drift_report = self.drift_detector.detect_drift(old_df, self.df)

            # Auto-retrain if drift detected
            if any(col["drift_detected"] for col in drift_report.values()):
                retrain_result = self.retrain_engine.retrain_forecast_model(self.df, model_name="forecast_model")
            else:
                retrain_result = None
        else:
            retrain_result = self.retrain_engine.retrain_forecast_model(self.df, model_name="forecast_model")

        explanation = self.explainer.generate(plan, {})
        assumptions = get_assumptions(plan["analysis_type"])
        confidence = estimate_confidence({})

        return {
            "dataset_path": dataset_path,
            "drift_report": drift_report,
            "retrain_result": retrain_result,
            "explanation": explanation,
            "assumptions": assumptions,
            "confidence_score": confidence
        }

# model_governance_engine/drift_detector.py

import pandas as pd
from scipy.stats import ks_2samp

class DriftDetector:
    """
    Detects distribution drift between current dataset and historical training dataset.
    """

    def detect_drift(self, old_df: pd.DataFrame, new_df: pd.DataFrame, numeric_cols=None):
        if numeric_cols is None:
            numeric_cols = old_df.select_dtypes(include="number").columns

        drift_report = {}

        for col in numeric_cols:
            if col in new_df.columns:
                stat, p_value = ks_2samp(old_df[col].dropna(), new_df[col].dropna())
                drift_report[col] = {
                    "ks_stat": stat,
                    "p_value": p_value,
                    "drift_detected": p_value < 0.05
                }

        return drift_report

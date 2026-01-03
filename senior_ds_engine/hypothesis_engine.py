# senior_ds_engine/hypothesis_engine.py

import numpy as np
from scipy.stats import ttest_ind


class HypothesisEngine:
    """
    Performs statistical hypothesis testing.
    """

    def run_t_test(self, group_a, group_b, alpha=0.05):
        stat, p_value = ttest_ind(group_a, group_b, nan_policy="omit")

        result = {
            "test": "Two Sample T-Test",
            "p_value": round(float(p_value), 5),
            "significant": p_value < alpha,
            "confidence_level": 1 - alpha
        }

        return result

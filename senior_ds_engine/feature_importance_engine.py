# senior_ds_engine/feature_importance_engine.py

import pandas as pd
from sklearn.ensemble import RandomForestRegressor


class FeatureImportanceEngine:
    """
    Calculates feature importance using tree-based models.
    """

    def calculate(self, df: pd.DataFrame, target: str):

        numeric_df = df.select_dtypes(include="number").dropna()

        if target not in numeric_df.columns:
            return {}

        X = numeric_df.drop(columns=[target])
        y = numeric_df[target]

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)

        importance = dict(
            zip(X.columns, model.feature_importances_)
        )

        return dict(sorted(importance.items(), key=lambda x: x[1], reverse=True))

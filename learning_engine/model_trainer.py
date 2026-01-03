# learning_engine/model_trainer.py

from learning_engine.memory_store import get_patterns


def train_internal_models():
    """
    Simulate internal learning based on accumulated patterns.
    (No ML retraining yet – rule based intelligence upgrade)
    """

    patterns = get_patterns()

    if len(patterns) < 10:
        return {
            "status": "insufficient_data",
            "patterns_used": len(patterns)
        }

    learned_schema = {}
    for p in patterns:
        for col in p["numeric_columns"]:
            learned_schema[col] = learned_schema.get(col, 0) + 1

    return {
        "status": "trained",
        "learned_features": list(learned_schema.keys()),
        "patterns_used": len(patterns)
    }

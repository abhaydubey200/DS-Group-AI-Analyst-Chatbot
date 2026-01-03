# learning_engine/memory_store.py

import time

LEARNING_MEMORY = {
    "patterns": [],
    "created_at": time.time()
}

MAX_PATTERNS = 50  # fixed limit


def add_pattern(pattern: dict):
    if len(LEARNING_MEMORY["patterns"]) >= MAX_PATTERNS:
        return False

    LEARNING_MEMORY["patterns"].append(pattern)
    return True


def get_patterns():
    return LEARNING_MEMORY["patterns"]


def clear_memory():
    LEARNING_MEMORY["patterns"] = []

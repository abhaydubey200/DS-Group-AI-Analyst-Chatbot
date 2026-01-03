# learning_engine/purge_manager.py

import time
from learning_engine.memory_store import clear_memory, LEARNING_MEMORY

MAX_LIFETIME_SECONDS = 60 * 60 * 24  # 24 hours


def auto_purge_if_needed():
    age = time.time() - LEARNING_MEMORY["created_at"]

    if age > MAX_LIFETIME_SECONDS:
        clear_memory()
        LEARNING_MEMORY["created_at"] = time.time()
        return True

    return False

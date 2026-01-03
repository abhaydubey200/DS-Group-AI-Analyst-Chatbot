# data_engine/sample_store.py
import os
import pandas as pd
from datetime import datetime

SAMPLE_DIR = "sample_cache"
MAX_SAMPLES = 5  # limit training samples

os.makedirs(SAMPLE_DIR, exist_ok=True)

def store_sample(df, schema_signature):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{schema_signature}_{timestamp}.csv"
    path = os.path.join(SAMPLE_DIR, filename)

    df.sample(min(500, len(df))).to_csv(path, index=False)
    cleanup_old_samples(schema_signature)

def cleanup_old_samples(schema_signature):
    files = sorted(
        [f for f in os.listdir(SAMPLE_DIR) if f.startswith(schema_signature)],
        reverse=True
    )
    for f in files[MAX_SAMPLES:]:
        os.remove(os.path.join(SAMPLE_DIR, f))

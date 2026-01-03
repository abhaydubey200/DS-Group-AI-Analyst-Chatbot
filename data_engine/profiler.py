# data_engine/profiler.py
def profile_dataset(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "duplicates": int(df.duplicated().sum()),
        "memory_mb": round(df.memory_usage(deep=True).sum() / 1024 / 1024, 2)
    }

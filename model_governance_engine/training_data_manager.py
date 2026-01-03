# model_governance_engine/training_data_manager.py

import os
import pandas as pd
import uuid
import shutil

class TrainingDataManager:
    """
    Stores uploaded datasets for training and manages retention.
    """

    def __init__(self, base_dir="training_data", retention_limit=5):
        self.base_dir = base_dir
        self.retention_limit = retention_limit
        os.makedirs(self.base_dir, exist_ok=True)

    def save_dataset(self, df: pd.DataFrame):
        dataset_id = str(uuid.uuid4())
        path = os.path.join(self.base_dir, f"{dataset_id}.csv")
        df.to_csv(path, index=False)
        self.cleanup_old_data()
        return path

    def cleanup_old_data(self):
        files = sorted(os.listdir(self.base_dir), key=lambda x: os.path.getctime(os.path.join(self.base_dir, x)))
        while len(files) > self.retention_limit:
            os.remove(os.path.join(self.base_dir, files.pop(0)))

# model_governance_engine/model_versioning.py

import json
import os

class ModelVersioning:
    """
    Simple versioning system for all models.
    """

    def __init__(self, version_file="model_versions.json"):
        self.version_file = version_file
        if not os.path.exists(self.version_file):
            with open(self.version_file, "w") as f:
                json.dump({}, f)

    def get_version(self, model_name: str):
        with open(self.version_file) as f:
            versions = json.load(f)
        return versions.get(model_name, 0)

    def increment_version(self, model_name: str):
        with open(self.version_file) as f:
            versions = json.load(f)
        versions[model_name] = versions.get(model_name, 0) + 1
        with open(self.version_file, "w") as f:
            json.dump(versions, f)
        return versions[model_name]

# execution_engine/context.py

class ExecutionContext:
    """
    Maintains state during analysis execution
    """

    def __init__(self):
        self.dataset = None
        self.filtered_dataset = None
        self.entities = {}
        self.results = {}
        self.logs = []

    def log(self, message: str):
        self.logs.append(message)

    def set_dataset(self, df):
        self.dataset = df
        self.filtered_dataset = df
        self.log("Dataset loaded")

    def update_filtered_dataset(self, df):
        self.filtered_dataset = df
        self.log("Dataset filtered")

    def add_result(self, key, value):
        self.results[key] = value
        self.log(f"Result added: {key}")

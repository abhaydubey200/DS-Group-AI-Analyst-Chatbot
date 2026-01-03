# execution_engine/executor.py

import pandas as pd
from execution_engine.context import ExecutionContext
from execution_engine.step_router import route_step


class PlanExecutor:
    """
    Executes an analysis plan step by step
    """

    def __init__(self, dataframe: pd.DataFrame, entities: dict):
        self.context = ExecutionContext()
        self.context.set_dataset(dataframe)
        self.context.entities = entities

    def execute(self, plan: dict) -> dict:
        for step in plan["steps"]:
            handler_name = route_step(step)
            if handler_name:
                handler = getattr(self, handler_name, None)
                if handler:
                    handler()
                else:
                    self.context.log(f"No handler implemented for {step}")
            else:
                self.context.log(f"Unknown step: {step}")

        return {
            "results": self.context.results,
            "logs": self.context.logs
        }

    # ---------------- EXECUTION STEPS ----------------

    def execute_load_dataset(self):
        self.context.log("Dataset already loaded")

    def execute_filter_by_time(self):
        df = self.context.filtered_dataset
        time_entity = self.context.entities.get("time_period")

        if time_entity and "Quarter" in df.columns:
            self.context.update_filtered_dataset(
                df[df["Quarter"] == time_entity]
            )
        self.context.log(f"Filtered by time: {time_entity}")

    def execute_filter_by_region(self):
        df = self.context.filtered_dataset
        region = self.context.entities.get("region")

        if region and "Region" in df.columns:
            self.context.update_filtered_dataset(
                df[df["Region"] == region]
            )
        self.context.log(f"Filtered by region: {region}")

    def execute_metric_trend(self):
        metric = self.context.entities.get("metric", "sales")
        df = self.context.filtered_dataset

        if metric and metric.capitalize() in df.columns:
            trend = df.groupby("Month")[metric.capitalize()].sum()
            self.context.add_result("metric_trend", trend.to_dict())

        self.context.log("Metric trend analysis executed")

    def execute_contribution(self):
        df = self.context.filtered_dataset

        if "Region" in df.columns and "Sales" in df.columns:
            contribution = (
                df.groupby("Region")["Sales"]
                .sum()
                .sort_values(ascending=False)
            )
            self.context.add_result(
                "regional_contribution",
                contribution.to_dict()
            )

        self.context.log("Contribution analysis executed")

    def execute_variance(self):
        df = self.context.filtered_dataset

        if "Sales" in df.columns:
            variance = df["Sales"].var()
            self.context.add_result("sales_variance", variance)

        self.context.log("Variance analysis executed")

    def execute_basic_analysis(self):
        df = self.context.filtered_dataset
        summary = df.describe().to_dict()
        self.context.add_result("summary", summary)
        self.context.log("Basic analysis executed")

    def execute_generate_insights(self):
        insights = []

        if "sales_variance" in self.context.results:
            insights.append(
                "Sales variance is high, indicating instability in performance."
            )

        if "regional_contribution" in self.context.results:
            insights.append(
                "Sales heavily depend on top-performing regions."
            )

        self.context.add_result("insights", insights)
        self.context.log("Insights generated")

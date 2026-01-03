# explainability_engine/explanation_generator.py

class ExplanationGenerator:
    """
    Generates human-readable explanations for AI outputs.
    """

    def generate(self, plan: dict, result: dict) -> str:
        analysis_type = plan.get("analysis_type")
        entities = plan.get("entities", {})

        explanation = f"""
This analysis was performed as a **{analysis_type.upper()} task**.

🔹 Dataset was loaded and filtered based on:
"""

        for key, value in entities.items():
            explanation += f"- {key.replace('_', ' ').title()}: {value}\n"

        explanation += "\n🔹 The AI followed these steps:\n"

        for step in plan.get("steps", []):
            explanation += f"- {step.replace('_', ' ').title()}\n"

        explanation += """
🔹 Final insights were generated using statistical and pattern-based reasoning.

This ensures the output aligns with historical trends and business logic.
"""
        return explanation.strip()

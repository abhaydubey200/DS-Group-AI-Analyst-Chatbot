# ui/components/panels.py

import streamlit as st

def render_explanation_panel(explanation, assumptions, confidence):
    st.subheader("🧠 AI Explanation")
    st.markdown(explanation)
    st.subheader("⚠️ Assumptions")
    st.write(assumptions)
    st.subheader("✅ Confidence Score")
    st.progress(confidence)

def render_senior_ds_panel(result):
    st.subheader("👨‍🔬 Senior Data Scientist Insights")
    if "hypothesis_test" in result:
        st.markdown(f"**Hypothesis Test:** {result['hypothesis_test']}")
    if "feature_importance" in result:
        from ui.components.charts import render_feature_importance_chart
        render_feature_importance_chart(result["feature_importance"])
    if "what_if" in result:
        st.markdown(f"**What-If Simulation:** {result['what_if']}")

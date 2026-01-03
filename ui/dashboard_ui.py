# ui/dashboard_ui.py

import streamlit as st
import pandas as pd
from logging_config import logger

# AI Engine
from ai_engine.intent_detector import detect_intent
from ai_engine.entity_extractor import extract_entities
from ai_engine.query_planner import build_analysis_plan

# Execution Engine
from execution_engine.executor import PlanExecutor

# Conversation Engine
from conversation_engine.conversation_memory import ConversationMemory

# UI Components
from components.charts import render_forecast_chart, render_scenario_chart
from components.filters import render_filters
from components.panels import render_explanation_panel, render_senior_ds_panel

def render_dashboard():
    st.set_page_config(page_title="DS Group AI Analyst", layout="wide")
    st.markdown("<h1 style='text-align:center;color:black;'>🤖 DS Group AI Data Analyst</h1>", unsafe_allow_html=True)

    if "memory" not in st.session_state:
        st.session_state.memory = ConversationMemory()

    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame()

    uploaded_file = st.file_uploader("Upload Dataset (CSV / XLSX)", type=["csv", "xlsx"])

    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                st.session_state.df = pd.read_csv(uploaded_file)
            else:
                st.session_state.df = pd.read_excel(uploaded_file)
            logger.info(f"Dataset uploaded: {uploaded_file.name}")
        except Exception as e:
            st.error("Failed to load dataset.")
            logger.error(f"Dataset loading error: {e}")

    df = st.session_state.df
    if not df.empty:
        render_filters(df, df.columns)
        st.session_state.filtered_df = df

    user_query = st.text_input("Ask a business question or analytical query:")

    if st.button("Analyze") and user_query:
        try:
            intent = detect_intent(user_query)
            intent["raw_query"] = user_query
            entities = extract_entities(user_query)

            plan = build_analysis_plan(intent, entities, memory=st.session_state.memory)
            executor = PlanExecutor(df, plan["entities"])
            output = executor.execute(plan)

            st.session_state.memory.add_turn(user_query, intent, plan["entities"])

            st.subheader("📊 Core Result")
            st.json(output["result"])

            render_explanation_panel(
                output["explanation"],
                output["assumptions"],
                output["confidence_score"]
            )
            render_senior_ds_panel(output["result"])

            if "forecast" in output["result"]:
                render_forecast_chart(output["result"]["forecast"])
            if "scenarios" in output.get("drift_report", {}):
                render_scenario_chart(output.get("drift_report", []))

            logger.info(f"Query processed successfully: {user_query}")

        except Exception as e:
            st.error("Analysis failed. Check logs for details.")
            logger.error(f"Execution error: {e}")

if __name__ == "__main__":
    render_dashboard()

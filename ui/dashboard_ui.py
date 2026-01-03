# ui/dashboard_ui.py

import streamlit as st
import pandas as pd

from ai_engine.intent_detector import detect_intent
from ai_engine.entity_extractor import extract_entities
from ai_engine.query_planner import build_analysis_plan
from execution_engine.executor import PlanExecutor
from conversation_engine.conversation_memory import ConversationMemory


def render_dashboard():

    st.set_page_config(page_title="DS Group AI Analyst", layout="wide")

    if "memory" not in st.session_state:
        st.session_state.memory = ConversationMemory()

    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame()

    st.title("🤖 DS Group AI Data Analyst — Senior Scientist Mode")

    uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "xlsx"])
    if uploaded_file:
        st.session_state.df = pd.read_csv(uploaded_file)

    user_query = st.text_input("Ask a deep analytical question")

    if st.button("Analyze") and user_query:

        intent = detect_intent(user_query)
        intent["raw_query"] = user_query

        entities = extract_entities(user_query)

        plan = build_analysis_plan(
            intent,
            entities,
            memory=st.session_state.memory
        )

        executor = PlanExecutor(
            st.session_state.df,
            plan["entities"]
        )

        output = executor.execute(plan)

        st.session_state.memory.add_turn(
            user_query, intent, plan["entities"]
        )

        st.subheader("📊 Core Result")
        st.json(output["result"])

        st.subheader("🧠 Explanation")
        st.markdown(output["explanation"])

        st.subheader("⚠️ Assumptions")
        st.write(output["assumptions"])

        st.subheader("✅ Confidence")
        st.progress(output["confidence_score"])


if __name__ == "__main__":
    render_dashboard()

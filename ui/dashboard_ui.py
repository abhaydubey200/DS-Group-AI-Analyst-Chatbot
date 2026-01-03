# ui/dashboard_ui.py

import streamlit as st

from ui.components.header import render_header
from ui.components.sidebar import render_sidebar
from ui.components.metric_card import render_metric_card
from ui.components.chat_bubble import render_chat_bubble
from ui.components.analysis_section import render_analysis_section
from ui.components.insight_card import render_insight_card

from ui.charts.sales_trend import sales_trend_chart
from ui.charts.bar_chart import region_contribution_chart
from ui.charts.pie_chart import product_share_chart

from ai_engine.intent_detector import detect_intent
from ai_engine.entity_extractor import extract_entities
from ai_engine.query_planner import build_analysis_plan


def render_dashboard():

    with open("ui/theme/layout.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    render_header("DS Group AI Data Analyst")
    page = render_sidebar()
    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- OVERVIEW ----------------
    if page == "Overview":

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric_card("Total Sales", "₹ 3,45,00,000", delta="5%")
        with col2:
            render_metric_card("Orders", "12,450", delta="2%")
        with col3:
            render_metric_card("Customers", "5,230", delta="-3%")
        with col4:
            render_metric_card("Products", "32", delta="8%")

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(sales_trend_chart(), use_container_width=True)
        with col2:
            st.plotly_chart(region_contribution_chart(), use_container_width=True)

    # ---------------- CHAT AI ----------------
    elif page == "Chat with AI":

        st.markdown("### 🤖 DS Group AI Analyst")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        for chat in st.session_state.chat_history:
            render_chat_bubble(chat["message"], chat["sender"])

        user_input = st.text_input(
            "Ask a business question",
            placeholder="Why did sales drop in North region in Q3?"
        )

        if st.button("Send") and user_input:

            st.session_state.chat_history.append(
                {"message": user_input, "sender": "user"}
            )

            intent = detect_intent(user_input)
            entities = extract_entities(user_input)
            plan = build_analysis_plan(intent, entities)

            ai_response = (
                f"📊 **Intent Detected:** {intent['intent']}\n\n"
                f"🧩 **Entities:** {entities}\n\n"
                f"🛠️ **Planned Steps:**\n- " +
                "\n- ".join(plan["steps"])
            )

            st.session_state.chat_history.append(
                {"message": ai_response, "sender": "ai"}
            )

            st.experimental_rerun()

    # ---------------- DEEP ANALYSIS ----------------
    elif page == "Deep Analysis":

        st.markdown("### 🔍 Deep Analysis")

        col1, col2 = st.columns(2)
        with col1:
            render_analysis_section("Sales Trend")
            st.plotly_chart(sales_trend_chart(), use_container_width=True)

        with col2:
            render_analysis_section("Regional Contribution")
            st.plotly_chart(region_contribution_chart(), use_container_width=True)

        render_insight_card(
            "Key Insight",
            "North region contributed 42% of growth last quarter",
            level="info"
        )

    # ---------------- UPLOAD DATA ----------------
    elif page == "Upload Data":
        from ui.pages.upload_data import render_upload_page
        render_upload_page()

    else:
        st.info("Module under development")


if __name__ == "__main__":
    render_dashboard()

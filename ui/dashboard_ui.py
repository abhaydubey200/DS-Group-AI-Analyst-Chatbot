# ui/dashboard_ui.py

import streamlit as st

# UI Components
from ui.components.header import render_header
from ui.components.sidebar import render_sidebar
from ui.components.metric_card import render_metric_card
from ui.components.chat_bubble import render_chat_bubble
from ui.components.analysis_section import render_analysis_section
from ui.components.insight_card import render_insight_card

# Charts
from ui.charts.sales_trend import sales_trend_chart
from ui.charts.bar_chart import region_contribution_chart
from ui.charts.pie_chart import product_share_chart


# --------------------------------------------------
# Main Dashboard Renderer
# --------------------------------------------------
def render_dashboard():

    # Load global CSS
    with open("ui/theme/layout.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Header
    render_header("DS Group AI Data Analyst")

    # Sidebar Navigation
    page = render_sidebar()
    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------
    # OVERVIEW PAGE
    # --------------------------------------------------
    if page == "Overview":

        # KPI Section
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric_card(
                "Total Sales",
                "₹ 3,45,00,000",
                delta="5%",
                description="Month over Month"
            )
        with col2:
            render_metric_card(
                "Total Orders",
                "12,450",
                delta="2%"
            )
        with col3:
            render_metric_card(
                "Active Customers",
                "5,230",
                delta="-3%"
            )
        with col4:
            render_metric_card(
                "New Products",
                "32",
                delta="8%"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Charts Section
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                sales_trend_chart(),
                use_container_width=True
            )
        with col2:
            st.plotly_chart(
                region_contribution_chart(),
                use_container_width=True
            )

    # --------------------------------------------------
    # CHAT WITH AI (JULIUS-STYLE)
    # --------------------------------------------------
    elif page == "Chat with AI":

        st.markdown("### 🤖 DS Group AI Assistant")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Render chat history
        for chat in st.session_state.chat_history:
            render_chat_bubble(
                chat["message"],
                sender=chat["sender"]
            )

        # Input box
        user_input = st.text_input(
            "Ask a business or data question",
            placeholder="e.g. Why sales dropped in North region?"
        )

        if st.button("Send") and user_input:
            st.session_state.chat_history.append(
                {"message": user_input, "sender": "user"}
            )

            # Placeholder AI response
            ai_response = (
                "📊 Based on preliminary analysis, this will be answered "
                "using trend, variance, and root cause models."
            )

            st.session_state.chat_history.append(
                {"message": ai_response, "sender": "ai"}
            )

            st.experimental_rerun()

    # --------------------------------------------------
    # DEEP ANALYSIS & ROOT CAUSE
    # --------------------------------------------------
    elif page == "Deep Analysis":

        st.markdown("### 🔍 Deep Analysis & Root Cause")

        col1, col2 = st.columns(2)
        with col1:
            render_analysis_section(
                "Sales Trend Analysis",
                "Time-based sales movement and seasonality"
            )
            st.plotly_chart(
                sales_trend_chart(),
                use_container_width=True
            )

        with col2:
            render_analysis_section(
                "Regional Contribution",
                "Identifying growth and decline drivers by region"
            )
            st.plotly_chart(
                region_contribution_chart(),
                use_container_width=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        col3, col4 = st.columns(2)
        with col3:
            render_analysis_section(
                "Product Share Analysis",
                "Revenue contribution by product category"
            )
            st.plotly_chart(
                product_share_chart(),
                use_container_width=True
            )

        with col4:
            render_analysis_section(
                "Customer Behavior",
                "Customer concentration and dependency risk"
            )
            st.info("Customer segmentation model will be connected here.")

        st.markdown("<br>", unsafe_allow_html=True)

        # Insight Cards
        render_insight_card(
            "Key Insight",
            "North region contributed 42% of total revenue growth last quarter.",
            level="info"
        )

        render_insight_card(
            "Risk Alert",
            "Sales decline observed in 3 high-revenue products.",
            level="warning"
        )

        render_insight_card(
            "Critical Observation",
            "Revenue dependency on a single distributor exceeds 38%.",
            level="critical"
        )

    # --------------------------------------------------
    # PLACEHOLDER PAGES
    # --------------------------------------------------
    else:
        st.markdown(
            f"""
            <div style="padding:20px;">
                <h3>{page}</h3>
                <p>Module under development.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# App Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    render_dashboard()

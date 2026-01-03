# ui/dashboard_ui.py
import streamlit as st
from ui.components.header import render_header
from ui.components.sidebar import render_sidebar
from ui.components.metric_card import render_metric_card
from ui.components.chart_card import render_chart_card

def render_dashboard():
    # Apply custom CSS
    with open("ui/theme/layout.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Header
    render_header()

    # Sidebar navigation
    page = render_sidebar()

    st.markdown("<br>", unsafe_allow_html=True)

    if page == "Overview":
        # KPI Cards Row
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric_card("Total Sales", "₹ 3,45,00,000", delta="5% ↑", description="Compared to last month")
        with col2:
            render_metric_card("Total Orders", "12,450", delta="2% ↑")
        with col3:
            render_metric_card("Active Customers", "5,230", delta="3% ↓")
        with col4:
            render_metric_card("New Products", "32", delta="8% ↑")

        # Charts Row
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            render_chart_card("Monthly Sales Trend")
        with col2:
            render_chart_card("Top 5 Products")

    else:
        st.markdown(f"<div style='padding:20px;'>Welcome to the {page} page!</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    render_dashboard()

# ui/components/sidebar.py
import streamlit as st

def render_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", [
        "Overview",
        "Chat with AI",
        "Deep Analysis",
        "Forecasting",
        "Data Quality",
        "Executive Summary"
    ])
    return page

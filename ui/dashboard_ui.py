# ui/dashboard_ui.py
import streamlit as st
from ui.components.header import render_header
from ui.components.sidebar import render_sidebar
from ui.theme.ds_theme import CARD_STYLE

def render_dashboard():
    # Apply custom CSS
    with open("ui/theme/layout.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Header
    render_header()

    # Sidebar navigation
    page = render_sidebar()

    # Page content placeholder
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div style='{CARD_STYLE}'>Welcome to the {page} page!</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    render_dashboard()

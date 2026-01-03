# ui/components/insight_card.py
import streamlit as st
from ui.theme.ds_theme import CARD_STYLE

def render_insight_card(title, insight, level="info"):
    color_map = {
        "info": "#0B8F4D",
        "warning": "#E6A100",
        "critical": "#C0392B"
    }

    st.markdown(
        f"""
        <div style="{CARD_STYLE}; border-left:6px solid {color_map.get(level)};">
            <h4 style="margin:0;">{title}</h4>
            <p style="margin-top:8px; color:#333;">{insight}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

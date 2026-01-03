# ui/components/chart_card.py
import streamlit as st
from ui.theme.ds_theme import CARD_STYLE, DS_TEXT_COLOR

def render_chart_card(title, chart_placeholder=True):
    st.markdown(
        f"""
        <div style="{CARD_STYLE}">
            <h3 style="color:{DS_TEXT_COLOR};">{title}</h3>
            {'<div style="height:200px;background:#f0f0f0;border-radius:8px;text-align:center;line-height:200px;color:#aaa;">Chart Placeholder</div>' if chart_placeholder else ''}
        </div>
        """,
        unsafe_allow_html=True
    )

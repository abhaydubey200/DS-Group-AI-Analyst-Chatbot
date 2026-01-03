# ui/components/metric_card.py
import streamlit as st
from ui.theme.ds_theme import CARD_STYLE, DS_PRIMARY_COLOR, DS_TEXT_COLOR

def render_metric_card(title, value, delta=None, description=None):
    delta_html = f"<span style='color:green;'>&#9650; {delta}</span>" if delta else ""
    description_html = f"<div style='font-size:12px;color:#555;'>{description}</div>" if description else ""
    
    st.markdown(
        f"""
        <div style="{CARD_STYLE}">
            <h3 style="margin:0;color:{DS_PRIMARY_COLOR};">{title}</h3>
            <h2 style="margin:5px 0;color:{DS_TEXT_COLOR};">{value} {delta_html}</h2>
            {description_html}
        </div>
        """,
        unsafe_allow_html=True
    )

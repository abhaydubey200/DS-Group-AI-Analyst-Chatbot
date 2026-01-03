# ui/components/analysis_section.py
import streamlit as st
from ui.theme.ds_theme import CARD_STYLE, DS_PRIMARY_COLOR

def render_analysis_section(title, description=None):
    description_html = f"<p style='color:#555;'>{description}</p>" if description else ""

    st.markdown(
        f"""
        <div style="{CARD_STYLE}">
            <h3 style="color:{DS_PRIMARY_COLOR}; margin-bottom:5px;">{title}</h3>
            {description_html}
            <div style="
                height:220px;
                background:#F5F5F5;
                border-radius:10px;
                display:flex;
                align-items:center;
                justify-content:center;
                color:#AAA;
                font-size:14px;
            ">
                Analysis Visualization Placeholder
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

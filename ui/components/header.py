# ui/components/header.py
import streamlit as st
from ui.theme.ds_theme import DS_PRIMARY_COLOR, DS_FONT_FAMILY

def render_header(title="DS Group AI Analyst"):
    st.markdown(
        f"""
        <div style="
            background-color:{DS_PRIMARY_COLOR};
            color:white;
            padding:15px;
            border-radius:8px;
            text-align:center;
            font-size:28px;
            font-family:{DS_FONT_FAMILY};
        ">
            {title} 🚀
        </div>
        """,
        unsafe_allow_html=True
    )

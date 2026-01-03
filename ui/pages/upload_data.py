# ui/pages/upload_data.py

import streamlit as st
from logging_config import logger
from data_engine.uploader import load_dataset

def page_upload_data():
    st.title("Upload Dataset")

    uploaded_file = st.file_uploader("Upload CSV/XLSX", type=["csv", "xlsx"])
    if uploaded_file:
        try:
            df = load_dataset(uploaded_file)
            st.success("Dataset loaded successfully!")
            st.dataframe(df.head())
            logger.info(f"Dataset uploaded: {uploaded_file.name}")
        except Exception as e:
            st.error("Failed to load dataset.")
            logger.error(f"Upload error: {e}")

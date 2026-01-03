# ui/components/filters.py

import streamlit as st

def render_filters(df, columns):
    filters = {}
    st.sidebar.header("⚙️ Filters")
    for col in columns:
        if df[col].dtype == object:
            filters[col] = st.sidebar.multiselect(f"Select {col}", options=df[col].unique(), default=df[col].unique())
        elif df[col].dtype in ["int64", "float64"]:
            min_val, max_val = int(df[col].min()), int(df[col].max())
            filters[col] = st.sidebar.slider(f"{col} range", min_value=min_val, max_value=max_val, value=(min_val, max_val))
    return filters

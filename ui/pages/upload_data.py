# ui/pages/upload_data.py
import streamlit as st
from data_engine.uploader import load_dataset
from data_engine.validator import validate_dataset
from data_engine.schema_detector import detect_schema
from data_engine.profiler import profile_dataset
from data_engine.sample_store import store_sample
import hashlib

def render_upload_page():

    st.markdown("### 📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file:
        df = load_dataset(uploaded_file)

        st.success("Dataset uploaded successfully")
        st.dataframe(df.head())

        # Validation
        issues = validate_dataset(df)
        if issues:
            st.warning("Data Issues Detected:")
            for issue in issues:
                st.write("•", issue)

        # Profiling
        profile = profile_dataset(df)
        st.json(profile)

        # Schema
        schema = detect_schema(df)
        st.markdown("### 🧬 Detected Schema")
        st.json(schema)

        # Store sample for training
        schema_signature = hashlib.md5(
            str(schema).encode()
        ).hexdigest()

        store_sample(df, schema_signature)

        st.success("Sample stored for future model learning")


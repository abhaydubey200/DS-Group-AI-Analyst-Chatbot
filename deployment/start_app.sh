#!/bin/bash
echo "Starting DS Group AI Analyst..."
streamlit run ui/dashboard_ui.py --server.port=8501 --server.address=0.0.0.0

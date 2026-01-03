# ui/components/charts.py

import streamlit as st
import plotly.express as px

def render_forecast_chart(df, date_col="Date", value_col="forecast"):
    fig = px.line(df, x=date_col, y=value_col, title="📈 Forecast Trend")
    st.plotly_chart(fig, use_container_width=True)

def render_scenario_chart(scenario_results):
    import pandas as pd
    combined = []
    for scenario in scenario_results:
        combined.append({
            "Scenario": scenario["scenario"],
            "Impact": scenario["impact"]["impact_value"]
        })
    chart_df = pd.DataFrame(combined)
    fig = px.bar(chart_df, x="Scenario", y="Impact", color="Impact", title="⚡ Scenario Impact")
    st.plotly_chart(fig, use_container_width=True)

def render_feature_importance_chart(feature_importance):
    import pandas as pd
    chart_df = pd.DataFrame(list(feature_importance.items()), columns=["Feature", "Importance"])
    fig = px.bar(chart_df, x="Feature", y="Importance", color="Importance", title="🧠 Feature Importance")
    st.plotly_chart(fig, use_container_width=True)

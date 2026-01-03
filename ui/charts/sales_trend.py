# ui/charts/sales_trend.py
import plotly.express as px
import pandas as pd
from ui.charts.chart_theme import apply_ds_theme, DS_GREEN

def sales_trend_chart():
    # Dummy data (will be replaced by real dataset later)
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [52, 58, 61, 59, 65, 72]
    })

    fig = px.line(
        df,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )
    fig.update_traces(line=dict(color=DS_GREEN, width=3))
    return apply_ds_theme(fig)

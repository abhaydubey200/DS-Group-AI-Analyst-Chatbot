# ui/charts/bar_chart.py
import plotly.express as px
import pandas as pd
from ui.charts.chart_theme import apply_ds_theme, DS_GREEN

def region_contribution_chart():
    df = pd.DataFrame({
        "Region": ["North", "South", "East", "West"],
        "Sales": [420, 310, 220, 180]
    })

    fig = px.bar(
        df,
        x="Region",
        y="Sales",
        title="Region-wise Sales Contribution"
    )
    fig.update_traces(marker_color=DS_GREEN)
    return apply_ds_theme(fig)

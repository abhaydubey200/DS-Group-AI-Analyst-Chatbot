# ui/charts/pie_chart.py
import plotly.express as px
import pandas as pd
from ui.charts.chart_theme import apply_ds_theme

def product_share_chart():
    df = pd.DataFrame({
        "Product": ["A", "B", "C", "D"],
        "Share": [35, 25, 20, 20]
    })

    fig = px.pie(
        df,
        names="Product",
        values="Share",
        title="Product Sales Share"
    )
    return apply_ds_theme(fig)

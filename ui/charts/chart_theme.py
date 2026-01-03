# ui/charts/chart_theme.py
DS_GREEN = "#0B8F4D"
DS_GRAY = "#EAEAEA"
DS_TEXT = "#000000"

def apply_ds_theme(fig):
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color=DS_TEXT, size=12),
        title_font=dict(size=16),
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
            y=-0.2
        )
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor=DS_GRAY)
    return fig

import pandas as pd
import plotly.express as px


def heatmap_chart(data):

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="zone",
        y="heat_score",
        text="visit_count",
        title="Zone Heatmap"
    )

    return fig


def funnel_chart(data):

    df = pd.DataFrame(
        {
            "Stage": [
                "Entry",
                "Zone Visit",
                "Billing"
            ],
            "Count": [
                data["entry"],
                data["zone_visit"],
                data["billing"]
            ]
        }
    )

    fig = px.funnel(
        df,
        x="Count",
        y="Stage"
    )

    return fig
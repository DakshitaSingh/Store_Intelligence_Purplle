import plotly.graph_objects as go


def layout_heatmap(
    heatmap_data
):

    scores = {}

    for row in heatmap_data:

        scores[
            row["zone"]
        ] = row["heat_score"]

    fig = go.Figure()

    fig.add_layout_image(
        dict(
            source="layouts/store2_layout.png",
            x=0,
            y=100,
            sizex=100,
            sizey=100,
            sizing="stretch",
            opacity=0.8,
            layer="below"
        )
    )

    zone_positions = {
        "LEFT_ZONE": (20, 50),
        "CENTER_ZONE": (50, 50),
        "RIGHT_ZONE": (80, 50)
    }

    xs = []
    ys = []
    sizes = []
    texts = []

    for zone, pos in zone_positions.items():

        score = scores.get(
            zone,
            0
        )

        xs.append(pos[0])
        ys.append(pos[1])

        sizes.append(
            max(
                score,
                10
            )
        )

        texts.append(
            f"{zone}<br>{score}"
        )

    fig.add_trace(

        go.Scatter(
            x=xs,
            y=ys,
            mode="markers+text",
            text=texts,
            textposition="top center",
            marker=dict(
                size=sizes
            )
        )
    )

    fig.update_xaxes(
        visible=False
    )

    fig.update_yaxes(
        visible=False
    )

    fig.update_layout(
        height=600
    )

    return fig
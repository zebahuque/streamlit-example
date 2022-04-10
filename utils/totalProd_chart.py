import altair as alt

def get_chart(data):
    hover = alt.selection_single(
        fields=["year"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Crop Production",
        )
        .mark_line()
        .encode(
            x = alt.X("year", axis=alt.Axis(title="Year")),
            y = alt.Y("crop-production", axis=alt.Axis(title="Crop Production (BU)"), sort="descending")
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x = alt.X("year", axis=alt.Axis(title="Year")),
            y = alt.Y("crop-production", axis=alt.Axis(title="Crop Production (BU)"), sort="descending"),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("year", title="Year"),
                alt.Tooltip("crop-production", title="Crop Production (BU)"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()
import altair as alt

def get_chart(data):
    hover = alt.selection_single(
        fields=["year"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Temperature",
        )
        .mark_line()
        .encode(
            x = alt.X("year", axis=alt.Axis(title="Year")),
            y = alt.Y("temperature", axis=alt.Axis(title="Temperature (°F)"), sort="descending"),
            color=alt.Color("County")
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
            y = alt.Y("temperature", axis=alt.Axis(title="Temperature (°F)"), sort="descending"),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("year", title="Year"),
                alt.Tooltip("temperature", title="Temperature (°F)"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()
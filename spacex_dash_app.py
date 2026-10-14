import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load SpaceX launch data
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Find minimum and maximum payload mass
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

# Initialize the Dash application
app = dash.Dash(__name__)

# Create the dashboard layout
app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center"}
        ),

        # TASK 1: Dropdown for selecting a launch site
        html.Label("Select Launch Site:"),
        dcc.Dropdown(
            id="site-dropdown",
            options=[{"label": "All Sites", "value": "ALL"}] + [
                {"label": site, "value": site}
                for site in spacex_df["Launch Site"].unique()
            ],
            value="ALL",
            placeholder="Select a Launch Site here",
            searchable=True
        ),

        # Pie chart
        html.Br(),
        html.Div(dcc.Graph(id="success-pie-chart")),

        # TASK 3: Payload range slider
        html.Label("Select Payload Range (kg):"),
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            marks={0: "0", 2500: "2500", 5000: "5000", 7500: "7500", 10000: "10000"},
            value=[min_payload, max_payload]
        ),

        # Scatter plot
        html.Br(),
        html.Div(dcc.Graph(id="success-payload-scatter-chart"))
    ]
)


# TASK 2: Update the pie chart when the launch site changes
@app.callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value")
)
def get_pie_chart(entered_site):
    if entered_site == "ALL":
        # Share of ALL successful launches contributed by each site
        # (class = 1 for success, so summing class counts successes per site)
        fig = px.pie(
            spacex_df,
            values="class",
            names="Launch Site",
            title="Total Successful Launches by Site"
        )
    else:
        # Success (1) vs. failure (0) for the selected site
        filtered_df = spacex_df[spacex_df["Launch Site"] == entered_site]
        fig = px.pie(
            filtered_df,
            names="class",
            title=f"Success vs. Failed Launches for {entered_site}"
        )
    return fig


# TASK 4: Update the scatter plot based on site and payload range
@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [
        Input(component_id="site-dropdown", component_property="value"),
        Input(component_id="payload-slider", component_property="value")
    ]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range

    # Filter by selected payload range
    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low) &
        (spacex_df["Payload Mass (kg)"] <= high)
    ]

    if entered_site == "ALL":
        fig = px.scatter(
            filtered_df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title="Payload Mass vs. Launch Outcome for All Sites"
        )
    else:
        filtered_df = filtered_df[filtered_df["Launch Site"] == entered_site]
        fig = px.scatter(
            filtered_df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title=f"Payload Mass vs. Launch Outcome for {entered_site}"
        )
    return fig


# Run the Dash application
if __name__ == "__main__":
    app.run(debug=True, port=8050)

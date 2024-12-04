import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json
from layouts import home_layout, analysis_layout, create_detailed_analysis_layout


state_to_code = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR", "california": "CA",
    "colorado": "CO", "connecticut": "CT", "delaware": "DE", "florida": "FL", "georgia": "GA",
    "hawaii": "HI", "idaho": "ID", "illinois": "IL", "indiana": "IN", "iowa": "IA",
    "kansas": "KS", "kentucky": "KY", "louisiana": "LA", "maine": "ME", "maryland": "MD",
    "massachusetts": "MA", "michigan": "MI", "minnesota": "MN", "mississippi": "MS",
    "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV", "new hampshire": "NH",
    "new jersey": "NJ", "new mexico": "NM", "new york": "NY", "north carolina": "NC",
    "north dakota": "ND", "ohio": "OH", "oklahoma": "OK", "oregon": "OR", "pennsylvania": "PA",
    "rhode island": "RI", "south carolina": "SC", "south dakota": "SD", "tennessee": "TN",
    "texas": "TX", "utah": "UT", "vermont": "VT", "virginia": "VA", "washington": "WA",
    "west virginia": "WV", "wisconsin": "WI", "wyoming": "WY"
}
normalized_state_to_code = {state.replace(" ", "").lower(): code for state, code in state_to_code.items()}



# Load JSON data - Candidates
with open('data/candidate_sentiments/after_cand_comment_sentiments.json') as f:
    data_after = json.load(f)

with open('data/candidate_sentiments/before_cand_comment_sentiments.json') as f:
    data_before = json.load(f)

# Load JSON data - Topics
with open('data/topic_pol_directions/after_topic_comment_stats.json') as f:
    topics_data_after = json.load(f)

with open('data/topic_pol_directions/after_topic_comment_stats.json') as f:
    topics_data_before = json.load(f)


# Normalize and Prepare the Data
def prepare_data(data, election_period):
    rows = []
    for state, topics in data.items():
        # Normalize the state name and map to abbreviation
        state_code = state_to_code.get(state.strip().lower(), None)  # Handle missing or invalid states
        
        # Skip invalid states
        if not state_code:
            continue
        
        for topic, details in topics.items():
            row = {
                "State": state_code,
                "Topic": topic.capitalize(),
                "Dominant Sentiment": details.get("direction"),
                "Election Period": election_period,
            }
            rows.append(row)
    return rows


data_before_rows = prepare_data(topics_data_before, "Before")
data_after_rows = prepare_data(topics_data_after, "After")


# Combine Both Periods into One DataFrame
df = pd.DataFrame(data_before_rows + data_after_rows)
detailed_analysis_layout = create_detailed_analysis_layout(df)
    
# AFTER ELECTION
trump_map_data_after = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in data_after.keys()],
    'Dominant Sentiment': [data_after[state]['trump']['sentiment'] for state in data_after.keys()],
    'Average Sentiment': [data_after[state]['trump']['avg_sentiment'] for state in data_after.keys()]
})

kamala_map_data_after = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in data_after.keys()],
    'Dominant Sentiment': [data_after[state]['harris']['sentiment'] for state in data_after.keys()],
    'Average Sentiment': [data_after[state]['harris']['avg_sentiment'] for state in data_after.keys()]
})

# BEFORE ELECTION
trump_map_data_before = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in data_before.keys()],
    'Dominant Sentiment': [data_before[state]['trump']['sentiment'] for state in data_before.keys()],
    'Average Sentiment': [data_before[state]['trump']['avg_sentiment'] for state in data_before.keys()]
})

kamala_map_data_before = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in data_before.keys()],
    'Dominant Sentiment': [data_before[state]['harris']['sentiment'] for state in data_before.keys()],
    'Average Sentiment': [data_before[state]['harris']['avg_sentiment'] for state in data_before.keys()]
})

# Define color mapping
color_discrete_map = {
    "positive": "#9AD3A2",  # light green
    "neutral": "#ADDFFF",   # light blue
    "negative": "#FFBDBF"   # light red
}

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Update Layout Based on URL
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Existing Callbacks for Graphs
@app.callback(Output('trump-map-before', 'figure'), Input('trump-map-before', 'id'))
def update_trump_map_before(_):
    return generate_map(trump_map_data_before, "Trump - Before the Election")

@app.callback(Output('kamala-map-before', 'figure'), Input('kamala-map-before', 'id'))
def update_kamala_map_before(_):
    return generate_map(kamala_map_data_before, "Kamala - Before the Election")

@app.callback(Output('trump-map-after', 'figure'), Input('trump-map-after', 'id'))
def update_trump_map_after(_):
    return generate_map(trump_map_data_after, "Trump - After the Election")

@app.callback(Output('kamala-map-after', 'figure'), Input('kamala-map-after', 'id'))
def update_kamala_map_after(_):
    return generate_map(kamala_map_data_after, "Kamala - After the Election")

# Function to generate a map
def generate_map(data, title):
    fig = px.choropleth(
        data,
        locations="State",
        locationmode="USA-states",
        color="Dominant Sentiment",
        hover_name="State",
        hover_data={"Dominant Sentiment": True, "Average Sentiment": ":.2f", 'State': False},
        scope="usa",
        color_discrete_map=color_discrete_map
    )
    fig.update_layout(
        title=None,
        title_x=0.5,
        geo=dict(lakecolor="lightblue"),
        hoverlabel=dict(bgcolor="white", font_size=14, font_family="Arial")
    )
    return fig



# Callback to Update Maps
@app.callback(
    [Output("hover-map-before", "figure"), Output("hover-map-after", "figure")],
    Input("keyword-dropdown", "value")
)
def update_hover_maps(selected_keyword):
    filtered_before = df[(df["Topic"] == selected_keyword) & (df["Election Period"] == "Before")]
    filtered_after = df[(df["Topic"] == selected_keyword) & (df["Election Period"] == "After")]

    fig_before = px.choropleth(
        filtered_before,
        locations="State",
        locationmode="USA-states",
        color="Dominant Sentiment",
        hover_name="State",
        scope="usa",
        color_discrete_map={"left": "#9AD3A2", "right": "#FFBDBF", "center": "#ADDFFF"}
    )
    fig_before.update_layout(title="Before the Election", title_x=0.5)

    fig_after = px.choropleth(
        filtered_after,
        locations="State",
        locationmode="USA-states",
        color="Dominant Sentiment",
        hover_name="State",
        scope="usa",
        color_discrete_map={"left": "#9AD3A2", "right": "#FFBDBF", "center": "#ADDFFF"}
    )
    fig_after.update_layout(title="After the Election", title_x=0.5)

    return fig_before, fig_after

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/analysis":
        return analysis_layout  # Ensure analysis_layout is defined
    elif pathname == "/detailed-analysis":
        return detailed_analysis_layout
    else:
        return home_layout
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

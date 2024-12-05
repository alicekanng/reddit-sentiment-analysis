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


#Loading Comments Data
# Load JSON data - Candidates
with open('data/candidate_sentiments/after_cand_comment_sentiments.json') as f:
    candidate_data_after_comments = json.load(f)

with open('data/candidate_sentiments/before_cand_comment_sentiments.json') as f:
    candidate_data_before_comments = json.load(f)

# Load JSON data - Topics
with open('data/topic_pol_directions/after_topic_comment_stats.json') as f:
    topics_data_after_comments = json.load(f)

with open('data/topic_pol_directions/after_topic_comment_stats.json') as f:
    topics_data_before_comments = json.load(f)

#Loading Posts Data
# Load JSON data - Candidates
with open('data/candidate_sentiments/after_cand_post_sentiments.json') as f:
    candidate_data_after_posts = json.load(f)

with open('data/candidate_sentiments/before_cand_post_sentiments.json') as f:
    candidate_data_before_posts = json.load(f)

# Load JSON data - Topics
with open('data/topic_pol_directions/after_topic_post_stats.json') as f:
    topics_data_after_posts = json.load(f)

with open('data/topic_pol_directions/after_topic_post_stats.json') as f:
    topics_data_before_posts = json.load(f)


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


#POSTS DATA 
data_before_rows_posts = prepare_data(topics_data_before_posts, "Before")
data_after_rows_posts = prepare_data(topics_data_after_posts, "After")

df_posts = pd.DataFrame(data_before_rows_posts + data_after_rows_posts)
detailed_analysis_layout_posts= create_detailed_analysis_layout(df_posts)

#COMMENTS DATA 
data_before_rows_comments = prepare_data(topics_data_before_comments, "Before")
data_after_rows_comments = prepare_data(topics_data_after_comments, "After")

# Combine Both Periods into One DataFrame
df_comments = pd.DataFrame(data_before_rows_comments + data_after_rows_comments)
detailed_analysis_layout_comments= create_detailed_analysis_layout(df_comments)

# BEFORE ELECTION - COMMENTS
trump_map_data_before_comments = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_before_comments.keys()],
    'Dominant Sentiment': [
        candidate_data_before_comments[state].get('trump', {}).get('sentiment', None)
        for state in candidate_data_before_comments.keys()
    ],
    'Average Sentiment': [
        candidate_data_before_comments[state].get('trump', {}).get('avg_sentiment', None)
        for state in candidate_data_before_comments.keys()
    ],
})

kamala_map_data_before_comments = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_before_comments.keys()],
    'Dominant Sentiment': [
        candidate_data_before_comments[state].get('harris', {}).get('sentiment', None)
        for state in candidate_data_before_comments.keys()
    ],
    'Average Sentiment': [
        candidate_data_before_comments[state].get('harris', {}).get('avg_sentiment', None)
        for state in candidate_data_before_comments.keys()
    ],
})

# AFTER ELECTION - COMMENTS
trump_map_data_after_comments = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_after_comments.keys()],
    'Dominant Sentiment': [
        candidate_data_after_comments[state].get('trump', {}).get('sentiment', None)
        for state in candidate_data_after_comments.keys()
    ],
    'Average Sentiment': [
        candidate_data_after_comments[state].get('trump', {}).get('avg_sentiment', None)
        for state in candidate_data_after_comments.keys()
    ],
})

kamala_map_data_after_comments = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_after_comments.keys()],
    'Dominant Sentiment': [
        candidate_data_after_comments[state].get('harris', {}).get('sentiment', None)
        for state in candidate_data_after_comments.keys()
    ],
    'Average Sentiment': [
        candidate_data_after_comments[state].get('harris', {}).get('avg_sentiment', None)
        for state in candidate_data_after_comments.keys()
    ],
})

# AFTER ELECTION - POSTS
trump_map_data_after_posts = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_after_posts.keys()],
    'Dominant Sentiment': [
        candidate_data_after_posts[state].get('trump', {}).get('sentiment', None)
        for state in candidate_data_after_posts.keys()
    ],
    'Average Sentiment': [
        candidate_data_after_posts[state].get('trump', {}).get('avg_sentiment', None)
        for state in candidate_data_after_posts.keys()
    ],
})

kamala_map_data_after_posts = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_after_posts.keys()],
    'Dominant Sentiment': [
        candidate_data_after_posts[state].get('harris', {}).get('sentiment', None)
        for state in candidate_data_after_posts.keys()
    ],
    'Average Sentiment': [
        candidate_data_after_posts[state].get('harris', {}).get('avg_sentiment', None)
        for state in candidate_data_after_posts.keys()
    ],
})

# BEFORE ELECTION - POSTS
trump_map_data_before_posts = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_before_posts.keys()],
    'Dominant Sentiment': [
        candidate_data_before_posts[state].get('trump', {}).get('sentiment', None)
        for state in candidate_data_before_posts.keys()
    ],
    'Average Sentiment': [
        candidate_data_before_posts[state].get('trump', {}).get('avg_sentiment', None)
        for state in candidate_data_before_posts.keys()
    ],
})

kamala_map_data_before_posts = pd.DataFrame({
    'State': [normalized_state_to_code[state.lower()] for state in candidate_data_before_posts.keys()],
    'Dominant Sentiment': [
        candidate_data_before_posts[state].get('harris', {}).get('sentiment', None)
        for state in candidate_data_before_posts.keys()
    ],
    'Average Sentiment': [
        candidate_data_before_posts[state].get('harris', {}).get('avg_sentiment', None)
        for state in candidate_data_before_posts.keys()
    ],
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


@app.callback(
    [Output("trump-map-before", "figure"), Output("kamala-map-before", "figure"),
     Output("trump-map-after", "figure"), Output("kamala-map-after", "figure")],
    [Input("data-toggle", "value")]
)
def update_candidate_maps(data_source):
    if data_source == "comments":
        trump_before = generate_map(trump_map_data_before_comments, "Trump - Before the Election")
        kamala_before = generate_map(kamala_map_data_before_comments, "Kamala - Before the Election")
        trump_after = generate_map(trump_map_data_after_comments, "Trump - After the Election")
        kamala_after = generate_map(kamala_map_data_after_comments, "Kamala - After the Election")
    elif data_source == "posts":
        trump_before = generate_map(trump_map_data_before_posts, "Trump - Before the Election (Posts)")
        kamala_before = generate_map(kamala_map_data_before_posts, "Kamala - Before the Election (Posts)")
        trump_after = generate_map(trump_map_data_after_posts, "Trump - After the Election (Posts)")
        kamala_after = generate_map(kamala_map_data_after_posts, "Kamala - After the Election (Posts)")

    return trump_before, kamala_before, trump_after, kamala_after


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



@app.callback(
    [Output("hover-map-before", "figure"), Output("hover-map-after", "figure")],
    [Input("keyword-dropdown", "value"), Input("data-toggle", "value")]
)
def update_hover_maps(selected_keyword, selected_data):
    if selected_data == "comments":
        filtered_before = df_comments[(df_comments["Topic"] == selected_keyword) & (df_comments["Election Period"] == "Before")]
        filtered_after = df_comments[(df_comments["Topic"] == selected_keyword) & (df_comments["Election Period"] == "After")]
    elif selected_data == "posts":
        filtered_before = df_posts[(df_posts["Topic"] == selected_keyword) & (df_posts["Election Period"] == "Before")]
        filtered_after = df_posts[(df_posts["Topic"] == selected_keyword) & (df_posts["Election Period"] == "After")]

    fig_before = px.choropleth(
        filtered_before,
        locations="State",
        locationmode="USA-states",
        color="Dominant Sentiment",
        hover_name="State",
        scope="usa",
        color_discrete_map={"left": "#9AD3A2", "right": "#FFBDBF", "center": "#ADDFFF"}
    )
    fig_before.update_layout(title=None, title_x=0.5)

    fig_after = px.choropleth(
        filtered_after,
        locations="State",
        locationmode="USA-states",
        color="Dominant Sentiment",
        hover_name="State",
        scope="usa",
        color_discrete_map={"left": "#9AD3A2", "right": "#FFBDBF", "center": "#ADDFFF"}
    )
    fig_after.update_layout(title=None, title_x=0.5)

    return fig_before, fig_after


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/analysis":
        return analysis_layout
    elif pathname == "/detailed-analysis":
        # Ensure the layout includes data-toggle
        return create_detailed_analysis_layout(df_comments)
    else:
        return home_layout


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

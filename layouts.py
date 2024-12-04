# layouts.py
from dash import html, dcc

# Define Home Page Layout
home_layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#FFFFFF",  # White background
        "color": "#333",
        "padding": "50px",
        "textAlign": "center",
        "height": "100vh",  # Full height
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "center",
        "alignItems": "center",
    },
    children=[
        html.H1(
            "Welcome to the Sentiment Analysis Dashboard",
            style={
                "color": "#333",
                "fontSize": "48px",
                "marginBottom": "20px",
                "fontFamily": "Roboto, sans-serif",
                "textShadow": "1px 1px 2px rgba(0, 0, 0, 0.1)",
            },
        ),
        html.P(
            "Explore the political sentiment analysis for the 2024 US Presidential Election.",
            style={
                "color": "#555",
                "fontSize": "20px",
                "marginBottom": "40px",
                "maxWidth": "600px",  # Restrict width for readability
            },
        ),
        html.Div(
            style={
                "display": "flex",
                "gap": "20px",
                "justifyContent": "center",
            },
            children=[
                html.A(
                    html.Button(
                        "Candidate Sentiment Analysis",
                        style={
                            "fontSize": "18px",
                            "padding": "12px 30px",
                            "backgroundColor": "#007bff",
                            "color": "white",
                            "borderRadius": "8px",
                            "border": "none",
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                            "cursor": "pointer",
                            "transition": "transform 0.3s, box-shadow 0.3s",
                        },
                    ),
                    href="/analysis",
                ),
                html.A(
                    html.Button(
                        "Political Topic Analysis",
                        style={
                            "fontSize": "18px",
                            "padding": "12px 30px",
                            "backgroundColor": "#007bff",
                            "color": "white",
                            "borderRadius": "8px",
                            "border": "none",
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                            "cursor": "pointer",
                            "transition": "transform 0.3s, box-shadow 0.3s",
                        },
                    ),
                    href="/detailed-analysis",
                ),
            ],
        ),
    ],
)



analysis_layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#FFFFFF",
        "padding": "20px"
    },
    children=[
        html.H1(
            "US Sentiment Analysis Dashboard",
            style={"textAlign": "center", "color": "#333", "fontSize": "40px", "marginBottom": "20px"}
        ),
        html.P(
            "This dashboard visualizes the dominant sentiment across U.S. states, derived from Reddit posts and comments. "
            ,
            style={"textAlign": "center", "color": "#666", "fontSize": "18px", "marginBottom": "30px"}
        ),
        html.Div(
            children=[
                html.H2("Before the Election", style={"textAlign": "center", "color": "#333", "marginBottom": "20px"}),
                html.Div(
                    style={"display": "flex", "justifyContent": "center", "gap": "20px"},
                    children=[
                        html.Div(
                            children=[
                                html.H3("Trump", style={"textAlign": "center", "color": "#333", "marginBottom": "10px"}),
                                dcc.Graph(id='trump-map-before', config={"displayModeBar": False})
                            ],
                            style={"flex": "1"}
                        ),
                        html.Div(
                            children=[
                                html.H3("Kamala", style={"textAlign": "center", "color": "#333", "marginBottom": "10px"}),
                                dcc.Graph(id='kamala-map-before', config={"displayModeBar": False})
                            ],
                            style={"flex": "1"}
                        )
                    ]
                )
            ]
        ),
        html.Div(
            children=[
                html.H2("After the Election", style={"textAlign": "center", "color": "#333", "marginBottom": "20px"}),
                html.Div(
                    style={"display": "flex", "justifyContent": "center", "gap": "20px"},
                    children=[
                        html.Div(
                            children=[
                                html.H3("Trump", style={"textAlign": "center", "color": "#333", "marginBottom": "10px"}),
                                dcc.Graph(id='trump-map-after', config={"displayModeBar": False})
                            ],
                            style={"flex": "1"}
                        ),
                        html.Div(
                            children=[
                                html.H3("Kamala", style={"textAlign": "center", "color": "#333", "marginBottom": "10px"}),
                                dcc.Graph(id='kamala-map-after', config={"displayModeBar": False})
                            ],
                            style={"flex": "1"}
                        )
                    ]
                )
            ]
        ),
        html.Br(),
        html.A(
            html.Button(
                "Back to Home",
                style={"fontSize": "16px", "padding": "10px 20px", "backgroundColor": "#007bff", "color": "white"}
            ),
            href="/"
        )
    ]
)

def create_detailed_analysis_layout(df):
    return html.Div(
        style={"padding": "20px", "fontFamily": "Arial, sans-serif"},
        children=[
            html.H1("Hover Map: Sentiment Analysis by Keyword", style={"textAlign": "center", "fontSize": "40px"}),
            html.Div(
                children=[
                    html.Label("Select Keyword:", style={"fontSize": "18px"}),
                    dcc.Dropdown(
                        id="keyword-dropdown",
                        options=[{"label": kw, "value": kw} for kw in df["Topic"].unique()],
                        value="Abortion",
                        style={"width": "50%", "margin": "auto"},
                    ),
                ],
                style={"marginBottom": "20px"}
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H2("Before the Election", style={"textAlign": "center"}),
                            dcc.Graph(id="hover-map-before", config={"displayModeBar": False}),
                        ],
                        style={"width": "48%", "display": "inline-block"}
                    ),
                    html.Div(
                        children=[
                            html.H2("After the Election", style={"textAlign": "center"}),
                            dcc.Graph(id="hover-map-after", config={"displayModeBar": False}),
                        ],
                        style={"width": "48%", "display": "inline-block"}
                    ),
                ],
                style={"display": "flex", "justifyContent": "center", "gap": "20px"}
            ),
            html.Br(),
            html.A(
                html.Button("Back to Home", 
                            style={"fontSize": "16px", "padding": "10px 20px", "backgroundColor": "#007bff", "color": "white"}),
                href="/",
            ),
        ],
    )

# Export layouts
__all__ = ["home_layout", "analysis_layout"]

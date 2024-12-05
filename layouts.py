from dash import html, dcc

# Define Home Page Layout
home_layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundImage": "url('https://img-cdn.inc.com/image/upload/f_webp,q_auto,c_fit/vip/2024/10/GettyImages-2175116872.jpg')",  # Replace with your background image URL
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "position": "relative",
        "height": "100vh",
        "color": "#333",
        "textAlign": "center",
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "center",
        "alignItems": "center",
    },
    children=[
        # Semi-transparent overlay
        html.Div(
            style={
                "position": "absolute",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "backgroundColor": "rgba(255, 255, 255, 0.8)",  # Adjust transparency (0.8 is 80% opaque)
                "zIndex": "1",
            },
        ),
        # Content box
        html.Div(
            style={
                "maxWidth": "900px",
                "textAlign": "center",
                "backgroundColor": "#ffffff",
                "padding": "40px",
                "borderRadius": "15px",
                "boxShadow": "0 6px 12px rgba(0, 0, 0, 0.1)",
                "zIndex": "2",  # Ensures content is above overlay
                "position": "relative",
            },
            children=[
            
                html.H1(
                    "Sentiment Analysis Dashboard",
                    style={
                        "fontSize": "48px",
                        "marginBottom": "20px",
                        "fontWeight": "bold",
                        "color": "#333",
                    },
                ),
                html.P(
                    "Unlock insights from the 2024 US Presidential Election. ",
                    style={
                        "fontSize": "18px",
                        "marginBottom": "40px",
                        "color": "#555",
                        "lineHeight": "1.6",
                    },
                ),
                # New Overview Section
                html.Div(
                    style={
                        "marginTop": "30px",
                        "padding": "20px",
                        "backgroundColor": "#f9f9f9",
                        "borderRadius": "12px",
                        "boxShadow": "0 2px 6px rgba(0, 0, 0, 0.1)",
                    },
                    children=[
                        html.H2(
                            "Overview of the Application",
                            style={
                                "fontSize": "24px",
                                "marginBottom": "15px",
                                "fontWeight": "bold",
                                "color": "#333",
                            },
                        ),
                        html.P(
                            "This dashboard offers comprehensive sentiment analysis based on data gathered from Reddit. With this tool, you can:",
                            style={
                                "fontSize": "16px",
                                "color": "#555",
                                "lineHeight": "1.5",
                                "marginBottom": "15px",
                            },
                        ),
                        html.Ul(
                            children=[
                                html.Li("Analyze sentiment trends for US Presidential candidates."),
                                html.Li("Track political topics and their public reception."),
                                html.Li("View sentiment data before and after the election."),
                                html.Li("Filter and explore data using interactive graphs."),
                            ],
                            style={
                                "fontSize": "16px",
                                "color": "#555",
                                "textAlign": "left",
                                "margin": "auto",
                                "lineHeight": "1.6",
                                "maxWidth": "700px",
                                "listStyleType": "disc",
                            },
                        ),
                    ],
                ),
                html.Div(
                    style={
                        "display": "flex",
                        "gap": "20px",
                        "justifyContent": "center",
                        "marginTop": "40px",
                    },
                    children=[
                        html.A(
                            html.Button(
                                "Candidate Analysis",
                                style={
                                    "fontSize": "18px",
                                    "padding": "15px 30px",
                                    "backgroundColor": "#1f77b4",
                                    "color": "white",
                                    "borderRadius": "8px",
                                    "border": "none",
                                    "cursor": "pointer",
                                    "transition": "all 0.3s ease",
                                },
                                className="button-hover",
                            ),
                            href="/analysis",
                        ),
                        html.A(
                            html.Button(
                                "Topic Analysis",
                                style={
                                    "fontSize": "18px",
                                    "padding": "15px 30px",
                                    "backgroundColor": "#1f77b4",
                                    "color": "white",
                                    "borderRadius": "8px",
                                    "border": "none",
                                    "cursor": "pointer",
                                    "transition": "all 0.3s ease",
                                },
                                className="button-hover",
                            ),
                            href="/detailed-analysis",
                        ),
                    ],
                ),
            ],
        ),
        html.Footer(
            "© 2024 Sentiment Insights Inc.",
            style={
                "marginTop": "40px",
                "fontSize": "14px",
                "color": "#aaa",
                "textAlign": "center",
                "zIndex": "2",  # Ensures footer is above overlay
                "position": "relative",
            },
        ),
    ],
)



analysis_layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f7f7f7",
        "padding": "40px",
    },
    children=[ html.A(
            html.Button(
                "Back to Home",
                style={
                    "fontSize": "16px",
                    "padding": "10px 20px",
                    "backgroundColor": "#1f8efa",
                    "color": "white",
                    "borderRadius": "10px",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "cursor": "pointer",
                },
            ),
            href="/",
        ),
        html.H1(
            "US Sentiment Analysis Dashboard",
            style={
                "textAlign": "center",
                "color": "#333",
                "fontSize": "44px",
                "marginBottom": "30px",
                "textShadow": "1px 1px 3px rgba(0, 0, 0, 0.1)",
            },
        ),
        html.P(
            "Discover the political pulse across the United States with insights into candidate sentiment from Reddit.",
            style={
                "textAlign": "center",
                "color": "#666",
                "fontSize": "18px",
                "marginBottom": "40px",
                "maxWidth": "800px",
                "marginLeft": "auto",
                "marginRight": "auto",
            },
        ),
        html.Div(
    children=[
        html.Label(
            "Select Data Source:",
            style={
                "fontSize": "18px",
                "marginBottom": "10px",
                "fontWeight": "bold",
                "textAlign": "center",
            },
        ),
        html.P(
            "Choose between analyzing Reddit comments or posts. Comments provide granular insights, while posts capture broader sentiment trends.",
            style={
                "fontSize": "14px",
                "color": "#555",
                "marginTop": "5px",
                "marginBottom": "20px",
                "textAlign": "center",
                "lineHeight": "1.5",
            },
        ),
        dcc.RadioItems(
            id="data-toggle",
            options=[
                {"label": "Comments", "value": "comments"},
                {"label": "Posts", "value": "posts"}
            ],
            value="comments",  # Default value
            inline=True,
        ),
    ],
    style={
        "textAlign": "center",
                    "padding": "20px",
                    "backgroundColor": "#fff",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "borderRadius": "10px",
                    "marginBottom": "30px",
    },
),

        html.Div(
            children=[
                html.H2(
                    "Before the Election",
                    style={"textAlign": "center", "color": "#333", "marginBottom": "20px"},
                ),
                html.Div(
                    style={"display": "flex", "justifyContent": "center", "gap": "20px"},
                    children=[
                        html.Div(
                            children=[
                                html.H3(
                                    "Trump",
                                    style={"textAlign": "center", "color": "#333", "marginBottom": "10px"},
                                ),
                                dcc.Graph(id="trump-map-before", config={"displayModeBar": False}),
                            ],
                            style={
                                "flex": "1",
                                "padding": "10px",
                                "backgroundColor": "#fff",
                                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                "borderRadius": "10px",
                            },
                        ),
                        html.Div(
                            children=[
                                html.H3(
                                    "Kamala",
                                    style={"textAlign": "center", "color": "#333", "marginBottom": "10px"},
                                ),
                                dcc.Graph(id="kamala-map-before", config={"displayModeBar": False}),
                            ],
                            style={
                                "flex": "1",
                                "padding": "10px",
                                "backgroundColor": "#fff",
                                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                "borderRadius": "10px",
                            },
                        ),
                    ],
                ),
            ]
        ),
        html.Div(
            children=[
                html.H2(
                    "After the Election",
                    style={"textAlign": "center", "color": "#333", "marginBottom": "20px"},
                ),
                html.Div(
                    style={"display": "flex", "justifyContent": "center", "gap": "20px"},
                    children=[
                        html.Div(
                            children=[
                                html.H3(
                                    "Trump",
                                    style={"textAlign": "center", "color": "#333", "marginBottom": "10px"},
                                ),
                                dcc.Graph(id="trump-map-after", config={"displayModeBar": False}),
                            ],
                            style={
                                "flex": "1",
                                "padding": "10px",
                                "backgroundColor": "#fff",
                                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                "borderRadius": "10px",
                            },
                        ),
                        html.Div(
                            children=[
                                html.H3(
                                    "Kamala",
                                    style={"textAlign": "center", "color": "#333", "marginBottom": "10px"},
                                ),
                                dcc.Graph(id="kamala-map-after", config={"displayModeBar": False}),
                            ],
                            style={
                                "flex": "1",
                                "padding": "10px",
                                "backgroundColor": "#fff",
                                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                "borderRadius": "10px",
                            },
                        ),
                    ],
                ),
            ]
        ),
        html.Br(),
    
    ],
)
def create_detailed_analysis_layout(df):
    return html.Div(
        style={
            "padding": "30px",
            "fontFamily": "Arial, sans-serif",
            "backgroundColor": "#f7f7f7",
            "minHeight": "100vh",
        },
        children=[ html.A(
            html.Button(
                "Back to Home",
                style={
                    "fontSize": "16px",
                    "padding": "10px 20px",
                    "backgroundColor": "#1f8efa",
                    "color": "white",
                    "borderRadius": "10px",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "cursor": "pointer",
                },
            ),
            href="/",
        ),
            html.H1(
                "Topic Sentiment Analysis",
                style={
                    "textAlign": "center",
                    "fontSize": "48px",
                    "color": "#333",
                    "marginBottom": "20px",
                    "textShadow": "1px 1px 3px rgba(0, 0, 0, 0.2)",
                },
            ),
            html.P(
                "Analyze how different topics resonated before and after the election.",
                style={
                    "textAlign": "center",
                    "fontSize": "18px",
                    "color": "#555",
                    "marginBottom": "40px",
                    "maxWidth": "800px",
                    "marginLeft": "auto",
                    "marginRight": "auto",
                },
            ),
            html.Div(
    children=[
        html.Label(
            "Select Data Source:",
            style={
                "fontSize": "18px",
                "marginBottom": "10px",
                "fontWeight": "bold",
                "textAlign": "center",
            },
        ),
        html.P(
            "Choose between analyzing Reddit comments or posts. Comments provide granular insights, while posts capture broader sentiment trends.",
            style={
                "fontSize": "14px",
                "color": "#555",
                "marginTop": "5px",
                "marginBottom": "20px",
                "textAlign": "center",
                "lineHeight": "1.5",
            },
        ),
        dcc.RadioItems(
            id="data-toggle",
            options=[
                {"label": "Comments", "value": "comments"},
                {"label": "Posts", "value": "posts"}
            ],
            value="comments",  # Default value
            inline=True,
        ),
    ],
    style={
        "textAlign": "center",
                    "padding": "20px",
                    "backgroundColor": "#fff",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "borderRadius": "10px",
                    "marginBottom": "30px",
    },
),
            html.Div(
                children=[
                    html.Label(
                        "Select Topic:",
                        style={
                            "fontSize": "20px",
                            "fontWeight": "bold",
                            "marginBottom": "10px",
                            "display": "block",
                        },
                    ),
                    dcc.Dropdown(
                        id="keyword-dropdown",
                        options=[{"label": kw, "value": kw} for kw in df["Topic"].unique()],
                        value=df["Topic"].unique()[0] if not df.empty else None,
                        style={
                            "width": "60%",
                            "margin": "auto",
                            "padding": "10px",
                            "borderRadius": "5px",
                            "border": "1px solid #ddd",
                        },
                    ),
                ],
                style={
                    "textAlign": "center",
                    "padding": "20px",
                    "backgroundColor": "#fff",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "borderRadius": "10px",
                    "marginBottom": "30px",
                },
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H2(
                                "Before the Election",
                                style={
                                    "textAlign": "center",
                                    "color": "#333",
                                    "marginBottom": "10px",
                                    "fontSize": "24px",
                                },
                            ),
                            dcc.Graph(
                                id="hover-map-before",
                                config={"displayModeBar": False},
                                style={
                                    "backgroundColor": "#f7f7f7",
                                    "borderRadius": "10px",
                                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                },
                            ),
                        ],
                        style={
                            "width": "48%",
                            "padding": "20px",
                            "backgroundColor": "#fff",
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                            "borderRadius": "10px",
                        },
                    ),
                    html.Div(
                        children=[
                            html.H2(
                                "After the Election",
                                style={
                                    "textAlign": "center",
                                    "color": "#333",
                                    "marginBottom": "10px",
                                    "fontSize": "24px",
                                },
                            ),
                            dcc.Graph(
                                id="hover-map-after",
                                config={"displayModeBar": False},
                                style={
                                    "backgroundColor": "#f7f7f7",
                                    "borderRadius": "10px",
                                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                },
                            ),
                        ],
                        style={
                            "width": "48%",
                            "padding": "20px",
                            "backgroundColor": "#fff",
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                            "borderRadius": "10px",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "gap": "20px",
                },
            ),
        ],
    )


# Export layouts
__all__ = ["home_layout", "analysis_layout", "create_detailed_analysis_layout"]

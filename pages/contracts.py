# pages/weights.py

from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from dash.dependencies import Input, Output

load_dotenv()
mongodb_connection_string = os.getenv("MONGODB_CONNECTION_STRING")

# Define the layout for the weights page
def create_contracts_page(app):
    # Read the CSV data
    df = pd.read_csv("data/weights.csv")
    mongo_client = MongoClient(mongodb_connection_string)
    db = mongo_client["fpds"]
    collection = db["contracts"]

    cursor = collection.find()
    mongo_data = list(cursor)
    df = pd.DataFrame(mongo_data)



    weights_layout = html.Div([



     dcc.Input(id='search-input', type='text', placeholder='Enter search query...'),
     html.Div(id='search-output'),



        html.Br(),
        # dcc.Graph(
        #     id="weights-chart2",
        #     config={"displayModeBar": False},
        #     figure={
        #         "data": [
        #             go.Scatter(
        #                 x=df["date"],
        #                 y=df["contracts"],
        #                 mode="lines",
        #                 marker={"color": "blue"},
        #             )
        #         ],
        #         "layout": go.Layout(
        #             title="Weight Data",
        #             xaxis={"title": "Date"},
        #             yaxis={"title": "Weight"},
        #         ),
        #     },
        #     style={"width": "80%", "position": "absolute", "left": "10%","top": "50%"},
        # ),
        # dcc.Interval(
        #     id="graph-interval",
        #     interval=10 * 1000,  # Refresh every 60 seconds (adjust as needed)
        #     n_intervals=0,
        # ),

    ])
    @app.callback(
        Output("weights-chart2", "figure"),
        [Input("graph-interval", "n_intervals")]
    )
    def update_graph(n):
        # Fetch data from MongoDB
        cursor = collection.find()
        mongo_data = list(cursor)
        df = pd.DataFrame(mongo_data)

        # Create a new figure with updated data
        figure = {
            "data": [
                go.Scatter(
                    x=df["date"],
                    y=df["contract_id"],
                    mode="lines",
                    marker={"color": "blue"},
                )
            ],
            "layout": go.Layout(
                title="contracts Data",
                xaxis={"title": "Date"},
                yaxis={"title": "Contract_ID"},
            ),
        }

        return figure


    @app.callback(
        Output('search-output', 'children'),
        [Input('search-input', 'value')]
    )
    def update_search_output(search_query):
        if search_query is None:
            return ''
        else:
            cursor = collection.find()
            mongo_data = list(cursor)
            df = pd.DataFrame(mongo_data)


            return f"You searched for: {df['contracts']}"




    return weights_layout

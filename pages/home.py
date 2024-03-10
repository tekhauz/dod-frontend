# pages/home.py

import dash
from dash import dcc, html
import plotly.graph_objs as go
from utils import mongi
import os



mongodb_connection_string = os.getenv("MONGODB_CONNECTION_STRING")
mongo_client = mongi.MongoHandler(mongodb_connection_string)
mongo_client.count_documents()

# Create sample data for the graph
x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 15, 25, 30]
labels = ['AIR FORCE', 'NAVY', 'ARMY', 'DEFENSE LOGISTICS AGENCY', 'MISSILE DEFENSE AGENCY', 'U.S. SPECIAL OPERATIONS COMMAND', 'DEFENSE ADVANCED RESEARCH PROJECTS AGENCY', 'WASHINGTON HEADQUARTERS SERVICES', 'U.S. TRANSPORTATION COMMAND']
values = [10, 20, 30, 5, 10, 8, 6, 4, 7]  # Placeholder values, replace with your actual data

# Create the layout
home_layout = html.Div([
    html.Br(),
    html.H1("Welcome to the Federal Procument Data System"),
    html.Div(className='row1', children=[
        html.Div(className='home-graphs', children=[
dcc.Graph(
    id='contracts-graph',
    figure={
        'data': [
            go.Pie(
                labels=labels,
                values=values,
                hole=0.4,  # Hole size, set to 0 for a regular pie chart
                showlegend=False  # Remove legend from the pie chart
               
            )
        ],
        'layout': go.Layout(
            title='Contracts Pie Chart',
            height=400,  # Increase the height to make the chart bigger
            hovermode='closest',
            margin=dict(l=50, r=50, t=50, b=50),  # Adjust margin to fit the chart properly
            font=dict(size=12),  # Set the font size of labels
        )
    }
)

                 ]),
        html.Div(className='separatorv'),
        html.Div(className='home-graphs', children=[
            dcc.Graph(
                id='companies-graph',
                figure={
                    'data': [
                        go.Scatter(
                            x=x_values,
                            y=y_values,
                            mode='lines+markers',
                            name='Sample Data'
                        )
                    ],
                    'layout': go.Layout(
                        title='Companies Graph',
                        xaxis={'title': 'X-axis'},
                        yaxis={'title': 'Y-axis'},
                        height=400,
                        hovermode='closest'
                    )
                }
            ),
        ]),
        html.Div(className='separatorv'),
        html.Div(className='home-graphs', children=[
            dcc.Graph(
                id='finance-graph',
                figure={
                    'data': [
                        go.Scatter(
                            x=x_values,
                            y=y_values,
                            mode='lines+markers',
                            name='Sample Data'
                        )
                    ],
                    'layout': go.Layout(
                        title='Finance Graph',
                        xaxis={'title': 'X-axis'},
                        yaxis={'title': 'Y-axis'},
                        height=400,
                        hovermode='closest'
                    )
                }
            ),
        ]),
    ]),


















    html.Div(className='separatorh'),
    html.Hr(),
    html.Div(className='row2', children=[
        html.Div(className='home-graphs', children=[
            dcc.Graph(
                id='sample-graph',
                figure={
                    'data': [
                        go.Scatter(
                            x=x_values,
                            y=y_values,
                            mode='lines+markers',
                            name='Sample Data'
                        )
                    ],
                    'layout': go.Layout(
                        title='History Graph',
                        xaxis={'title': 'X-axis'},
                        yaxis={'title': 'Y-axis'},
                        height=400,
                        hovermode='closest'
                    )
                }
            ),
        ]),
        html.Div(className='separatorv'),
        html.Div(className='home-graphs', children=[
            dcc.Graph(
                id='companies-graph',
                figure={
                    'data': [
                        go.Scatter(
                            x=x_values,
                            y=y_values,
                            mode='lines+markers',
                            name='Sample Data'
                        )
                    ],
                    'layout': go.Layout(
                        title='Grants Graph',
                        xaxis={'title': 'X-axis'},
                        yaxis={'title': 'Y-axis'},
                        height=400,
                        hovermode='closest'
                    )
                }
            ),
        ]),
        html.Div(className='separatorv'),
        html.Div(className='home-graphs', children=[
            dcc.Graph(
                id='projects-graph',
                figure={
                    'data': [
                        go.Scatter(
                            x=x_values,
                            y=y_values,
                            mode='lines+markers',
                            name='Sample Data'
                        )
                    ],
                    'layout': go.Layout(
                        title='Projects Graph',
                        xaxis={'title': 'X-axis'},
                        yaxis={'title': 'Y-axis'},
                        height=400,
                        hovermode='closest'
                    )
                }
            ),
        ]),
    ]),



])

# Run the app
app = dash.Dash(__name__)
app.layout = home_layout

if __name__ == '__main__':
    app.run_server(debug=True)

# pages/home.py

import dash
from dash import dcc, html
import plotly.graph_objs as go
from utils import mongi

# Create sample data for the graph
x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 15, 25, 30]

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
                        go.Scatter(
                            x=x_values,
                            y=y_values,
                            mode='lines+markers',
                            name='Sample Data'
                        )
                    ],
                    'layout': go.Layout(
                        title='Contracts Graph',
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

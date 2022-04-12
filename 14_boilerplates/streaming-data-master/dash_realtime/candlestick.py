import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    # dcc.Checklist(
    #     id='toggle-rangeslider',
    #     options=[{'label': 'Include Rangeslider',
    #               'value': 'slider'}],
    #     value=['slider']
    # ),
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # in milliseconds
        n_intervals=0
    ),
    dcc.Graph(id="graph"),
])

import time
def gen(data):
    while 1:
        time.sleep(1)
        for i in range(len(data.index)):
            yield data.iloc[i]


@app.callback(
    Output("graph", "figure"),
    # [Input("toggle-rangeslider", "value")],
    [Input('interval-component', "n_intervals")]
)
def display_candlestick(value):
    df = next(gen(df))
    df2 = df.copy()
    fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['AAPL.Open'],
        high=df['AAPL.High'],
        low=df['AAPL.Low'],
        close=df['AAPL.Close']
    ))

    # fig.update_layout(
    #     xaxis_rangeslider_visible='slider' in value
    # )

    return fig


app.run_server(debug=True)

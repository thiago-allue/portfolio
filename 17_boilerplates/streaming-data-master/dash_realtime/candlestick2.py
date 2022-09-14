from dash.dependencies import Output, Input
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go

dados = np.array([[1509608700000, 0.00002246, 0.00002246, 0.00002246, 0.00002246, 100.00000000, 1509609599999],
                  [1509609600000, 0.00002800, 0.00002802, 0.00002800, 0.00002800, 6832.00000000, 1509610499999],
                  [1509610500000, 0.00002700, 0.00002700, 0.00002501, 0.00002501, 3936.00000000, 1509611399999],
                  [1509611400000, 0.00002588, 0.00002678, 0.00002588, 0.00002614, 7125.00000000, 1509612299999],
                  [1509612300000, 0.00002615, 0.00002621, 0.00002614, 0.00002617, 19318.00000000, 1509613199999],
                  [1509613200000, 0.00002627, 0.00002643, 0.00002625, 0.00002627, 109218.00000000, 1509614099999],
                  [1509614100000, 0.00002627, 0.00002642, 0.00002603, 0.00002639, 134825.00000000, 1509614999999],
                  [1509615000000, 0.00002639, 0.00002655, 0.00002616, 0.00002618, 74432.00000000, 1509615899999]
                  ])

columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time']

df = pd.DataFrame(data=dados, columns=columns)

last_id = 0

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div(className='container-fluid', children=
    [
        html.Div(className='row',
                 children=html.Div(dcc.Graph(id='live-graph', animate=True), className='col s12 m12 l12')),
        dcc.Interval(
            id='graph-update',
            interval=5000
        )
    ]),
)


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'interval')]
)
def graph_update(interval):
    global df

    ndf = df.iloc[0:2]
    print(ndf)

    last_id = ndf.iloc[0]['open_time']

    ndf['data'] = pd.to_datetime(ndf['open_time'], unit='ms')
    ndf.set_index('open_time', inplace=True)
    ndf.round({'close': 8, 'open': 8, 'high': 8, 'low': 8})

    data = [dict(
        type='candlestick',
        open=ndf.open * 10e6,
        high=ndf.high * 10e6,
        low=ndf.low * 10e6,
        close=ndf.close * 10e6,
        x=ndf.data,
        yaxis='y2',
        name='Ripple',
    )]

    df = df.iloc[2:]
    print(df)

    return {'data': data, 'layout': {'title': str(last_id)}}


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_js:
    app.scripts.append_script({'external_url': js})

server = app.server
dev_server = app.run_server(debug=True)

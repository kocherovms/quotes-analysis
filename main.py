import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas
import pandas_datareader.data
from statsmodels.tsa.seasonal import seasonal_decompose

from lib.stock_list import stock_list

MIN_YEAR = 2010
MAX_YEAR = 2019

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='Seasonality analysis of stock quotes'),
    dcc.Dropdown(
        id='stock-code',
        options=[{'label': '{} / {} ({})'.format(stock_list[e]['name'], stock_list[e]['type'], e), 'value': e} for e in
                 stock_list]
    ),
    html.H3(children='Quotes range'),
    html.Div([
        html.Div([
            dcc.RangeSlider(
                id='date-range',
                min=MIN_YEAR,
                max=MAX_YEAR,
                step=1,
                value=[MIN_YEAR, MAX_YEAR],
                marks={r: str(r) for r in range(MIN_YEAR, MAX_YEAR + 1)},
                allowCross=False
            )],
            style={'height': '50px', 'margin': '30px'}
        ),
        html.Div([
            dcc.Dropdown(
                id='freq',
                options=[{'label': x, 'value': x} for x in list(range(30, 360, 30)) + [365]],
                value=365
            )], style={'height': '50px', 'margin': '30px'}
        )]
    ),
    dcc.Graph(
        id='quotes-graph',
    ),
    dcc.Graph(
        id='trend-graph',
    ),
    dcc.Graph(
        id='seasonality-graph',
    ),
    dcc.Graph(
        id='residual-graph',
    ),
])

@app.callback(
    [
        Output('quotes-graph', 'figure'),
        Output('trend-graph', 'figure'),
        Output('seasonality-graph', 'figure'),
        Output('residual-graph', 'figure')
    ],
    [
        Input(component_id='stock-code', component_property='value'),
        Input(component_id='date-range', component_property='value'),
        Input(component_id='freq', component_property='value')
    ]
)
def draw_seasonal_plots(stock_code, date_range, freq):
    if not stock_code:
        return [{}, {}, {}, {}]

    start_date = '{}-01-01'.format(date_range[0])
    end_date = '{}-01-01'.format(date_range[1] + 1)

    quotes = pandas.DataFrame()
    df = pandas_datareader.data.DataReader('{}.ME'.format(stock_code), 'yahoo', start_date, end_date)
    df['SECID'] = stock_code
    df = df.rename(index=str, columns={'Close': 'CLOSE'})
    df = df[['SECID', 'CLOSE']]
    df.index = pandas.to_datetime(df.index, format="%Y-%m-%d")
    quotes = quotes.append(df)

    current_date = None
    current_close = None

    quotes.sort_index(inplace=True)
    new_rows = pandas.DataFrame()

    for index, row in quotes.iterrows():
        if current_date and (index - current_date > pandas.Timedelta('1 days')):
            date_in_loop = current_date + pandas.Timedelta('1 days')

            while date_in_loop < index:
                new_row = pandas.DataFrame({'SECID': stock_code, 'CLOSE': current_close}, index=[date_in_loop])
                new_rows = new_rows.append(new_row, verify_integrity=True)
                date_in_loop = date_in_loop + pandas.Timedelta('1 days')

        current_date = index
        current_close = row['CLOSE']

    quotes = quotes.append(new_rows, verify_integrity=True)
    quotes.sort_index(inplace=True)

    pure_quotes = quotes[['CLOSE']]
    freq = freq
    quotes_part = seasonal_decompose(pure_quotes, model='multiplicative', freq=freq)

    return [
        {
            'data': [compute_figure_data(quotes)],
            'layout': {
                'title': 'Quotes'
            }
        },
        {
            'data': [compute_figure_data(quotes_part.trend)],
            'layout': {
                'title': 'Trend'
            }
        },
        {
            'data': [compute_figure_data(quotes_part.seasonal)],
            'layout': {
                'title': 'Seasonality'
            }
        },
        {
            'data': [compute_figure_data(quotes_part.resid)],
            'layout': {
                'title': 'Residual'
            }
        },
    ]


def compute_figure_data(df):
    result = {'x': [], 'y': [], 'type': 'line'}

    for index, row in df.iterrows():
        result['x'].append(index)
        result['y'].append(row['CLOSE'])

    return result


if __name__ == '__main__':
    app.run_server(debug=True)

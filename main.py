import json
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Output, Input, State
import pandas
import pandas_datareader.data
from statsmodels.tsa.seasonal import seasonal_decompose

from lib.stock_list import stock_list

MIN_YEAR = 2010
MAX_YEAR = 2019

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Stock Insights'
app.layout = html.Div(children=[
    html.H1(children='Seasonality analysis of stock quotes'),

    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(['Stock code on MOEX'], htmlFor='stock-code'),
                            dcc.Dropdown(
                                id='stock-code',
                                options=[
                                    {'label': '{} / {} ({})'.format(e, stock_list[e]['name'], stock_list[e]['type']),
                                     'value': e} for e in
                                    stock_list],
                                optionHeight=60,
                            ),
                            html.Br(),
                            html.Label(['Date range'], htmlFor='date-range'),
                            dcc.RangeSlider(
                                id='date-range',
                                min=MIN_YEAR,
                                max=MAX_YEAR,
                                step=1,
                                value=[MIN_YEAR, MAX_YEAR],
                                marks={r: str(r) for r in range(MIN_YEAR, MAX_YEAR + 1)},
                                allowCross=False,
                                className='range-slider'
                            ),
                            html.Br(),
                            html.Br(),
                            html.Label(['Period (days)'], htmlFor='period'),
                            dcc.Dropdown(
                                id='period',
                                options=[{'label': x, 'value': x} for x in [365] + list(range(330, 0, -30))],
                                value=365,
                                clearable=False,
                                searchable=False
                            ),
                            html.Br(),
                            html.Label(['Analysis type'], htmlFor='analysis-type'),
                            dcc.RadioItems(
                                id='analysis-type',
                                options=[
                                    {'label': 'Multiplicative', 'value': 'multiplicative'},
                                    {'label': 'Additive', 'value': 'additive'},
                                ],
                                value='multiplicative'
                            ),
                            html.Br(),
                            html.Label(['Seasonality graph type'], htmlFor='seasonality-graph-type'),
                            dcc.RadioItems(
                                id='seasonality-graph-type',
                                options=[
                                    {'label': 'Smooth', 'value': 'smooth'},
                                    {'label': 'Raw', 'value': 'raw'},
                                ],
                                value='smooth'
                            )
                        ],
                        style={'position': 'sticky', 'top': '0'}
                    )
                ],
                style={'width': '100px', 'margin': '10px', 'flex-grow': '1'}
            ),
            html.Div(
                [
                    dcc.Loading(
                        [
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
                            html.Label(['Residual stats'], htmlFor='residual-stats'),
                            dash_table.DataTable(
                                id='residual-stats',
                                columns=[
                                    {"name": 'Stat', "id": 'index'},
                                    {"name": 'Value', "id": 'CLOSE'},
                                ]
                            )
                        ]),
                ],
                style={'width': '100px', 'margin': '10px', 'flex-grow': '3'}
            ),
            html.Div(id='quotes-storage', style={'display': 'none'})
        ],
        style={'display': 'flex'}
    )
])


@app.callback(
    [
        Output('quotes-graph', 'figure'),
        Output('trend-graph', 'figure'),
        Output('seasonality-graph', 'figure'),
        Output('residual-graph', 'figure'),
        Output('residual-stats', 'data'),
        Output('quotes-storage', 'children'),
    ],
    [
        Input('stock-code', 'value'),
        Input('date-range', 'value'),
        Input('period', 'value'),
        Input('analysis-type', 'value'),
        Input('seasonality-graph-type', 'value'),
    ],
    [
        State('quotes-storage', 'children')
    ]
)
def draw_seasonal_plots(stock_code, date_range, period, analysis_type, seasonality_graph_type, quotes_storage):
    if not stock_code:
        return [{}, {}, {}, {}, [], quotes_storage]

    start_date = '{}-01-01'.format(date_range[0])
    end_date = '{}-01-01'.format(date_range[1] + 1)

    if quotes_storage:
        quotes_storage = json.loads(quotes_storage)

    if quotes_storage and \
            quotes_storage.get('stock_code', '') == stock_code and \
            quotes_storage.get('start_date', '') == start_date and \
            quotes_storage.get('end_date', '') == end_date:
        quotes = pandas.read_json(quotes_storage.get('quotes', None))
    else:
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
    quotes_part = seasonal_decompose(pure_quotes, model=analysis_type, freq=period)

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
            'data': [compute_seasonal_figure_data(quotes_part.seasonal, period, seasonality_graph_type)],
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
        quotes_part.resid.describe(include='all').reset_index().to_dict('records'),
        json.dumps({
            'stock_code': stock_code,
            'start_date': start_date,
            'end_date': end_date,
            'quotes': quotes.to_json()
        })
    ]


def compute_figure_data(df):
    result = {'x': [], 'y': [], 'type': 'line'}

    for index, row in df.iterrows():
        result['x'].append(index)
        result['y'].append(row['CLOSE'])

    return result


def compute_seasonal_figure_data(df, period, seasonality_graph_type):
    if seasonality_graph_type == 'smooth':
        # TODO: for OBUV - this xxx doesn't handle missing values
        df_part = seasonal_decompose(df, freq=30)
        df = df_part.trend

    months = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec',
    }
    result = {'x': [], 'y': [], 'type': 'line'}
    day = 1
    date = pandas.Timestamp('2019-01-01')

    for index, row in df.iterrows():
        if day > period:
            break

        result['x'].append('{} {}'.format(months.get(date.month, '?'), date.day))
        result['y'].append(row['CLOSE'])
        date = date + pandas.Timedelta('1 days')
        day += 1

    return result


if __name__ == '__main__':
    is_debug = True if os.environ.get('DEBUG', False) else False
    app.run_server(debug=is_debug, host='0.0.0.0', port=int(os.environ.get('PORT', 0)))

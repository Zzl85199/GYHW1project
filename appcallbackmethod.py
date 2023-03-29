import dash
import pandas as pd
from dash import html, dcc, Output, Input, State

app = dash.Dash(__name__)
def meth():
    @app.callback(Output('page-content', 'children'),Input('url', 'pathname'))
    def display_page(pathname):
        if pathname == '/index':
            return index_layout
        elif pathname == '/data':
            from data import data_layout
            return data_layout
        elif pathname == '/chart':
            from chart import chart_layout
            return chart_layout
        elif pathname == '/predict':
            from predict import predict_layout
            return predict_layout
        return index_layout

    @app.callback(
        Output("gender", "children"),
        [Input("submit", "n_clicks")],
        [State("input", "value")]
    )
    def search(n_clicks,inputs):
        if n_clicks > 0:
            gender_data = df.loc[df['subject_id'] == inputs, 'gender'].values
            if len(gender_data) > 0:
                return gender_data[0]
            else:
                return "找不到相對應的資料"
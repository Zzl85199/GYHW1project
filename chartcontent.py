import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
from dash.dependencies import Input, Output, State

df = pd.read_csv('data/PATIENTS_6.csv')

def chartcontent_layout():
    return html.Div([
        html.Div([
            dcc.Input(
                id='input',
                type='number',
                value='',
                placeholder="請輸入病人編號",
                style={'width': '50%'}
            ),
            dbc.Button("查詢", outline=True, id="submit", color="primary", n_clicks=0, className="ml-2"),
            html.H6("患者資料圖表："),
            html.Div(["性別：", html.Div(id="gender")])
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = chartcontent_layout()

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

if __name__ == "__main__":
    app.run_server(debug=False)

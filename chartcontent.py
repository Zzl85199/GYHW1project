import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
import datetime

start_date = datetime.datetime(2021, 1, 1, 4, 0, 0)  # 設定最早和最晚的日期
end_date = datetime.datetime(2023, 12, 31, 10, 0, 0)
start_ts = int(start_date.timestamp())  # 將日期轉換為unix timestamp
end_ts = int(end_date.timestamp())
start_str = start_date.strftime('%Y/%m/%d %H:%M')
end_str = end_date.strftime('%Y/%m/%d %H:%M')

def Agechange(dobtime,datatime):
    return [str(datatime.year - dobtime.year - ((dobtime.month, dobtime.day) < (dobtime.month, dobtime.day)))]

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
            html.Div(
                dcc.Slider(
                    id='date-slider',
                    min=start_ts,
                    max=end_ts,
                    step=3600,  # 一天的秒數
                    value=start_ts,
                    marks={
                        start_ts: start_str,
                        end_ts: end_str
                    }
                ),
                style={'padding-left': '30px','padding-right': '10px'}
            ),
            html.H6("患者圖表資料："),
            dbc.Container([
                dbc.Row([
                    dbc.Col(html.Div(["年齡：", html.Div(id="age")]), width=4, className="col-lg-3 col-md-3 col-sm-3 col-xs-3 border border-dark"),
                    dbc.Col(html.Div(["性別：", html.Div(id="gender")]), width=4, className="col-lg-3 col-md-3 col-sm-3 col-xs-3 border border-dark"),
                    dbc.Col(html.Div(["ICU類型：",html.Div(id="ICU")]), width=4, className="col-lg-3 col-md-3 col-sm-3 col-xs-3 border border-dark"),
                ], justify="center"),
                dbc.Row([
                    dbc.Col(html.Div(["哥斯拉哥量表：",html.Div(id="glasgow")]), width=4, className="col-lg-3 col-md-3 col-sm-3 col-xs-3 border border-dark"),
                    dbc.Col(html.Div(["機械通氣狀態：",html.Div(id="vent")]), width=4, className="col-lg-3 col-md-3 col-sm-3 col-xs-3 border border-dark"),
                    dbc.Col(html.Div(["尿量：",html.Div(id="urine")]), width=4, className="col-lg-3 col-md-3 col-sm-3 col-xs-3 border border-dark"),
                ], justify="center"),
                dbc.Row(
                    dbc.Col(html.Hr())
                ),
            ],fluid=True),
            dbc.Container([
                dbc.Row([
                    dbc.Col(html.H6("體溫"), width=3),
                    dbc.Col(html.H6("心率"), width=3),
                    dbc.Col(html.H6("收縮、舒張及血壓"), width=3),
                    dbc.Col(html.H6("BMI"), width=3)
                ], justify="center"),
                dbc.Row([
                    dbc.Col(html.Img(src='/assets/temperature.jpg'), width=3),
                    dbc.Col(html.Img(src='/assets/heartrate.jpg'), width=3),
                    dbc.Col(html.Img(src='/assets/presure.jpg'), width=3),
                    dbc.Col(html.Img(src='/assets/BMI.jpg'), width=3)
                ]),
                dbc.Row(
                    dbc.Col(html.Br())
                )
            ],fluid=True),
            dbc.Container([
                dbc.Row([
                    dbc.Col(html.H6("呼吸率"), width=4),
                    dbc.Col(html.H6("血氧飽和度"), width=4),
                    dbc.Col(html.H6("吸入氧分率"), width=4)
                ], justify="center"),
                dbc.Row([
                    dbc.Col(html.Img(src='/assets/inspirerate.jpg'), width=4),
                    dbc.Col(html.Img(src='/assets/Spo2.jpg'), width=4),
                    dbc.Col(html.Img(src='/assets/Fio2.jpg'), width=4),
                ]),
            ],fluid=True),
        ])
    ])
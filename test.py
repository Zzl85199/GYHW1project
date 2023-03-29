import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc, Output, Input, State
from Navbar import navbar_layout
import datetime
import numpy as np
from chartcontent import Agechange

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_url_path='/assets/')
PATIENTS_df = pd.read_csv('data/PATIENTS_6.csv')
OUTPUTEVENTS_df = pd.read_csv('data/OUTPUTEVENTS_6.csv')
CHARTEVENTS_df = pd.read_csv('data/CHARTEVENTS_6.csv')
ICUSTAYS_df = pd.read_csv('data/ICUSTAYS_6.csv')
#limitdatetime = datetime.datetime(1970, 1, 1, 0, 0, 0)

index_layout=html.Div(
    children=[
        navbar_layout(),
        dbc.Container([
            dbc.Row([
                dbc.Col(html.H1("我們日以繼夜廢寢忘食的成果"), className="text-center my-5")
            ]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.P("這個網頁是我們用心凝聚而成的作品，經歷無數個不眠之夜，用無盡的汗水和熱情鑄造而成。"),
                    html.P("我們融合了設計的美感、技術的精湛和創意的靈感，只為了呈現出一個完美的世界，希望您能夠在其中感受到我們對於美好事物的熱愛和追求。")
                ], className="text-center my-3"), className="text-center my-3")
            ]),
            dbc.Row([
                dbc.Col(html.P("以下是我們採用的mimic-III資料："), className="text-center my-1")
            ]),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("ADMISSIONS", className="card-title"),
                        html.P("在這個頁面中你可以查看有關患者入院的訊息，包含患者出入院時間、入院來源等資料。", className="card-text"),
                        dbc.Button("進入", color="primary", href="/patient_list")
                    ])
                ], className="shadow p-3 mb-5 bg-white rounded"), width=3, className="mx-auto my-3"),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("CHARTEVENT", className="card-title"),
                        html.P("在這個頁面中你可以查看患者在ICU期間的數據，包含生命體徵、精神狀態等。", className="card-text"),
                        dbc.Button("進入", color="primary", href="/patient_data")
                    ])
                ], className="shadow p-3 mb-5 bg-white rounded"), width=3, className="mx-auto my-3"),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("ICUSTAYS", className="card-title"),
                        html.P("在這個頁面中你可以查看患者入住ICU的資訊，紀錄進入到離開ICU的時間及入住的ICU種類等。", className="card-text"),
                        dbc.Button("進入", color="primary", href="/patient_data")
                    ])
                ], className="shadow p-3 mb-5 bg-white rounded"), width=3, className="mx-auto my-3")
            ]),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("LABEVENTS", className="card-title"),
                        html.P("在這個頁面中你可以查看實驗室取得患者測量值數據，如白血球、紅血球須化驗的資料等。", className="card-text"),
                        dbc.Button("進入", color="primary", href="/patient_data")
                    ])
                ], className="shadow p-3 mb-5 bg-white rounded"), width=3, className="mx-auto my-3"),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("OUTPUTEVENTS", className="card-title"),
                        html.P("在這個頁面中你可以查看患者輸出的資料，如:液體輸出數據(尿液等)、輸液是否中斷的資訊等。", className="card-text"),
                        dbc.Button("進入", color="primary", href="/patient_data")
                    ])
                ], className="shadow p-3 mb-5 bg-white rounded"), width=3, className="mx-auto my-3"),dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H5("PATIENTS", className="card-title"),
                        html.P("在這個頁面中你可以查看患者基本資料，如:性別、出生日期等。", className="card-text"),
                        dbc.Button("進入", color="primary", href="/patient_data")
                    ])
                ], className="shadow p-3 mb-5 bg-white rounded"), width=3, className="mx-auto my-3")
            ])
        ])
    ]
    ,style={'backgroundColor': '#f0f0f0', 'height': '1000px', "overflow-y": "scroll"} 
)                  

#設定路由 dcc.Location ->偵測URL並回傳給回調函數    
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id='page-content')
])    

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
    [Output("gender", "children"),Output("date-slider", "min"),Output("date-slider", "max"),Output('date-slider', 'marks'),Output("urine", "children"),Output("age", "children"),Output("ICU", "children"),Output("vent", "children"),Output("glasgow", "children")],
    [Input("submit", "n_clicks")],
    [State("input", "value")]
)
def search(n_clicks,inputs):
    if n_clicks > 0:
        gender_data = PATIENTS_df.loc[PATIENTS_df['subject_id'] == inputs, 'gender'].values

        charttime = OUTPUTEVENTS_df.loc[OUTPUTEVENTS_df['subject_id'] == inputs, 'charttime'].values
        start = datetime.datetime.strptime(min(charttime), '%Y/%m/%d %H:%M')
        start_ts = int(start.timestamp())
        start_str = min(charttime)
        end = datetime.datetime.strptime(max(charttime), '%Y/%m/%d %H:%M')
        end_ts = int(end.timestamp())
        end_str = max(charttime)
        mark={
            start_ts: start_str,
            end_ts: end_str
        }
        
        #charteventCharttime = pd.to_datetime(np.unique(charteventdf.loc[charteventdf['subject_id'] == inputs, 'charttime'].values))
        #start = min(charteventCharttime).date() - datetime.timedelta(days=365*200)
        #start_ts = int((datetime.datetime(start.year, start.month, start.day) - limitdatetime).total_seconds())
        #start_str = start.strftime('%Y-%m-%d')
        #end = max(charteventCharttime).date() - datetime.timedelta(days=365*200)
        #end_ts = int((datetime.datetime(end.year, end.month, end.day) - limitdatetime).total_seconds())
        #end_str = end.strftime('%Y-%m-%d')
        #mark = {start_ts:start_str,end_ts:end_str}
        
        urine_data = OUTPUTEVENTS_df.loc[OUTPUTEVENTS_df['subject_id'] == inputs]
        urine_data.set_index('charttime')
        urine_data = urine_data.loc[urine_data['charttime'] == end_str]
        urine_data = urine_data.loc[urine_data.index.min(),'value']
        
        age_data = PATIENTS_df.loc[PATIENTS_df['subject_id'] == inputs, 'DOB'].values
        age_data = Agechange(datetime.datetime.strptime(age_data[0], '%Y/%m/%d %H:%M'), datetime.datetime.strptime(min(charttime), '%Y/%m/%d %H:%M'))
        
        icu_data = ICUSTAYS_df.loc[ICUSTAYS_df['SUBJECT_ID'] == inputs]
        icu_data.set_index('INTIME')
        icu_data = icu_data.loc[icu_data['INTIME'].index.max(), 'LAST_CAREUNIT']
        
        vent_data = CHARTEVENTS_df.loc[CHARTEVENTS_df['subject_id'] == inputs]
        vent_data = vent_data.loc[vent_data['itemid'] == 223848]
        vent_data.set_index('charttime')
        vent_data = vent_data.loc[vent_data['charttime'].index.max(), 'valuenum']
        if vent_data == 1:
            vent_data = "on"
        else:
            vent_data = "off"
        
        glasgow_data = CHARTEVENTS_df.loc[CHARTEVENTS_df['subject_id'] == inputs]
        glasgow_data_eye = glasgow_data.loc[glasgow_data['itemid'] == 220739]
        glasgow_data_eye.set_index('charttime')
        glasgow_data_eye = glasgow_data_eye.loc[glasgow_data_eye.index.max(), 'valuenum']
        glasgow_data_verbal = glasgow_data.loc[glasgow_data['itemid'] == 223900]
        glasgow_data_verbal.set_index('charttime')
        glasgow_data_verbal = glasgow_data_verbal.loc[glasgow_data_verbal.index.max(), 'valuenum']
        glasgow_data_motor = glasgow_data.loc[glasgow_data['itemid'] == 223901]
        glasgow_data_motor.set_index('charttime')
        glasgow_data_motor = glasgow_data_motor.loc[glasgow_data_motor.index.max(), 'valuenum']
        glasgow_data = "eye:" + str(glasgow_data_eye.astype(int)) + " verbal:" + str(glasgow_data_verbal.astype(int)) + " motor:" +str(glasgow_data_motor.astype(int))
           
    return gender_data[0], start_ts, end_ts, mark,urine_data, age_data, icu_data, vent_data, glasgow_data


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc, Output, Input, State
from Navbar import navbar_layout
import datetime
import numpy as np
from chartcontent import Agechange
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_url_path='/assets/')
PATIENTS_df = pd.read_csv('data/PATIENTS_6.csv')
OUTPUTEVENTS_df = pd.read_csv('data/OUTPUTEVENTS_6.csv')
CHARTEVENTS_df = pd.read_csv('data/CHARTEVENTS_6.csv')
ICUSTAYS_df = pd.read_csv('data/ICUSTAYS_6.csv')
limitdatetime = datetime.datetime(1970, 1, 1, 0, 0, 0)

start_date = datetime.datetime(2021, 1, 1, 4, 0, 0)  # 設定最早和最晚的日期
end_date = datetime.datetime(2023, 12, 31, 10, 0, 0)
start_ts = int(start_date.timestamp())  # 將日期轉換為unix timestamp
end_ts = int(end_date.timestamp())
start_str = start_date.strftime('%Y/%m/%d %H:%M')
end_str = end_date.strftime('%Y/%m/%d %H:%M')
mark = {start_ts:start_str,end_ts:end_str}

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
    [Output("gender", "children"),Output("date-slider", "min"),Output("date-slider", "max"),
     Output('date-slider', 'marks'),Output("urine", "children"),Output("age", "children"),
     Output("ICU", "children"),Output("vent", "children"),Output("glasgow", "children"),
     Output('graph', 'figure')],
    [Input("submit", "n_clicks")],
    [State("input", "value")],
    [State('date-slider', 'value')]
)
def search(n_clicks,inputs,date_range):
    global start_ts,start_str,end_ts,end_str,mark
    gender_data = [""]
    urine_data = ""
    age_data = ""
    icu_data = ""
    vent_data = ""
    glasgow_data = ""
    
    if n_clicks > 0:
        gender_data = PATIENTS_df.loc[PATIENTS_df['subject_id'] == inputs, 'gender'].values
        
        charteventCharttime = pd.to_datetime(np.unique(CHARTEVENTS_df.loc[(CHARTEVENTS_df['subject_id'] == inputs) & (CHARTEVENTS_df['itemid'] == 220045), 'charttime'].values))

        start = min(charteventCharttime).date()
        start_ts = int((datetime.datetime(start.year, start.month, start.day) - limitdatetime).total_seconds())
        start_str = start.strftime('%Y-%m-%d')
        end = max(charteventCharttime).date()
        end_ts = int((datetime.datetime(end.year, end.month, end.day) - limitdatetime).total_seconds())
        end_str = end.strftime('%Y-%m-%d')
        mark = {start_ts:start_str,end_ts:end_str}
        
        urine_data = OUTPUTEVENTS_df.loc[OUTPUTEVENTS_df['subject_id'] == inputs]
        urine_data.set_index('charttime')
        urine_data = urine_data.loc[urine_data.index.min(),'value']
        
        age_data = PATIENTS_df.loc[PATIENTS_df['subject_id'] == inputs, 'DOB'].values
        age_data = Agechange(datetime.datetime.strptime(age_data[0], '%Y/%m/%d %H:%M'), min(charteventCharttime))
        
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
        
        df_filtered = CHARTEVENTS_df[(CHARTEVENTS_df['subject_id'] == inputs) & (CHARTEVENTS_df['itemid'] == 220045)]
        df_filtered['charttime'] = pd.to_datetime(df_filtered['charttime'])
        df_filtered = df_filtered.sort_values(by=['charttime'])
        df_filtered['value'] = pd.to_numeric(df_filtered['value'])
        df_filtered = df_filtered.sort_values(by=['value'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_filtered['charttime'], y=df_filtered['value'], mode='markers'))
        fig.update_layout(title=f'心率圖統計表 Subject_id : {inputs} ', xaxis_title='日期', yaxis_title='心律(bpm)') 
        if (date_range[0] - start_ts) < 0:
            start_percent = 0
            end_percent = 1
        else:
            start_percent = (date_range[0] - start_ts) / (end_ts - start_ts)
            end_percent = (date_range[1] - start_ts) / (end_ts - start_ts)
        df_filtered = df_filtered.sort_values(by=['charttime'])
        start_index = int(start_percent * len(df_filtered['charttime']))
        end_index = int(end_percent * len(df_filtered['charttime']))-1
        start_value_str = df_filtered['charttime'].iloc[start_index].strftime("%Y-%m-%d %H:%M:%S")
        end_value_str = df_filtered['charttime'].iloc[end_index].strftime("%Y-%m-%d %H:%M:%S")
        start_value = (datetime.datetime.strptime((start_value_str), "%Y-%m-%d %H:%M:%S")).strftime("%Y/%-m/%-d %H:%M")
        end_value = (datetime.datetime.strptime((end_value_str), "%Y-%m-%d %H:%M:%S")).strftime("%Y/%-m/%-d %H:%M")
        start_datetime = datetime.datetime.strptime(start_value, "%Y/%m/%d %H:%M")
        end_datetime = datetime.datetime.strptime(end_value, "%Y/%m/%d %H:%M")
        fig.update_xaxes(range=[start_datetime, end_datetime])
           
        #print(start_percent)
        #print(end_percent)
        #print(len(df_filtered['charttime']))
        #print(start_index)
        #print(end_index)
        #print(start_value)
        #print(end_value)
        
    return gender_data[0], start_ts, end_ts, mark,urine_data, age_data, icu_data, vent_data, glasgow_data, fig

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input
from Navbar import navbar_layout
from chartcontent import chartcontent_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_url_path='/assets/')

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id='page-content')
])    
    
chart_layout=html.Div(
        children=[
        navbar_layout(),
        chartcontent_layout(),
        #圖表放置位子
        #dbc.Container([
        #    dbc.Row([
        #        dbc.Col(html.Div("Chart 1"), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #        dbc.Col(html.Div("Chart 2"), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #        dbc.Col(html.Div("Chart 3"), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #        dbc.Col(html.Div("Chart 4"), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #    ]),
        #    dbc.Row([
        #        dbc.Col(dbc.Row(["Chart 6","Chart 7"]), width=2),
        #        dbc.Col(html.Div("Chart 8"), width=2),
        #        dbc.Col(html.Div("Chart 9"), width=2),
        #        dbc.Col(html.Div("Chart 10"), width=2)
        #    ]),
        #    dbc.Row([
        #        dbc.Col(html.Div("Chart 11"), width=2),
        #        dbc.Col(html.Div("Chart 12"), width=2),
        #        dbc.Col(html.Div("Chart 13"), width=2),
        #    ]),
        #    dbc.Row([
        #        dbc.Col(html.Div("Chart 14"), width=2),
        #        dbc.Col(html.Div("Chart 15"), width=2),
        #        dbc.Col(html.Div("Chart 16"), width=2),
        #    ]),
        #]),
        #
        
        
        #dbc.Container([
        #    dbc.Row([
        #        dbc.Col(html.Div(["年齡：","*****引用資料"]), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #        dbc.Col(html.Div(["性別：", html.Div(id="gender")]), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #        dbc.Col(html.Div(["ICU類型：","*****引用資料"]), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #    ]),
        #    dbc.Row([
        #        dbc.Col(html.Div(["哥斯拉哥量表：","*****引用資料"]), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #        dbc.Col(html.Div(["機械通氣狀態：","*****引用資料"]), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #        dbc.Col(html.Div(["尿量：","*****引用資料"]), width=2, className="col-lg-3 col-md-3 col-sm-3 col-xs-3"),
        #    ]),
        #    
        #]),
        
        
        
        
        
        html.H1("圖表"),
        html.P("這是圖表"),
        
    ]
    ,style={'backgroundColor': '#f0f0f0', 'height': '1000px', "overflow-y": "scroll"}
    )

if __name__ == '__main__':
    app.run_server(debug=True)




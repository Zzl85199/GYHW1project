import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input
from Navbar import navbar_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_url_path='/assets/')

index_layout=html.Div(
    children=[
        navbar_layout(),
        html.H1("首頁"),
        html.P("這是首頁"),
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
    
if __name__ == '__main__':
    app.run_server(debug=True)
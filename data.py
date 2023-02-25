import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input
from Navbar import navbar_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_url_path='/assets/')

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id='page-content')
])    
    
data_layout=html.Div(
        children=[
        navbar_layout(),
        #網頁內容
        html.H1("原始資料頁面"),
        html.P("這是原始資料"),
        #網頁內容
    ]
    ,style={'backgroundColor': '#f0f0f0', 'height': '1000px', "overflow-y": "scroll"}
    )

if __name__ == '__main__':
    app.run_server(debug=True)




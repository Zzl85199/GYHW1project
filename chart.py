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
    ]
    ,style={'backgroundColor': '#f0f0f0', 'height': '1000px', "overflow-y": "scroll"}
    )

if __name__ == '__main__':
    app.run_server(debug=True)




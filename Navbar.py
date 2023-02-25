import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

def navbar_layout():
    return dbc.Navbar(
        dbc.Container([
            dbc.Row(
                [
                    dbc.Col(html.Img(src='/assets/brand.png', height="70px")),
                    dbc.Col(
                        dbc.NavbarBrand("Project web", className="ms-3 fs-1 fw-normal") 
                    ),
                ],
                align="center",
                className="g-0",
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("首頁", href="index"),className="text-decoration-underline fw-light fs-5"),
                            dbc.NavItem(dbc.NavLink("原始資料", href="data"),className="text-decoration-underline fw-light fs-5"),
                            dbc.NavItem(dbc.NavLink("統計圖表", href="chart"),className="text-decoration-underline fw-light fs-5"),
                            dbc.NavItem(dbc.NavLink("模型預測", href="predict"),className="text-decoration-underline fw-light fs-5"),
                        ],
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
        ]),
        color="white",
        dark=False,
        sticky="top",
    )

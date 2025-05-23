import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from login import login_layout, add_login_callback
from dashboard import dashboard
from orders import orders_view
from tracking import tracking_view_layout
from home import home
from predict import prediction_layout, add_predict_callback

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True)
server = app.server

app.layout = dbc.Container([
    dcc.Location(id="url"),
    dcc.Store(id="logueado-store", data=False),
    dcc.Store(id="usuario-store", data=""),
    dbc.NavbarSimple(
        brand="Red Logística Inteligente",
        brand_href="/",
        color="primary",
        dark=True,
        children=[
            dbc.NavItem(dcc.Link("Inicio", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Dashboard", href="/dashboard", className="nav-link")),
            dbc.NavItem(dcc.Link("Órdenes", href="/ordenes", className="nav-link")),
            dbc.NavItem(dcc.Link("Tracking", href="/tracking", className="nav-link")),
            dbc.NavItem(dcc.Link("Predicción ML", href="/prediccion", className="nav-link")),
            dbc.NavItem(dcc.Link("Cerrar sesión", href="/logout", className="nav-link"))
        ]
    ),
    html.Div(id="page-content")
], fluid=True)

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname"),
     Input("logueado-store", "data"),
     Input("usuario-store", "data")]
)
def display_page(pathname, logueado, usuario):
    if not logueado:
        if pathname == "/login":
            return login_layout()
        else:
            return home()
    else:
        if pathname == "/dashboard":
            from database import get_orders_df
            return dashboard(get_orders_df().to_dict("records"))
        elif pathname == "/ordenes":
            from database import get_orders_df
            return orders_view(get_orders_df().to_dict("records"))
        elif pathname == "/tracking":
            from database import get_orders_df
            return tracking_view_layout(get_orders_df().to_dict("records"))
        elif pathname == "/prediccion":
            return prediction_layout()
        elif pathname == "/logout":
            return dbc.Alert("Sesión cerrada correctamente.", color="success", style={"marginTop": "40px", "textAlign": "center"})
        else:
            return home()

add_login_callback(app)
add_predict_callback(app)

if __name__ == "__main__":
    app.run(debug=True)


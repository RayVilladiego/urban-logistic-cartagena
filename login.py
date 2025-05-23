from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from auth import verify_password
from database import SessionLocal
from models import User

def login_layout():
    return dbc.Card([
        dbc.CardImg(src="/assets/logo.png", top=True, style={"width": "90px", "margin": "0 auto", "marginTop": "10px"}),
        dbc.CardBody([
            html.H2("Iniciar Sesión", className="card-title", style={"marginBottom": "14px", "textAlign": "center"}),
            dbc.Input(id="login-usuario", placeholder="Usuario", type="text", className="mb-2"),
            dbc.Input(id="login-clave", placeholder="Contraseña", type="password", className="mb-2"),
            dbc.Button("Ingresar", id="login-btn", color="primary", block=True, className="mb-2"),
            html.Div(id="login-message")
        ])
    ], style={"maxWidth": "400px", "margin": "60px auto", "boxShadow": "0px 4px 22px #e1e1e1"})

def add_login_callback(app):
    @app.callback(
        Output("login-message", "children"),
        Output("logueado-store", "data"),
        Output("usuario-store", "data"),
        Input("login-btn", "n_clicks"),
        State("login-usuario", "value"),
        State("login-clave", "value"),
        prevent_initial_call=True
    )
    def login_process(n_clicks, usuario, clave):
        if not usuario or not clave:
            return dbc.Alert("Por favor completa todos los campos.", color="warning"), False, ""
        db = SessionLocal()
        user = db.query(User).filter(User.username == usuario).first()
        if user and verify_password(clave, user.hashed_password):
            return dbc.Alert(f"Bienvenido {usuario}", color="success"), True, usuario
        else:
            return dbc.Alert("Usuario o contraseña incorrectos.", color="danger"), False, ""

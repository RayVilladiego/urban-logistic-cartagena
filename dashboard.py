from dash import html

def dashboard(data):
    total = len(data)
    activos = sum(1 for d in data if d["estado"] == "Pendiente")
    en_ruta = sum(1 for d in data if d["estado"] == "En ruta")
    entregados = sum(1 for d in data if d["estado"] == "Entregado")
    return html.Div([
        html.H2("Dashboard de Seguimiento", style={"textAlign": "center"}),
        html.Div([
            html.Div([
                html.H4("Total Pedidos"),
                html.H2(total)
            ], style={"display": "inline-block", "width": "22%", "background": "#e1e7fa", "padding": "15px", "margin": "8px", "borderRadius": "8px", "textAlign": "center"}),
            html.Div([
                html.H4("Pedidos Activos"),
                html.H2(activos)
            ], style={"display": "inline-block", "width": "22%", "background": "#e6ffe1", "padding": "15px", "margin": "8px", "borderRadius": "8px", "textAlign": "center"}),
            html.Div([
                html.H4("Pedidos En Ruta"),
                html.H2(en_ruta)
            ], style={"display": "inline-block", "width": "22%", "background": "#fff6e1", "padding": "15px", "margin": "8px", "borderRadius": "8px", "textAlign": "center"}),
            html.Div([
                html.H4("Pedidos Entregados"),
                html.H2(entregados)
            ], style={"display": "inline-block", "width": "22%", "background": "#e1ffe6", "padding": "15px", "margin": "8px", "borderRadius": "8px", "textAlign": "center"}),
        ], style={"width": "100%", "display": "flex", "justifyContent": "center"}),
    ])

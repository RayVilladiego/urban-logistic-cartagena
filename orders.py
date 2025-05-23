from dash import html

def orders_view(pedidos):
    if not pedidos:
        return html.Div("No hay órdenes registradas.", style={"color": "#999", "textAlign": "center", "marginTop": "35px"})
    return html.Div([
        html.H2("📦 Gestión de Órdenes", style={"textAlign": "center", "marginBottom": "30px", "marginTop": "10px"}),
        html.Div([
            html.Div([
                html.H4(f"ID: {pedido['id']}", style={"marginBottom": "6px"}),
                html.P(f"{pedido['origen']} → {pedido['destino']}", style={"fontWeight": "bold"}),
                html.P(f"Estado: {pedido['estado']}", style={
                    "color": "#dc3545" if pedido['estado'] == "Pendiente" else (
                        "#ffc107" if pedido['estado'] == "En ruta" else "#198754"
                    ),
                    "fontWeight": "bold"
                }),
            ],
            style={
                "background": "white",
                "boxShadow": "0 2px 10px #e0e0e0",
                "borderRadius": "10px",
                "padding": "15px 18px",
                "margin": "10px 0",
                "width": "320px",
                "display": "inline-block",
                "verticalAlign": "top"
            })
            for pedido in pedidos
        ],
        style={"textAlign": "center"}),
    ])

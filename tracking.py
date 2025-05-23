from dash import html, dcc, Input, Output

def tracking_view_layout(pedidos):
    id_options = [{"label": f"Pedido #{p['id']}", "value": p['id']} for p in pedidos] if pedidos else []
    return html.Div([
        html.H2("📍 Tracking de Pedidos", style={"textAlign": "center", "marginBottom": "30px", "marginTop": "10px"}),
        html.Div([
            dcc.Dropdown(
                id="tracking-pedido-id",
                options=id_options,
                placeholder="Selecciona un ID de pedido",
                style={"width": "320px", "margin": "0 auto"}
            ),
            html.Div(id="tracking-pedido-info", style={"marginTop": "24px"})
        ], style={"textAlign": "center"})
    ])

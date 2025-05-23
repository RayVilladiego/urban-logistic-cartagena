from dash import html, dcc

def home():
    return html.Div([
        html.Div([
            html.Img(src="/assets/logo.png", style={"height": "90px", "marginBottom": "12px"}),
        ], style={"textAlign": "center", "marginTop": "30px"}),
        html.H1("🚚 Bienvenido al Sistema de Logística Urbana", style={
            "textAlign": "center", "marginTop": "20px", "color": "#12427d"
        }),
        html.H3("¡Gestiona, monitorea y optimiza tus entregas en un solo lugar!", style={
            "textAlign": "center", "color": "#375a9e"
        }),
        html.P(
            "Usa el menú o los accesos directos para navegar entre las secciones clave. "
            "Mejora tu control operativo y toma decisiones inteligentes con el dashboard interactivo.",
            style={"fontSize": "1.1em", "margin": "30px 22% 18px 22%", "textAlign": "center"}
        ),
        html.Div([
            dcc.Link(html.Button("Ir al Dashboard", style={"margin": "10px"}), href="/dashboard"),
            dcc.Link(html.Button("Ver Órdenes", style={"margin": "10px"}), href="/ordenes"),
            dcc.Link(html.Button("Tracking", style={"margin": "10px"}), href="/tracking"),
            dcc.Link(html.Button("Predicción ML", style={"margin": "10px"}), href="/prediccion"),
        ], style={"textAlign": "center", "marginBottom": "18px"}),
        html.Div([
            html.Ul([
                html.Li("🔎 Seguimiento en tiempo real de pedidos y entregas"),
                html.Li("📊 KPIs y métricas clave para la toma de decisiones"),
                html.Li("👤 Gestión integral de usuarios"),
                html.Li("🛒 Registro fácil y rápido de nuevos pedidos"),
            ], style={"listStyle": "none", "padding": 0, "fontSize": "1.1em"})
        ], style={"textAlign": "center"}),
        html.Div(
            "¿Listo para transformar tu operación logística?",
            style={"marginTop": "30px", "fontWeight": "bold", "textAlign": "center", "color": "#188f48"}
        ),
    ])

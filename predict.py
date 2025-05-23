import numpy as np
import pandas as pd
import joblib
import tensorflow as tf
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Archivos en la raíz del proyecto
modelo = tf.keras.models.load_model("modelo_entrega.h5")
scaler = joblib.load("scaler_entrega.pkl")
encoder = joblib.load("encoder_entrega.pkl")

columnas_modelo = ["origen", "destino", "distancia", "hora_salida"]  # AJUSTA según tu pipeline real

def prediction_layout():
    return dbc.Card([
        dbc.CardBody([
            html.H3("Predicción de Tiempo de Entrega", style={"textAlign": "center"}),
            dbc.Input(id="origen-pred", placeholder="Origen", type="text", className="mb-2"),
            dbc.Input(id="destino-pred", placeholder="Destino", type="text", className="mb-2"),
            dbc.Input(id="distancia-pred", placeholder="Distancia (km)", type="number", className="mb-2"),
            dbc.Input(id="hora-pred", placeholder="Hora de salida (HH:MM)", type="text", className="mb-2"),
            dbc.Button("Predecir", id="btn-predecir", color="primary", block=True, className="mb-2"),
            html.Div(id="resultado-pred")
        ])
    ], style={"maxWidth": "480px", "margin": "60px auto", "boxShadow": "0px 4px 22px #e1e1e1"})

def add_predict_callback(app):
    @app.callback(
        Output("resultado-pred", "children"),
        Input("btn-predecir", "n_clicks"),
        State("origen-pred", "value"),
        State("destino-pred", "value"),
        State("distancia-pred", "value"),
        State("hora-pred", "value"),
        prevent_initial_call=True
    )
    def hacer_prediccion(n, origen, destino, distancia, hora):
        if not all([origen, destino, distancia, hora]):
            return dbc.Alert("Por favor completa todos los campos.", color="warning")

        df = pd.DataFrame([{
            "origen": origen,
            "destino": destino,
            "distancia": float(distancia),
            "hora_salida": hora
        }])

        try:
            df[["origen", "destino"]] = encoder.transform(df[["origen", "destino"]])
        except Exception as e:
            return dbc.Alert(f"Error en encoding: {e}", color="danger")
        
        try:
            df = df.reindex(columns=columnas_modelo, fill_value=0)
            X = scaler.transform(df)
        except Exception as e:
            return dbc.Alert(f"Error en preprocesamiento: {e}", color="danger")
        
        try:
            pred = modelo.predict(X)
            tiempo = int(pred[0, 0])
            return dbc.Alert(f"⏰ El tiempo estimado de entrega es: {tiempo} minutos.", color="success")
        except Exception as e:
            return dbc.Alert(f"Error en la predicción: {e}", color="danger")

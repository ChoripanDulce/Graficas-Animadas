""" from fastapi import FastAPI
import pandas as pd
from matplotlib.animation import FuncAnimation

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola Mundo, servicio activo"}

@app.get("/saludo{pais}")
paramPais = pais
def saludo(pais: str):
    return {"message": f"Grafico generado para el{pais}"}


df = pd.read_csv("01 renewable-share-energy.csv")
df_africa = df[df["Entity"] == "paramPais"].copy()
years = df_africa["Year"].values """
import os
from fastapi import FastAPI

app = FastAPI()

from load_model import load_model
from input import make_df

model_name = "weights.sav"
model = load_model(model_name)

@app.get("/predict")
def predict(input_data:str):
    return f"<p>{model_name=}</p><p>{input_data=}</p><p>prediction={model.predict(make_df(input_data))}</p>"

@app.get("/status")
def status():
    return f"<p>FastAPI is OK</p><p>{model_name=}</p>"

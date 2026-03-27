from functools import lru_cache

from fastapi import FastAPI
from fastapi import HTTPException
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

maxsize=1
def get_classifier():
    return pipeline("sentiment-analysis")

@app.get("/")
def root():
    return {"message": "FastAPI service started!"}

@app.get("/predict/{text}")
def get_params(text: str):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    return get_classifier()(text)

"/predict/"
def predict(item: Item):
    if not item.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    return get_classifier()(item.text)

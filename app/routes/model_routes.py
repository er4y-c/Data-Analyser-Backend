from fastapi import APIRouter
import pandas as pd
from core.models.classification import XGBoostClassifier
from fastapi.encoders import jsonable_encoder
from app.crud.models import get_data_from_source
from app.crud.example import get_columns

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/train/{datasource}")
async def train(datasource: str):
    data = get_data_from_source(datasource)
    columns = get_columns(datasource)
    df = pd.DataFrame(data, columns=columns)
    classifier = XGBoostClassifier(df)
    classifier.preprocess_data()
    classifier.train_model()
    classifier.json_xgb_model('xgboost_model.json')
    return {"message": "Hello World"}

@router.post("/predict")
async def predict():
    return {"message": "Hello World"}
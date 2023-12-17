from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes.analysis_routes import router as analysis_routes
from app.routes.data_connector_routes import router as data_connector_routes
from app.routes.model_routes import router as model_routes
from app.routes.auth_routes import router as auth_routes
from app.db.mongodb import init_mongo
from pymongo import MongoClient
from dynaconf import settings
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_mongo()

app.include_router(router=auth_routes, tags=["auth"], prefix="/auth")
app.include_router(router=analysis_routes, tags=["analysis"], prefix="/analysis")
app.include_router(router=data_connector_routes, tags=["data-connector"], prefix="/data-connector")
app.include_router(router=model_routes, tags=["model"], prefix="/model")
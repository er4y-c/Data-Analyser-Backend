from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analysis_routes import router as analysis_routes
from app.routes.data_connector_routes import router as data_connector_routes
from app.routes.model_routes import router as model_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=analysis_routes, tags=["analysis"], prefix="/analysis")
app.include_router(router=data_connector_routes, tags=["data-connector"], prefix="/data-connector")
app.include_router(router=model_routes, tags=["model"], prefix="/model")
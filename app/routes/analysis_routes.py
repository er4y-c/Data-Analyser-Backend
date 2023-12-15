from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud.example import get_all_data, get_tables, get_columns, get_column_data

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/get_all_data")
async def get_data():
    try:
        data = get_all_data()
        return JSONResponse(
            status_code=200,
            content={
                "results": jsonable_encoder(data)
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"An error occurred. Error details: {str(e)}"
            }
        )

@router.get("/get_data_sources")
async def get_data_sources():
    try:
        tables = get_tables()
        return JSONResponse(
            status_code=200,
            content={
                "data_sources": tables
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"An error occurred. Error details: {str(e)}"
            }
        )
@router.get("/get_data_sources/{table_name}")
async def get_data_sources(table_name):
    try:
        columns = get_columns(table_name)
        return JSONResponse(
            status_code=200,
            content={
                "table_columns": columns
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"An error occurred. Error details: {str(e)}"
            }
        )

@router.post("/get_charts_data/{table_name}")
async def get_charts_data(table_name:str, column_names:list[str]):
    try:
        data = get_column_data(table_name, column_names)
        return JSONResponse(
            status_code=200,
            content={
                "columns": column_names,
                "results": jsonable_encoder(data)
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"An error occurred. Error details: {str(e)}"
            }
        )
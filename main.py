from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud.example import get_all_data

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_data")
async def get_data():
    try:
        data = await get_all_data()
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
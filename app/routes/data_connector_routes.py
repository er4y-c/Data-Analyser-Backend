from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import pandas as pd
from app.crud.example import create_table, insert_into_table, clean_column_names

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        table_name = file.filename.split('.')[0].lower()
        table_name = table_name.replace(' ', '_').replace('-', '_').replace('.', '_').replace(',', '_')
        contents = await file.read()
        decoded = contents.decode('utf-8').splitlines()

        columns = decoded[0].split(',')
        columns = clean_column_names(columns)
        create_table(table_name, [f"{col} VARCHAR(255)" for col in columns])

        data = [row.split(',') for row in decoded[1:]]

        insert_into_table(table_name, columns, data)

        return JSONResponse(
            status_code=200,
            content={
                "message": "File uploaded and data inserted into the database."
            }
        )

    elif file.filename.endswith('.xlsx'):
        table_name = file.filename.split('.')[0].lower()
        table_name = table_name.replace(' ', '_').replace('-', '_').replace('.', '_').replace(',', '_')
        contents = await file.read()
        df = pd.read_excel(contents)
        columns = df.columns.tolist()
        create_table(table_name, [f"{col.lower().replace(' ', '_')} VARCHAR(255)" for col in columns])
        data = df.values.tolist()

        insert_into_table(table_name, columns, data)

        return JSONResponse(
            status_code=200,
            content={
                "message": "File uploaded and data inserted into the database."
            }
        )
    else:
        return JSONResponse(
            status_code=400,
            content={
                "message": "File type not supported. Please upload a CSV or Excel file."
            }
        )
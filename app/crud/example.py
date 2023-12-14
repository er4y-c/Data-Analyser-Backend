from fastapi import FastAPI, UploadFile, File
import psycopg2
import csv
from dynaconf import settings
from app.db.postgre import engine, Session
from app.models.ExampleModel import HastaneVerileri

session = Session(bind=engine)

def get_all_data():
    return session.query(HastaneVerileri).all()

def create_table(table_name, columns):
    conn = psycopg2.connect(
        database=settings.POSTGRE_DB_NAME,
        user=settings.POSTGRE_DB_USER,
        password=settings.POSTGRE_DB_PASSWORD,
        host=settings.POSTGRE_DB_HOST,
        port=settings.POSTGRE_DB_PORT
    )
    cur = conn.cursor()
    # Tablo oluştur
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
    cur.execute(query)
    conn.commit()
    conn.close()

def insert_into_table(table_name, columns, data):
    conn = psycopg2.connect(
        database=settings.POSTGRE_DB_NAME,
        user=settings.POSTGRE_DB_USER,
        password=settings.POSTGRE_DB_PASSWORD,
        host=settings.POSTGRE_DB_HOST,
        port=settings.POSTGRE_DB_PORT
    )
    cur = conn.cursor()
    # Verileri tabloya ekle
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
    cur.executemany(query, data)
    conn.commit()
    conn.close()
    
def clean_column_names(columns):
    return [col.replace(' ', '_') for col in columns]
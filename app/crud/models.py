import psycopg2
from dynaconf import settings
from app.db.postgre import engine, Session

session = Session(bind=engine)

def get_data_from_source(table_name):
    conn = psycopg2.connect(
        database=settings.POSTGRE_DB_NAME,
        user=settings.POSTGRE_DB_USER,
        password=settings.POSTGRE_DB_PASSWORD,
        host=settings.POSTGRE_DB_HOST,
        port=settings.POSTGRE_DB_PORT
    )
    query = f"SELECT * FROM {table_name}"
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    conn.close()

    return data
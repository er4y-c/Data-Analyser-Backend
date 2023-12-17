import psycopg2
from dynaconf import settings
from app.db.postgre import engine, Session

session = Session(bind=engine)

def get_all_data(table_name, columns):
    conn = psycopg2.connect(
        database=settings.POSTGRE_DB_NAME,
        user=settings.POSTGRE_DB_USER,
        password=settings.POSTGRE_DB_PASSWORD,
        host=settings.POSTGRE_DB_HOST,
        port=settings.POSTGRE_DB_PORT
    )
    query = f"SELECT * FROM {table_name}"
    if columns is not None:
        query = f"SELECT {', '.join(columns)} FROM {table_name}"

    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    conn.close()

    return data

def get_column_data(table_name, column_names):
    conn = psycopg2.connect(
        database=settings.POSTGRE_DB_NAME,
        user=settings.POSTGRE_DB_USER,
        password=settings.POSTGRE_DB_PASSWORD,
        host=settings.POSTGRE_DB_HOST,
        port=settings.POSTGRE_DB_PORT
    )
    cur = conn.cursor()
    query = "SELECT "
    for column in column_names:
        query = query + f"COUNT(DISTINCT {column}) as {column}_count, "
    query = query[:-2]
    query = query+f" FROM {table_name}"
    print(query)
    cur.execute(query)
    data = cur.fetchall()
    conn.close()
    return data

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

def get_tables():
    conn = psycopg2.connect(
        database=settings.POSTGRE_DB_NAME,
        user=settings.POSTGRE_DB_USER,
        password=settings.POSTGRE_DB_PASSWORD,
        host=settings.POSTGRE_DB_HOST,
        port=settings.POSTGRE_DB_PORT
    )
    cur = conn.cursor()

    query = f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    cur.execute(query)
    tables = cur.fetchall()
    conn.close()
    return tables

def get_columns(table_name):
    conn = psycopg2.connect(
        database=settings.POSTGRE_DB_NAME,
        user=settings.POSTGRE_DB_USER,
        password=settings.POSTGRE_DB_PASSWORD,
        host=settings.POSTGRE_DB_HOST,
        port=settings.POSTGRE_DB_PORT
    )
    cur = conn.cursor()

    query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'"
    cur.execute(query)
    columns = cur.fetchall()
    conn.close()
    return columns
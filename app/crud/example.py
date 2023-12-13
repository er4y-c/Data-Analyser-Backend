from app.db.postgre import engine, Session
from app.models.ExampleModel import HastaneVerileri

session = Session(bind=engine)

async def get_all_data():
    return session.query(HastaneVerileri).all()
from pymongo import MongoClient
from dynaconf import settings
from typing import Optional

client: Optional[MongoClient] = None

def init_mongo():
    global client
    client = MongoClient(settings.MONGODB_HOST)
    return client


def get_database():
    if client is None:
        raise ValueError("init_mongo must be called")
    return client
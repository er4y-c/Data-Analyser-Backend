from fastapi import Depends
from passlib.context import CryptContext
from dynaconf import settings

import jwt
from app.schemas.auth_schemas import Users
from app.db.mongodb import get_database

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(email: str):
    db = get_database()
    users = db[settings.MONGODB_DB_NAME]["Users"]
    user_data = users.find_one({"email": email})
    if user_data:
        return dict(user_data)
    return None

def create_user(user: Users):
    db = get_database()
    users = db[settings.MONGODB_DB_NAME]["Users"]
    user_dict = dict(user)
    # hashed_password = pwd_context.hash(user.password)
    # user_dict.update({"hashed_password": hashed_password})
    # del user_dict['password']
    results = users.insert_one(user_dict)
    return results.inserted_id

def verify_password(plain_password, hashed_password):
    return #pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

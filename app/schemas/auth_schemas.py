from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    username: str
    password: str
    email: str
    full_name: str
    disabled: Optional[bool] = None

    class Config:
        model_config = {
        "json_schema_extra": {
            "examples": [{
                "username": "test",
                "password": "test",
                "email": "test",
                "full_name": "test",
                "disabled": False
                }
            ]
        }
    }

class UserLogin(BaseModel):
    username: str
    password: str
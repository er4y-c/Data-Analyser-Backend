from pydantic import BaseModel
from typing import Optional, List

class Users(BaseModel):
    email: str
    password: str
    full_name: str
    department: str
    projects: Optional[List[str]] = None
    disabled: Optional[bool] = None

    class Config:
        model_config = {
        "json_schema_extra": {
            "examples": [{
                "email": "test@example.com",
                "password": "test",
                "full_name": "test",
                "department": "İş Geliştirme",
                "projects": ["sagligim_cepte", "test2"],
                "disabled": False
                }
            ]
        }
    }

class UserLogin(BaseModel):
    email: str
    password: str
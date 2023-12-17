from fastapi import APIRouter, Depends
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.schemas.auth_schemas import Users, UserLogin
from app.controllers.auth_controller import get_user, create_user, verify_password, create_access_token
from app.db.mongodb import get_database
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/create_user")
async def create_user_endpoint(user: Users):
        existing_user = get_user(user.email)
        if existing_user:
            print(existing_user)
            return JSONResponse(status_code=400, content={"message": "User already exists"})
        idx = create_user(user)

        return JSONResponse(status_code=200, content={"message": f"User {idx} created successfully"})

@router.post("/login")
async def login_for_access_token(user: UserLogin):
    db_user = get_user(user.email)
    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    print(db_user)
    access_token = create_access_token(data={"sub": db_user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(email: str):
    current_user = get_user(email)
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return JSONResponse(status_code=200, content=jsonable_encoder(current_user))

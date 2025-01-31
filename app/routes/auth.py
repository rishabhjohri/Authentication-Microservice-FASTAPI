from fastapi import APIRouter, HTTPException
from app.database import users_collection
from app.models import User, LoginUser, Token
from app.utils import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
async def register(user: User):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hash_password(user.password)
    new_user = {"username": user.username, "email": user.email, "hashed_password": hashed_pw}
    
    await users_collection.insert_one(new_user)
    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
async def login(user: LoginUser):  # Use the new LoginUser model
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


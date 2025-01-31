from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):  # Separate model for login
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

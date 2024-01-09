from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    
class UserCreate(UserBase):
    lname: str
    fname: str
    password: str
    
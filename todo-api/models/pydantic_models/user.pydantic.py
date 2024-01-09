from pydantic import BaseModel, EmailStr, StrictStr

class UserBase:
    email: EmailStr
    
class UserCreate(UserBase):
    lname: str
    fname: str
    password: str
    
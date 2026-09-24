from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict,EmailStr

class PostBase(BaseModel):
    title:str
    content:str
    published:bool =True
    # rating: Optional[float]=None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    # title:str
    # content:str
    # published:bool
    model_config = ConfigDict(from_attributes=True)
        

class UserCreate(BaseModel):
    # id:int
    email:EmailStr
    password:str

class UserSend(BaseModel):
    id:int
    email:EmailStr
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]=None
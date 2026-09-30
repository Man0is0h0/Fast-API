from datetime import datetime
from typing import Optional
from typing import Annotated
from pydantic import BaseModel, ConfigDict,EmailStr, Field

class PostBase(BaseModel):
    title:str
    content:str
    published:bool =True
    # rating: Optional[float]=None

class PostCreate(PostBase):
    pass
        
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
    id: Optional[int]=None

class Post(PostBase):
    id:int
    created_at: datetime
    user_id: int
    owner:UserSend
    model_config = ConfigDict(from_attributes=True)
class PostOut(BaseModel):
    Post: Post
    Votes:int
    model_config = ConfigDict(from_attributes=True)

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]
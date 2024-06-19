from typing import Optional
from pydantic import BaseModel,EmailStr

from datetime import datetime

from pydantic.types import conint
class PostBase(BaseModel):
    title: str
    content: str 
    published:bool =True 
class PostCreate(PostBase):
    pass 

class UserCreate(BaseModel):
    email:EmailStr
    password:str
class UserOut(BaseModel):
    id:int
    email:EmailStr 
    created_at:datetime   

class UserLogin(BaseModel):
    email:EmailStr 
    password:str
    
    
class Post(PostBase):
    id:int
    created_at:datetime 
    owner_id:int
    owner:UserOut

class PostOUT(BaseModel):
    Post: Post
    votes:int

class Token(BaseModel):
    access_token:str 
    token_type:str 

class TokenData(BaseModel):
    id:Optional[int] =None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) 
    
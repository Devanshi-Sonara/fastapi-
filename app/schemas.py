from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Base class for shared attributes
class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True

# Class for creating a new post
class PostCreate(PostBase):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    # Pydantic v2 configuration
    # model_config = {
    #     "from_attributes": True
    # }
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostRes(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool] = True
    created_at: datetime
    owner_id: int
    owner: UserOut

    # Pydantic v2 configuration
    model_config = {
        "from_attributes": True
    }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str

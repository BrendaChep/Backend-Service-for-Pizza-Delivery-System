from pydantic import BaseModel
from typing import Optional
from fastapi_jwt_auth import AuthJWT

class SignUpModel(BaseModel):
    id:Optional[str]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
            'username':'johndoe',
            'email':'johndoe@gmail.com',
            'password':'password',
            'is_staff':False,
            'is_active':True

            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str='dac6225e7545f69ca1cedebfe7cec4cadceb58f3fe32197a724b957bdfe0d123'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 

class LoginModel(BaseModel):
    username:str
    password:str
    class Config:
        orm_mode=True
        schema_extra={
            'example':{
            'username':'johndoe',
            'password':'password'

            }
        }

class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]='PENDING'
    pizza_size:Optional[str]='SMALL'
    user_id :Optional[int]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
            'pizza_size':'LARGE',
            'quantity':2
            

            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str]='PENDING'

    class Config:
        orm_mode = True
        schema_extra={
            'example':{
            'order_status':'PENDING'
            }
        }

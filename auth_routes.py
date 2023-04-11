from fastapi import APIRouter,status,Depends, Request, Body, Form
from database import Session, engine
from schemas import SignUpModel,LoginModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

auth_router = APIRouter(
    prefix = '/auth',
    tags=['auth']
)

session = Session(bind=engine)

@auth_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):

    """
    Sample hello world route for a logged in user.    
    """

    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
    return {'message':'hello world'}

@auth_router.post('/signup',status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpnModel,Authorize:AuthJWT=Depends()):

    """
    Creates a user. This requires the following
    ```
    username:integer
    email:string
    password:string
    ```    
    """

    db_email = session.query(User).filter(User.email==email).first()

    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with the email already exists')    

    db_username = session.query(User).filter(User.username==username).first()

    if db_username is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with the username already exists')
    
    new_user = User(
        username = username,
        email = email,
        password = generate_password_hash(password)
    )

    session.add(new_user)
    session.commit()
    print(new_user)

    return new_user

#login route
@auth_router.post('/login', status_code=status.HTTP_200_OK)
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):

    """
    Login a user. This requires the following
    ```
    username:integer
    password:string
    ```  
    and returns a token pair of 'access' and 'refresh'  
    """
       
    db_user=session.query(User).filter(User.username==user.username).first()
    if db_user and check_password_hash(db_user.password, user.password):
        access_token=Authorize.create_access_token(subject=db_user.username)
        refresh_token=Authorize.create_refresh_token(subject=db_user.username)

        response={
            'access':access_token,
            'refresh':refresh_token
        }
        return jsonable_encoder(response)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Username or Password')

#refreshing tokens
@auth_router.get('/refresh')
async def refresh_token(Authorize:AuthJWT=Depends()):

    """
    Creates a fresh access token. This creates a fresh access token and it requires a refresh token.     
    """
    try:
        Authorize.jwt_refresh_token_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Please provide a valid refresh token')
    
    current_user = Authorize.get_jwt_subject()
    
    access_token = Authorize.create_access_token(current_user)

    return jsonable_encoder({'access': access_token})




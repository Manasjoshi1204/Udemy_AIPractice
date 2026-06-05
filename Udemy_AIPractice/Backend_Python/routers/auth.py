from fastapi import APIRouter,Depends,HTTPException
from pydantic import BaseModel
from models import Users 
from passlib.context import CryptContext
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError
import secrets
from datetime import timedelta,timezone,datetime


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = "mysecretkey123456" #secrets.token_hex(32)
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class Token(BaseModel):
    access_token : str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class User_check(BaseModel):
    email: str
    username: str
    name:str
    surname:str
    password:str
    role:str
    phone_number:str

db_dependency = Annotated[Session,Depends(get_db)]

#Check username and password
def check_user_pass(username:str,password:str,db: Session):
    user = db.query(Users).filter(username == Users.username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

#Creating payload for JWT
def create_access_Token(username:str,user_id:int,role:str,expires_delta:timedelta):
    encode = {'sub':username,'id':user_id,'role':role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

#Validate token    
async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username : str = payload.get('sub')
        user_id : str = payload.get('id')
        user_role : str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user')
        return {'username':username, 'id':user_id,'user_role':user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user')

@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,user : User_check):
    user_model = Users(
        email = user.email,
        username = user.username,
        name = user.name,
        surname = user.surname,
        role = user.role,
        hashed_password = bcrypt_context.hash(user.password),
        is_active = True,
        phone_number = user.phone_number
    )   
    db.add(user_model)
    db.commit()
    
#Sending the token to user    
@router.post('/token',response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
    user = check_user_pass(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_Token(user.username,user.id,user.role,timedelta(minutes=2))
    return {'access_token' : token, 'token_type': 'bearer'}




    




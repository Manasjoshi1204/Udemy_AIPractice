from fastapi import APIRouter,Depends,HTTPException,Path
from models import Users
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from .auth import get_current_user
from passlib.context import CryptContext
from pydantic import BaseModel,Field

router = APIRouter(
    prefix='/users',
    tags=['users']
)

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
        
class UpdatePass(BaseModel):
    old_pass:str
    new_pass:str = Field(min_length=5)
        
db_dependancy = Annotated[Session,Depends(get_db)]
user_dependancy = Annotated[dict,Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')


@router.get("/user",status_code=status.HTTP_200_OK)
async def show_all(db:db_dependancy,user:user_dependancy):
    return db.query(Users).filter(Users.id == user.get('id')).all()


@router.put("/chpassword",status_code=status.HTTP_204_NO_CONTENT)
async def change_pass(new_pass: UpdatePass,db:db_dependancy,user:user_dependancy):
    
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if user_model is None:
        raise HTTPException(status_code=404,detail="Id not fine")
    
    if not bcrypt_context.verify(new_pass.old_pass,user_model.hashed_password):
        raise HTTPException(status_code=401,detail="Pass not fine")
    
    user_model.hashed_password = bcrypt_context.hash(new_pass.new_pass)
    db.commit()
    
@router.put("/update_phn",status_code=status.HTTP_204_NO_CONTENT)
async def change_phn(user:user_dependancy,db:db_dependancy,new_phn:str):
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if user_model is None:
        raise HTTPException(status_code=404,detail="Id not fine")
    user_model.phone_number = new_phn
    db.commit()
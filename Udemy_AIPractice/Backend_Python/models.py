#Models.py -> to define tables
from database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True)
    username = Column(String,unique=True)
    name = Column(String)
    surname = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)
    role = Column(String)
    phone_number = Column(String)
    

class Todos(Base):
    __tablename__ = 'todos' #Defining table name in DB
    id = Column(Integer,primary_key=True,index=True) #unique by index
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean,default=False)
    owner_id = Column(Integer,ForeignKey("users.id"))
    
    
    
                
    
    
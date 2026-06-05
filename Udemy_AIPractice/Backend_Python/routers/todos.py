from fastapi import APIRouter,Depends,HTTPException,Path
from models import Todos
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel,Field
from .auth import get_current_user

router = APIRouter(
     prefix="/todos",
    tags=["todos"]
)    

def get_db():
    db = SessionLocal()
    try:
        yield db #return + finally = close before route uses db (coz return ends)
                 #yield + finally  = close after route uses db (coz yeild pauses)
    finally:
        db.close()
        
db_dependency = Annotated[Session,Depends(get_db)]
user_dependancy = Annotated[dict,Depends(get_current_user)]

class TodoCheck(BaseModel):
    title:str = Field(...,min_length=3)
    description:str = Field(...,min_length=3,max_length=100)
    priority:int = Field(...,gt=0,le=6)
    complete:bool

#Get all        
@router.get("/",status_code=status.HTTP_200_OK)
async def real_all(user:user_dependancy,db : db_dependency):
    #Depends-> Dependency injection (To do smthing before final execute)
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()

#Get with path parameter
@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(user:user_dependancy,db:db_dependency,todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first() #cause ids are unique it wont check for others improving performance
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Id not found')


#Add new Todo
@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(user:user_dependancy,input_todo:TodoCheck,db:db_dependency):
    todo_model = Todos(**input_todo.model_dump(),owner_id = user.get('id'))
    db.add(todo_model)
    db.commit()
    

#Update old todo
@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user:user_dependancy,db:db_dependency,todo_updated:TodoCheck,todo_id : int = Path(gt=0)):
    
    todos_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first()
    if todos_model is None:
        raise HTTPException(status_code=404,detail="Id not fine")
    
    todos_model.title = todo_updated.title
    todos_model.description = todo_updated.description
    todos_model.priority = todo_updated.priority
    todos_model.complete = todo_updated.complete    
    
    #for key, value in todo_updated.model_dump().items():
        #setattr(todos_model, key, value) if we want to copy all attributes
    db.commit()
    
    
@router.delete('/todo/{todo_id}')
async def delete_todo(user:user_dependancy,db:db_dependency,todo_id : int = Path(gt=0)):
    todos_model = db.query(Todos).filter(todo_id == Todos.id).filter(Todos.owner_id == user.get('id')).first()
    if todos_model is None:
        raise HTTPException(status_code=404,detail="Id not fine")
    db.delete(todos_model)
    db.commit()
    
    

    
    
    
    

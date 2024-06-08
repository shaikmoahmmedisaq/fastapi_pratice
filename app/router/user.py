from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from app import models,schemas,utills
# from .. import schemas 
# from .. import utills
from .. database import get_db
from typing import List 
router = APIRouter(
    prefix="/users",tags=['users']
)
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut) 
def createuser(user:schemas.UserCreate,db :Session = Depends(get_db)):
    hashed_password = utills.hash(user.password)
    user.password= hashed_password
    print(user.password)
    new_user = models.User(**user.dict()) 
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.UserOut)
def get_user(id:int,db :Session = Depends(get_db)):
    Get_user=db.query(models.User).filter(models.User.id == id).first()
    if not Get_user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with {id} is not exists")
    return Get_user
from .. import schemas,models,utils
from ..database import get_db
from fastapi import HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/",status_code=201,response_model=schemas.UserSend)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    try:
        user.password=utils.hash_password(user.password)
        new_user=models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as error:
        db.rollback()
        print("Error:", error)
        raise HTTPException(
            status_code=409,
            detail="Could not create user"
        )

@router.get('/{id}',status_code=200,response_model=schemas.UserSend)
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail=f"User with id: {id} does not exist")
    return user
    # return new_user
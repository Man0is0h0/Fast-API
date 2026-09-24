from turtle import mode

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, schemas, models,utils,oauth2


router = APIRouter(tags=['Authentication'])


@router.post("/login",status_code=200)
def login(user_cred: OAuth2PasswordRequestForm=Depends(),db: Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==user_cred.username).first()
    if not user:
        raise HTTPException(status_code=403,detail="Invalid Credentials")
    if not utils.verify(user_cred. password,user.password):
        raise HTTPException(status_code=403,detail="Invalid Credentials")
    access_token=oauth2.create_access_token(data={"user_id":user.id})

    return {"access_token":access_token,"token_type":"bearer"}
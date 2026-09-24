from time import timezone

from fastapi import Depends,status,HTTPException
from jose import JWTError,jwt
from datetime import datetime,timedelta

from pydantic import Secret

from app import schemas 
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY="yDdRA52r3L1ko5Hk5M6mNDWVM8MQzyEwpaSGrEVzLDA"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_id=payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data=schemas.TokenData(id=user_id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token:str=Depends(oauth2_scheme)):
    createtials_exception=HTTPException(status_code=401,detail=f"Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,createtials_exception)
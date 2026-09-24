# from multiprocessing import connection
# from os import stat_result
# from sqlite3 import Cursor, connect


# from passlib.context import CryptContext
from fastapi import FastAPI
# from fastapi.params import Body
# from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from app.routers import auth
from . import models 
from .database import engine
from .routers import post,user
models.Base.metadata.create_all(bind=engine)
app=FastAPI()




    

while True:
    try: 
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Manish2004',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database Connection was successfull")
        break
    except Exception as error:
        print("Connection failed")
        print("Error: ",error)
        time.sleep(2)


#get post by id
# def find_post(id):
#     for p in my_posts:
#         if p['id']==id:
#             return p

# #get post index
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id']==id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"Message: " : "Welcome to my api!!!"}  
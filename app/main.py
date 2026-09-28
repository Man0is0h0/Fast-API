# from multiprocessing import connection
# from os import stat_result
# from sqlite3 import Cursor, connect
# from passlib.context import CryptContext
# from fastapi.params import Body
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

from fastapi import FastAPI
from app.routers import auth
from . import models
from .database import engine
from .routers import post,user
models.Base.metadata.create_all(bind=engine)
app=FastAPI()

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
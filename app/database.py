from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# while True:
#     try: 
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Manish2004',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database Connection was successfull")
#         break
#     except Exception as error:
#         print("Connection failed")
#         print("Error: ",error)
#         time.sleep(2)




SQLALCHEMY_DATABASE_URL='postgresql://postgres:Manish2004@localhost/fastapi'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) 
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
        # print("Database Connection was successfull")
    finally:
        db.close()
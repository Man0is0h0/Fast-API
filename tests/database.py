from fastapi.testclient import TestClient
from httpx2 import head
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.database import get_db,Base
from app.config import settings
import pytest
# from alembic import command


SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.database_username,
    password=settings.database_password,
    host=settings.database_hostname,
    port=settings.database_port,
    database=settings.database_name+'_test',
    query={"sslmode": settings.database_sslmode},
)
engine=create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) 

# Base=declarative_base()
    
# client=TestClient(app)
@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db=TestingSessionLocal()
    try:
        yield db
            # print("Database Connection was successfull")
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
                    # print("Database Connection was successfull")
        finally:
            session.close()
    # command.upgrade(head)
    app.dependency_overrides[get_db]=override_get_db
    yield TestClient(app)
 
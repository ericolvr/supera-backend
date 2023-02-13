import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from src.infra.configs.database import get_database
from src.main import app

load_dotenv()

db = {
    'user': os.getenv('TEST_DB_USER'),
    'pwd': os.getenv('TEST_DB_PWD'),
    'host': os.getenv('TEST_DB_HOST'),
    'port': os.getenv('TEST_DB_PORT'),
    'name': os.getenv('TEST_DB_NAME'),
}

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:tests@localhost:3307/tests_supera"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={}, 
    future=True
)

TestingSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    future=True
)

Base = declarative_base()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_database():
    """ get database connection """
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()


app.dependency_overrides[get_database] = override_get_database

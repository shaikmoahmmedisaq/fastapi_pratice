from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Settings

SQLALCHEMY_DATABASE_URL =f'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:{Settings.database_port}/{Settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# import psycopg2
# from psycopg2.extras import RealDictCursor 
# import time

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='root',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection is sucessfully!")
#         break
#     except Exception as error:
#         print("Connection to database  failed ") 
#         print("Error:",error)
#         time.sleep(2)
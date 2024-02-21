from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Qwerty123@localhost:3306/todoapp'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DB:
    def __init__(self):
        try:
            engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=40)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Can't connect to server")

db = DB()
from sqlalchemy import create_engine,Column, Integer, String,Date
from sqlalchemy.orm import declarative_base
from datetime import datetime as d


db_url="sqlite:////storage/emulated/0/@FLASK/taskManager2.db"

engine = create_engine(db_url)

Base= declarative_base()

class Users(Base):
    __tablename__="taskManager2"
    id=Column(Integer, primary_key=True)
    tasks=Column(String)
    date=Column(Date)
Base.metadata.create_all(engine)

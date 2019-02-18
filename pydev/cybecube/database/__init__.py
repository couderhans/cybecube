from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///C:\\Users\\couder\\Projects\\pydev\\test.db')

Base = declarative_base()

db_session = sessionmaker()
db_session.configure(bind=engine)
session = db_session()
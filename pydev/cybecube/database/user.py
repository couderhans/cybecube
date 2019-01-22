from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


def create_table_user():
    Base.metadata.create_all(engine)


def get_user(name):
    user = session.query(User).filter(User.name == name).first()
    return user


def insert_into_user(user):
    session.add(user)
    session.commit()


def delete_user():
    Base.metadata.drop_all(engine)


from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session
from cybecube.database.user import User

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref


class Repository(Base):
    __tablename__ = 'repository'
    repo_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    clone_url = Column(String(250), nullable=False)
    user_name = Column(String(250), ForeignKey(User.name))
    user = relationship(User, foreign_keys='Repository.user_name')


def create_table_repository():
    Base.metadata.create_all(engine)


def get_repository(name):
    repository = session.query(Repository).filter(Repository.name == name).first()
    return repository


def insert_into_repository(repository):
    session.add(repository)
    session.commit()


def delete_repository():
    Base.metadata.drop_all(engine)

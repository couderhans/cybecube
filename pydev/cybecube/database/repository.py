from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session

from sqlalchemy import Column, Integer, String


class Repository(Base):
    __tablename__ = 'repository'
    repo_id = Column(Integer, primary_key=True)
    user = Column(String(250))
    name = Column(String(250))
    clone_url = Column(String(250), nullable=False)


def create_table_repositories():
    Base.metadata.create_all(engine)


def get_repository(name):
    repository = session.query(Repository).filter(Repository.name == name).first()
    return repository


def insert_into_repositories(repo):
    session.add(repo)
    session.commit()


def delete_repositories():
    Base.metadata.drop_all(engine)


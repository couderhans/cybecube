from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session
from cybecube.database.repository import Repository

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Content(Base):
    __tablename__ = 'content'
    content_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250))
    repo_name = Column(Integer, ForeignKey(Repository.name))
    repository = relationship(Repository)


def create_table_content():
    Base.metadata.create_all(engine)


def delete_content():
    Base.metadata.drop_all(engine)


def insert_into_content(content):
    session.add(content)
    session.commit()
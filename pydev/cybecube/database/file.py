from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session
from cybecube.database.content import Content

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Url(Base):
    __tablename__ = 'url'
    url_id = Column(Integer, primary_key=True)
    url = Column(String(450), nullable=False)
    html_url = Column(String(450))
    git_url = Column(String(450))
    download_url = Column(String(450))


class File(Base):
    __tablename__ = 'file'
    file_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250))
    path = Column(String(250))
    sha = Column(String(250))
    size = Column(Integer)
    url_name = Column(String(250), ForeignKey(Url.url))
    url = relationship(Url)
    content_name = Column(String(250), ForeignKey(Content.name))
    content = relationship(Content)


def create_table_file():
    Base.metadata.create_all(engine)


def delete_table_file():
    Base.metadata.drop_all(engine)


def insert_into_file(file):
    session.add(file)
    session.commit()
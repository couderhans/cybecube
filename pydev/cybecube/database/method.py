from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session
from cybecube.database.clazz import Clazz

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Method(Base):
    __tablename__ = 'method'
    _id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    origin = Column(String(250))
    access = Column(String(250))
    type = Column(String(250))
    signature = Column(String(250))
    clazz_name = Column(String(250), ForeignKey(Clazz.name))
    clazz = relationship(Clazz)


def create_table_method():
    Base.metadata.create_all(engine)


def delete_table_method():
    Base.metadata.drop_all(engine)


def insert_into_Method(Method):
    session.add(Method)
    session.commit()


def get_Method(name):
    method = session.query(Method).filter(Method.name == name).first()
    return method
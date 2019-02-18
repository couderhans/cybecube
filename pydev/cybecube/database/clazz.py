from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session
from cybecube.database.package import Package

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Clazz(Base):
    __tablename__ = 'clazz'
    class_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250))
    package_name = Column(String(250), ForeignKey(Package.name))
    package = relationship(Package)


def create_table_class():
    Base.metadata.create_all(engine)


def delete_table_class():
    Base.metadata.drop_all(engine)


def insert_into_class(clazz):
    session.add(clazz)
    session.commit()


def get_clazz(name):
    clazz = session.query(Clazz).filter(Clazz.name == name).first()
    return clazz
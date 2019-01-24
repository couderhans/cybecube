from cybecube.database import engine
from cybecube.database import Base
from cybecube.database import session
from cybecube.database.file import File

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Package(Base):
    __tablename__ = 'package'
    package_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250))
    file_name = Column(String(250), ForeignKey(File.name))
    file = relationship(File)


def create_table_package():
    Base.metadata.create_all(engine)


def delete_table_package():
    Base.metadata.drop_all(engine)


def insert_into_package(package):
    session.add(package)
    session.commit()


def get_package(name):
    package = session.query(Package).filter(Package.name == name).first()
    return package

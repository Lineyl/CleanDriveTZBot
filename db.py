from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, BigInteger, Text, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import date
import random

engine = create_engine('sqlite:///users.db',echo=True, connect_args={"check_same_thread": False})
con = engine.connect()

Base = declarative_base()
metadata = MetaData()

class Roles(Base):
    __tablename__ = 'roles'
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(50), nullable=False)
    user = relationship('Users')


class Users(Base):
    __tablename__ = 'users'
    id = Column('id', BigInteger(), primary_key=True)
    fio = Column('fio', Text())
    datar = Column('datar', Date())
    id_role = Column('id_role', Integer(), ForeignKey('roles.id'))


Base.metadata.create_all(engine)

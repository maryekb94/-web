from sqlalchemy import (
    Column,
    Integer,
    Text,
    Boolean,
    ForeignKey
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Text)


class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    address = Column(Text)
    info = Column(Text)


class Good(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    manufacturer = relationship(Manufacturer)
    taste = Column(Text)
    available = Column(Boolean)
    price = Column(Integer)
    weight = Column(Integer)
    image_name = Column(Text)

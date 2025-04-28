from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Accommodation(Base):
    __tablename__ = "accommodation"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    numRooms = Column(Integer)
    isAvailable = Column(Boolean)

    host_id = Column(Integer, ForeignKey("host.id"))
    host = relationship("Host", back_populates="accommodation")


class Host(Base):
    __tablename__ = "host"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))

    country = relationship("Country", back_populates="host")

class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    continent = Column(String)

    hosts = relationship("Host", back_populates="country")


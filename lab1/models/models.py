from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum, Date
from sqlalchemy.orm import relationship, declarative_base

from lab1.models.schema import Category

Base = declarative_base()

class Accommodation(Base):
    __tablename__ = "accommodation"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    numRooms = Column(Integer)
    category = Column(Enum(Category), nullable=False)
    isAvailable = Column(Boolean)

    user_id = Column(Integer, ForeignKey("user.id"))
    host_id = Column(Integer, ForeignKey("host.id"))
    host = relationship("Host", back_populates="accommodations")



class Host(Base):
    __tablename__ = "host"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))

    country = relationship("Country", back_populates="host")
    accommodations = relationship("Accommodation", back_populates="host")

class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    continent = Column(String)

    host = relationship("Host", back_populates="country")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    temp_accomm = relationship("TemporaryAccommodation", back_populates="user")

class TemporaryAccommodation(Base):
    __tablename__ = "tempAcc"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    accommodation_id = Column(Integer, ForeignKey("accommodation.id"))

    user = relationship("User", back_populates="temp_accomm")
    accommodation = relationship("Accommodation")

class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True)
    accommodation_id = Column(Integer, ForeignKey("accommodation.id"))
    start = Column(Date, nullable=False)
    end = Column(Date, nullable=False)




from datetime import date, datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel
from pydantic.v1 import Field


class Category(Enum):
    Room = "Room"
    House = "House"
    Flat = "Flat"
    Apartment = "Apartment"
    Hotel = "Hotel"
    Motel = "Motel"


class CountrySchema(BaseModel):
    id: int
    name: str
    continent: str

    class Config:
        from_attributes = True





class UserSchema(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True

class HostSchema(BaseModel):
    id: int
    name: str
    surname: str
    country: CountrySchema
    user: UserSchema

    class Config:
        from_attributes = True


class AccommodationSchema(BaseModel):
    id: int
    name: str
    numRooms: int
    isAvailable: bool
    # user: UserSchema
    host: Optional[HostSchema] = None

    class Config:
        from_attributes = True


# DTO
class CreateAccommodation(BaseModel):
    name: str
    category: Optional[Category] = None
    host_id: Optional[int] = None
    country_id: Optional[int] = None
    numRooms: int
    isAvailable: bool


class UpdateAccommodation(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    host_id: Optional[int] = None
    country_id: Optional[int] = None
    isAvailable: Optional[bool] = None

##


class TemporaryAccommodationSchema(BaseModel):
    id: int
    user_id: int
    accommodation_id: int

    class Config:
        from_attributes = True


class CreateTempAcc(BaseModel):
    user_id: int
    accommodation_id: int
    start: datetime
    end: datetime


class AccommodationReservationsForUserSchema(BaseModel):
    temp_accomm: List[TemporaryAccommodationSchema] = Field(default_factory=list)

class ReservationsSchema(BaseModel):
    id: int
    accommodation_id: int
    start: date
    end: date

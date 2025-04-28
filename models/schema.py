from enum import Enum
from typing import Optional

from pydantic import BaseModel


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


class HostSchema(BaseModel):
    id: int
    name: str
    surname: str
    country: CountrySchema

    class Config:
        from_attributes = True


class AccommodationSchema(BaseModel):
    id: int
    name: str
    category: Category
    host: HostSchema
    numRooms: int
    isAvailable: bool

    class Config:
        from_attributes = True

#UFO(DTO) - i joke heh
class CreateAccommodation(BaseModel):
    name: str
    category_id: int
    host_id: int
    country_id: int
    numRooms: int
    isAvailable: bool


class UpdateAccommodation(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    host_id: Optional[int] = None
    country_id: Optional[int] = None
    isAvailable: Optional[bool] = None

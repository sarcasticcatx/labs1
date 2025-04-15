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


class Country(BaseModel):
    id: int
    name: str
    continent: str


class Host(BaseModel):
    id: int
    name: str
    surname: str
    country: Country

class Accomodation(BaseModel):
    id: int
    name: str
    category: Category
    host: Host
    numRooms: int
    isAvailable: bool


class CreateAccomodation(BaseModel):
    name: str
    category_id: int
    host_id: int
    country_id: int
    numRooms: int
    isAvailable: bool


class UpdateAccomodation(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    host_id: Optional[int] = None
    country_id: Optional[int] = None
    isAvailable: Optional[bool] = None



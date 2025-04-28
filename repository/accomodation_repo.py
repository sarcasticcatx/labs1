from sqlalchemy.orm import  Session
from models.models import Accommodation, Host
from models.schema import CreateAccommodation, UpdateAccommodation


def list_all(db: Session):
    return db.query(Accommodation).all()

def find_by_id(db: Session, accommodation_id: int):
   return db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()


def create_accommodation(db: Session, create_accommodation: CreateAccommodation):
    host_id = db.query(Host).filter(Host.id == create_accommodation.host_id).first()

    new_accommodation = Accommodation(
       name = create_accommodation.name,
       numRooms = create_accommodation.numRooms,
       isAvailable = create_accommodation.isAvailable,
       host_id = host_id )

    db.add(new_accommodation)
    db.commit()
    db.refresh(new_accommodation)

    return new_accommodation

def update_by_id(db: Session, update_accommodation: UpdateAccommodation, accommodation_id: int):
    accommodation = find_by_id(db, accommodation_id)

    if not accommodation:
        return

    for key, value in update_accommodation.model_dump(exclude_unset=True).items():
        setattr(accommodation, key, value)

    db.commit()
    db.refresh()

    return accommodation

def delete_by_id(db: Session, accommodation_id: int):
    accommodation = find_by_id(db, accommodation_id)

    if accommodation:
        db.delete(accommodation)
        db.commit()

    return accommodation

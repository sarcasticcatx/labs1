from sqlalchemy.orm import Session
from models.schema import CreateAccommodation, UpdateAccommodation
from repository import accomodation_repo

# list all
def list_all(db: Session):
    print("All accommodations listed")
    return accomodation_repo.list_all(db)

# find by id
def find_by_id(db: Session, accommodation_id: int):
    return accomodation_repo.find_by_id(db, accommodation_id)

# create
def createAcc(db: Session, create_data: CreateAccommodation):
    return accomodation_repo.create_accommodation(db, create_data)

# update
def update(db: Session, update_data: UpdateAccommodation, accommodation_id: int):
    return accomodation_repo.update_by_id(db, update_data,accommodation_id)

# and delete
def delete(db: Session, accommodation_id: int):
    accomodation_repo.delete_by_id(db, accommodation_id)


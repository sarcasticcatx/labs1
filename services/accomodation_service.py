from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models.models import Accommodation
from models.schema import CreateAccommodation, UpdateAccommodation
from repository import accomodation_repo

# List all accommodations
class CustomException:
    pass


def list_all(db: Session):
    try:
        print("All accommodations listed: ")
        return accomodation_repo.list_all(db)
    except SQLAlchemyError as e:
        print(f"Database error while listing accommodations: {e}")
        raise CustomException("Could not list accommodations.")
    except Exception as e:
        print(f"Unexpected error while listing accommodations: {e}")
        raise CustomException("An unexpected error occurred.")

# Find by ID
def find_by_id(db: Session, accommodation_id: int):
    try:
        # Query the accommodation by ID
        accommodation = db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()

        # If the accommodation is not found, return None
        if accommodation is None:
            print(f"Accommodation with ID {accommodation_id} not found.")
            return None

        print(f"Found accommodation: {accommodation}")
        return accommodation

    except SQLAlchemyError as e:
        # Log the database error in detail
        print(f"SQLAlchemy error occurred while querying accommodation by ID {accommodation_id}: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")

    except Exception as e:
        # Log any other errors
        print(f"Unexpected error occurred while querying accommodation by ID {accommodation_id}: {e}")
        raise HTTPException(status_code=500, detail="Unexpected error occurred")

# Create accommodation
def createAcc(db: Session, create_data: CreateAccommodation):
    print(createAcc.__class__)
    try:
        print(f" Created accommodation {create_data}")
        return accomodation_repo.create_accommodation(db, create_data)
    except SQLAlchemyError as e:
        print(f"Database error while creating accommodation: {e}")
        raise CustomException("Could not create accommodation.")
    except Exception as e:
        print(f"Unexpected error while creating accommodation: {e}")
        raise CustomException("An unexpected error occurred.")

# Update accommodation
def update(db: Session, update_data: UpdateAccommodation, accommodation_id: int):
    try:
        print(f" Updated accommodation {update_data}")
        return accomodation_repo.update_by_id(db, update_data, accommodation_id)
    except SQLAlchemyError as e:
        print(f"Database error while updating accommodation: {e}")
        raise CustomException("Could not update accommodation.")
    except Exception as e:
        print(f"Unexpected error while updating accommodation: {e}")
        raise CustomException("An unexpected error occurred.")

# Delete accommodation
def delete(db: Session, accommodation_id: int):
    try:
        print(f"Deleted accommodation with this id: {accommodation_id}")
        accomodation_repo.delete_by_id(db, accommodation_id)
    except SQLAlchemyError as e:
        print(f"Database error while deleting accommodation: {e}")
        raise CustomException("Could not delete accommodation.")
    except Exception as e:
        print(f"Unexpected error while deleting accommodation: {e}")
        raise CustomException("An unexpected error occurred.")
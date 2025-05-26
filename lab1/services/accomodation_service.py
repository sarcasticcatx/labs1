
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from lab1.models.models import Accommodation, TemporaryAccommodation, Reservation
from lab1.models.schema import CreateAccommodation, UpdateAccommodation, CreateTempAcc
from lab1.repository import accomodation_repo





def list_all(db: Session):
    try:
        print("All accommodations listed: ")
        return accomodation_repo.list_all(db)
    except SQLAlchemyError as e:
        print(f"Database error while listing accommodations: {e}")
        raise HTTPException(status_code=500, detail="Could not list accommodations.")
    except Exception as e:
        print(f"Unexpected error while listing accommodations: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

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
        raise HTTPException(status_code=500, detail="in create acc error.")
    except Exception as e:
        print(f"Unexpected error while creating accommodation: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


# create temporary accomodation
def createTempAcc(db: Session, create_data: CreateTempAcc):
    print(createTempAcc.__class__)
    try:
        print(f"Created temporary accommodation {create_data}")
        return accomodation_repo.create_temp_acc(db, create_data)
    except SQLAlchemyError as e:
        print(f"Database error while creating temp accommodation: {e}")
        raise HTTPException(status_code=500, detail="Could not create temporary accommodation.")
    except Exception as e:
        print(f"Unexpected error while creating temp accommodation: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

#     oвозможете корисникот да ги резервира сите сместувања од листата на приверемени резервации со
#     една акција, при што сите сместувања од листата ќе бидат означени како изнајмени


        temp_list = db.query(TemporaryAccommodation).filter(TemporaryAccommodation.user_id == create_data.user_id).all()

        if temp_list:
            for temp_acc in temp_list:
                accommodation = db.query(Accommodation).filter(Accommodation.id == temp_acc.accommodation_id).first()

                if accommodation and accommodation.isAvailable:
                    accommodation.isAvailable = False
                    db.commit()
                    print(f"Accommodation {accommodation.name} has been reserved.")
                else:
                    raise CustomException(f"Accommodation {accommodation.name} is no longer available for reservation.")

        return new_temp_acc


def reserve_all_temp_acc(db: Session, user_id: int):
    temp_list = db.query(TemporaryAccommodation).filter_by(user_id=user_id).all()
    if not temp_list:
        return False

    for temp in temp_list:
        reservation = Reservation(
            accommodation_id=temp.accommodation_id,
            user_id=temp.user_id,
            start=temp.start,
            end=temp.end
        )
        db.add(reservation)
        db.delete(temp)

    db.commit()
    return {"message": "All temporary reservations have been confirmed."}



# Update accommodation
def update(db: Session, update_data: UpdateAccommodation, accommodation_id: int):
    try:
        print(f" Updated accommodation {update_data}")
        return accomodation_repo.update_by_id(db, update_data, accommodation_id)
    except SQLAlchemyError as e:
        print(f"Database error while updating accommodation: {e}")
        raise HTTPException(status_code=500, detail="Could not update accommodation.")
    except Exception as e:
        print(f"Unexpected error while updating accommodation: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

# Delete accommodation
def delete(db: Session, accommodation_id: int):
    try:
        print(f"Deleted accommodation with this id: {accommodation_id}")
        accomodation_repo.delete_by_id(db, accommodation_id)
    except SQLAlchemyError as e:
        print(f"Database error while deleting accommodation: {e}")
        raise HTTPException(status_code=500, detail="Could not delete accommodation.")
    except Exception as e:
        print(f"Unexpected error while deleting accommodation: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
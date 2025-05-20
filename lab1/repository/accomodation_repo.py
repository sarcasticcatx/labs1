from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import  Session

from lab1.models.models import Accommodation, Host, TemporaryAccommodation
from lab1.models.schema import CreateAccommodation, UpdateAccommodation, CreateTempAcc


def list_all(db: Session):
    return db.query(Accommodation).all()

def find_by_id(db: Session, accommodation_id: int):
   return db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()


def create_accommodation(db: Session, create_accommodation: CreateAccommodation):
    # host = db.query(Host).filter(Host.id == create_accommodation.host_id).first()
    #
    # if not host:
    #     raise HTTPException(status_code=400, detail="Host not found")
    if create_accommodation.host_id:
        host = db.query(Host).filter(Host.id == create_accommodation.host_id).first()
        if not host:
            raise HTTPException(status_code=400, detail="poop")
    else:
        host = None

    new_accommodation = Accommodation(
       name = create_accommodation.name,
       numRooms = create_accommodation.numRooms,
       isAvailable = create_accommodation.isAvailable,
        category = create_accommodation.category,
       host_id = create_accommodation.host_id )

    db.add(new_accommodation)
    db.commit()
    db.refresh(new_accommodation)

    new_accommodation.host = host

    return new_accommodation


def create_temp_acc(db: Session, create_temp_acc: CreateTempAcc):

    # dali postoi akomodacijata
    accomm = db.query(Accommodation).filter(Accommodation.id == create_temp_acc.accommodation_id).first()
    if not accomm:
        raise HTTPException(status_code=404,detail="Accommodation not found")

    # корисникот може да додаде сместување во листата само ако сместувањето е слободно и
    # ако корисникот се обиде да додаде сместување што не е слободно, прикажете соодветна порака
    if not accomm.isAvailable:
        raise HTTPException(status_code=404,detail="Accommodation not available")


    # корисникот може да додава повеќе резервации во листата,
    # но не може да додаде резервација за некое сместување што веќе е во листата

    ifTempAccExist = db.query(TemporaryAccommodation).filter_by(
        user_id = create_temp_acc.user_id, accommodation_id = create_temp_acc.accommodation_id).first()

    if ifTempAccExist:
        raise HTTPException(status_code=400, detail="Accommodation is already in your temporary list")

    # овозможете корисниците да додаваат сместувања во својата листа на привремени резервации
    # и да ја прегледуваат пред да ја потврдат резервацијата

    # accommodation_id = db.query(Accommodation).filter(Accommodation.id == create_temp_acc.accommodation_id).first()

    new_temp_acc = TemporaryAccommodation(
        user_id = create_temp_acc.user_id,
        accommodation_id = create_temp_acc.accommodation_id

    )

    db.add(new_temp_acc)
    db.commit()
    db.refresh(new_temp_acc)

    return new_temp_acc


def update_by_id(db: Session, update_accommodation: UpdateAccommodation, accommodation_id: int):
    accommodation = find_by_id(db, accommodation_id)

    if not accommodation:
        return

    for key, value in update_accommodation.model_dump(exclude_unset=True).items():
        setattr(accommodation, key, value)

    db.commit()
    db.refresh(accommodation)

    return accommodation

def delete_by_id(db: Session, accommodation_id: int):
    accommodation = find_by_id(db, accommodation_id)

    if accommodation:
        db.delete(accommodation)
        db.commit()

    return accommodation
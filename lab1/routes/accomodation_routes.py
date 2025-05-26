from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from lab1.models.models import TemporaryAccommodation
from lab1.models.schema import AccommodationSchema, CreateAccommodation, UpdateAccommodation, \
    TemporaryAccommodationSchema, CreateTempAcc
from lab1.repository.accomodation_repo import create_temp_acc
from lab1.services import accomodation_service
from lab1.database.database import get_db


router = APIRouter(prefix="/api/accommodation", tags=["Accommodation"])

@router.get("/all", response_model=list[AccommodationSchema])
async def list_all(db: Session =  Depends(get_db)):
    try:
        accommodations = accomodation_service.list_all(db)
        if not accommodations:
            raise HTTPException(status_code=404, detail="No accommodations found")
        return accommodations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{accommodation_id}", response_model=AccommodationSchema)
async def find_by_id(accommodation_id: int, db: Session = Depends(get_db)):
    try:
        acc = accomodation_service.find_by_id(db, accommodation_id)
        print(acc)
        if acc is not None:
            return acc
        return JSONResponse(status_code=404, content={"message": f"Accommodation with id number: {accommodation_id} not found!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#овозможете корисниците да додаваат сместувања во својата листа на привремени
#резервации и да ја прегледуваат пред да ја потврдат резервацијата
@router.get("/temp-reservation/{user_id}")
def get_user_temp_reservations(user_id: int, db: Session = Depends(get_db)):
    temp_reservations = db.query(TemporaryAccommodation).filter_by(user_id=user_id).all()
    return temp_reservations


@router.post("/accommodations", response_model=AccommodationSchema)

async def createAcc(createAcc: CreateAccommodation, db: Session = Depends(get_db)):

    try:
        new_accommodation = accomodation_service.createAcc(db, createAcc)
        if not new_accommodation:
            raise HTTPException(status_code=400, detail="Failed to create accommodation")
        return new_accommodation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



#корисникот може да додава повеќе резервации во листата,
#но не може да додаде резервација за некое сместување што веќе е во листата
@router.post("/temp-reservation")
def create_temp_reservation(create_data: CreateTempAcc, db: Session = Depends(get_db)):
    return accomodation_service.createTempAcc(db, create_data)





@router.put("/edit/{accommodation_id}", response_model=AccommodationSchema)
async def update_by_id(accommodation_id:int, update_acc: UpdateAccommodation, db: Session = Depends(get_db)):
    try:
        acc = accomodation_service.find_by_id(db, accommodation_id)
        if acc is not None:
            return accomodation_service.update(db, update_acc, accommodation_id)
        return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accommodation_id} not found!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{accommodation_id}")
async def delete_acc(accommodation_id: int, db: Session = Depends(get_db)):
    acc = accomodation_service.find_by_id(db, accommodation_id)
    if acc is not None:
        accomodation_service.delete(db, accommodation_id)
        return JSONResponse(status_code=200, content={"message": f"Accommodation with id {accommodation_id} deleted successfully"})
    else:
        return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accommodation_id} not found!"})

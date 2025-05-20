from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from lab1.models.schema import TemporaryAccommodationSchema, CreateTempAcc
from lab1.services import accomodation_service
from lab1.database.database import get_db
from lab1.models.models import TemporaryAccommodation


router = APIRouter(prefix="/api/temp-accommodation", tags=["TemporaryAccommodationSchema"])

@router.post("/temporary-res", response_model=TemporaryAccommodationSchema)
async def createTempAcc(createTempAcc: CreateTempAcc, db: Session = Depends(get_db())):
    try:
        new_temp_accommodation = accomodation_service.createTempAcc(db, createTempAcc)
        if not new_temp_accommodation:
            raise HTTPException(status_code=400, detail="Failed to create temporary accommodation")
        return new_temp_accommodation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("reserve-all-temp-acc", response_model=dict)
async def reserve_all_temp_accommodations(user_id: int, db: Session = Depends(get_db())):
    try:
        result = accomodation_service.createTempAcc(db, user_id)
        if not result:
            raise HTTPException(status_code=400, detail="Failed to reserve all")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/temporary-res{user_id}", response_model=list[TemporaryAccommodationSchema])
async def get_temp_acc_user(user_id: int, db: Session = Depends(get_db)):
    try:
        userList = db.query(TemporaryAccommodation).filter_by(user_id = user_id).all()
        print(userList)
        if userList is not None:
            return userList
        return JSONResponse(status_code=404, content={"message": f"Temporary accommodation with user id number: {user_id} not found!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
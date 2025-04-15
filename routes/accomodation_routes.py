from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.schema import Accomodation, CreateAccomodation, UpdateAccomodation
from services import accomodation_service

router = APIRouter(prefix="/api/accommodation", tags=["Accommodation"])

@router.get("", response_model=list[Accomodation])
async def list_all():
    return accomodation_service.list_all()

@router.get("/{accomodation_id}", response_model=Accomodation)
async def find_by_id(accomodation_id: int):
    acc = accomodation_service.find_by_id(accomodation_id)
    if acc is not None:
        return acc
    return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accomodation_id} not found!"})

@router.post("", response_model=CreateAccomodation)
async def createAcc(createAcc: CreateAccomodation):
    return createAcc

@router.put("/{accomodation_id}", response_model=Accomodation)
async def update_by_id(accomodation_id:int, update_acc: UpdateAccomodation):
    acc = accomodation_service.find_by_id(accomodation_id)
    if acc is not None:
        return accomodation_service.update(update_acc, accomodation_id)
    return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accomodation_id} not found!"})

@router.delete("/{accomodation_id}")
async def delete_acc(accomodation_id: int):
    acc = accomodation_service.find_by_id(accomodation_id)
    if acc is not None:
        accomodation_service.delete(accomodation_id)
        return JSONResponse(status_code=200, content={"message": f"Accommodation with id {accomodation_id} deleted successfully"})
    else:
        return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accomodation_id} not found!"})

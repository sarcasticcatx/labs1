# from http.client import HTTPException
#
# from fastapi import APIRouter
# from fastapi.params import Depends
# from sqlalchemy.orm import Session
#
# from lab1.database.database import get_db
# from lab1.models.schema import Category
# from lab1.services import category_service
#
# router = APIRouter(prefix="/api/category", tags=["Category"])
#
# @router.get("/categories", response_model=list[Category])
# async def list_all(db: Session =  Depends(get_db)):
#     try:
#         accommodations = category_service.list_all(db)
#         if not accommodations:
#             raise HTTPException(status_code=404, detail="No accommodations found")
#         return accommodations
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# from http.client import HTTPException
#
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.orm import Session
#
# from lab1.repository import category_repo
#
#
# def list_all(db: Session):
#     try:
#         print("All categories listed: ")
#         return category_repo.list_all(db)
#     except SQLAlchemyError as e:
#         print(f"Database error while listing categories: {e}")
#         raise HTTPException(status_code=500, detail="Could not list categories.")
#     except Exception as e:
#         print(f"Unexpected error while listing categories: {e}")
#         raise HTTPException(status_code=500, detail="An unexpected error occurred.")
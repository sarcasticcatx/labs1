from sqlalchemy.orm import  Session

from lab1.models.models import Country

def list_all(db: Session):
    return db.query(Country).all()

def find_by_id(db: Session, country_id: int):
    return db.query(Country).filter(Country.id == country_id).first()
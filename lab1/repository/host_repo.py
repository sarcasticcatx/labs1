from sqlalchemy.orm import Session

from lab1.models.models import Host

def list_all(db: Session):
    return db.query(Host).all()

def find_by_id(db: Session ,host_id: int):
    return db.query(Host).filter(Host.id == host_id).first()

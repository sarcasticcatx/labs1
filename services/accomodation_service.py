from repository import accomodation_repo
from models.schema import CreateAccomodation, UpdateAccomodation
from database.database import accomodation


def list_all():
    print("Current accommodations:", accomodation)
    return accomodation_repo.list_all()

def find_by_id(accomodation_id: int):
    return accomodation_repo.find_by_id(accomodation_id)

def createAcc(create_data: CreateAccomodation):
    new_id = len(accomodation) + 1
    new_acc = {
        "id": new_id,
        "name": create_data.name,
        "category_id": create_data.category_id,
        "host_id": create_data.host_id,
        "country_id": create_data.country_id,
        "numRooms": create_data.numRooms,
        "isAvailable": create_data.isAvailable
    }
    accomodation.append(new_acc)
    print("succsessfully attached to accomodation")
    return new_acc


def update(updateAcc: UpdateAccomodation, accomodation_id: int):
    return accomodation_repo.update_by_id(updateAcc, accomodation_id)

def delete(accomodation_id: int):
    accomodation_repo.delete_by_id(accomodation_id)


from database.database import accomodation
from models.schema import CreateAccomodation, UpdateAccomodation
from database.database import category, host


def list_all():
    return accomodation

def find_by_id(accomodation_id: int):
    for accomodations in accomodation:
        if accomodations["id"] == accomodation_id:
            return accomodations
    return None

def find_cat_by_id(category_id: int):
    for cat in category:
        if cat["id"] == category_id:
            return cat
    return None

def find_host_by_id(host_id:int):
    for hosts in host:
        if host["id"] == host_id:
            return hosts
    return None


def create_accomodation(create_accomodotian: CreateAccomodation):
    new_accomodation = {
        "id": len(accomodation) + 1,
          "name": create_accomodotian.name,
        "category_id": create_accomodotian.category_id,
        "host_id": create_accomodotian.host_id,
        "country_id": create_accomodotian.country_id,
        "numRooms": create_accomodotian.numRooms,
        "isAvailable": create_accomodotian.isAvailable
    }
    accomodation.append(new_accomodation)
    return new_accomodation

def update_by_id(update_accomodation: UpdateAccomodation, accomodation_id: int):
    accomodation = find_by_id(accomodation_id)

    if not accomodation:
        return

    accomodation["name"] = update_accomodation.name
    accomodation["category_id"] = update_accomodation.category_id
    accomodation["host_id"] = update_accomodation.host_id
    accomodation["country_id"] = update_accomodation.country_id
    accomodation["numRooms"] = update_accomodation.numRooms
    accomodation["isAvailable"] = update_accomodation.isAvailable

def delete_by_id(accomodation_id: int):
    accomodation = find_by_id(accomodation_id)

    if not accomodation:
        return

    accomodation.remove(accomodation)
    return True
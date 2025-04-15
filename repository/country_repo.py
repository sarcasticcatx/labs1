from database.database import countries


def list_all():
    return countries

def find_by_id(country_id: int):
    for count in countries:
        if count["id"] == country_id:
            return count
    return None
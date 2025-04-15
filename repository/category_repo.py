from database.database import category


def list_all():
    return category

def find_by_id(cat_id: int):
    for cat in category:
        if cat["id"] == cat_id:
            return cat
    return None
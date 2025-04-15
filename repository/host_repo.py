from database.database import host


def list_all():
    return host

def find_by_id(host_id: int):
    for hosts in host:
        if hosts["id"] == host_id:
            return hosts
    return None
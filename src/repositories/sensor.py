from models.sensor import Sensor
from utils.db import executeSelect


def getSensorById(id: int) -> Sensor:
    query = f"SELECT name FROM sensor WHERE id = {id};"
    name = executeSelect(query)[0][0]
    return Sensor(id, name)

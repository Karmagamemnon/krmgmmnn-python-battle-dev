from models.sensor import Sensor
from utils.db import executeSelect


def getAll() -> list[Sensor]:
    query = f"SELECT id, name FROM sensor;"
    result = executeSelect(query)
    sensors = []
    for row in result:
        sensor = Sensor(row[0], row[1])
        sensors.append(sensor)
    return sensors


def getSensorById(id: int) -> Sensor:
    query = f"SELECT name FROM sensor WHERE id = {id};"
    name = executeSelect(query)[0][0]
    return Sensor(id, name)

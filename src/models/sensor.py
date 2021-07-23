from __future__ import annotations
from models.data import Data
from utils.db import count, executeSelect, executeTransaction


class Sensor:

    def __init__(self, id: int, name: str = None):
        self.id = id
        self.name = name

    def doesSensorExist(self) -> bool:
        query = f"SELECT COUNT(1) FROM sensor WHERE id = {self.id}"
        exists = count(query) > 0
        return exists

    def getInsertQuery(self):
        return (
            "INSERT INTO sensor (id) " +
            f"VALUES ({self.id});"
        )

    def getLast100Data(self) -> list[Data]:
        query = f"SELECT timestamp, temperature, humidity, rssi, battery_voltage_status FROM data WHERE id_sensor = {self.id} ORDER BY timestamp DESC;"
        result = executeSelect(query)
        dataset = []
        for row in result:
            data = Data(None, row[0], row[1], row[2], row[3], row[4], self.id)
            dataset.append(data)
        return dataset

    def setName(self, name: str) -> None:
        query = f"UPDATE sensor SET name = '{name}' WHERE id = {self.id}"
        executeTransaction([query])

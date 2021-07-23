from utils.db import count, executeSelectQuery, execute


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

    def getSensorNameById(id):
        query = f"SELECT name FROM sensor WHERE id = {id}"
        name = executeSelectQuery(query)[0][0]
        return name

    def updateSensorNameQuery(id: int, name: str):
        query = f"UPDATE sensor SET name = '{name}' WHERE id = {id}"
        execute([query])
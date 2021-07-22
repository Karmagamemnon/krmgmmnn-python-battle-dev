from utils.db import count


class Sensor:

    def __init__(self, id):
        self.id = id

    def doesSensorExist(self) -> bool:
        query = f"SELECT COUNT(1) FROM sensor WHERE id = {self.id}"
        exists = count(query) > 0
        return exists

    def getInsertQuery(self):
        return (
            "INSERT INTO sensor (id) " +
            f"VALUES ({self.id});"
        )

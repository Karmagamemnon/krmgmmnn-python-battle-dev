class Sensor:

    def __init__(self, id):
        self.id = id

    def getInsertQuery(self):
        return (
            "INSERT INTO sample (id) " +
            f"VALUES ({self.id});"
        )
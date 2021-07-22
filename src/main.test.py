import requests
import unittest
from utils.db import execute
from models.sensor import Sensor
from models.sample import Sample


def jsonToSamples(jsonResponse):
    samples = []
    for sampleData in jsonResponse:
        sampleObject = Sample(sampleData)
        samples.append(sampleObject)
    return samples


class TestMainMethods(unittest.TestCase):

    def test_getLastSamples(self):
        response = requests.get(
            "http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
        json = response.json()
        samples = jsonToSamples(json)

        queries: list[str] = []

        for sample in samples:
            if(not sample.doesSampleExist()):
                queries.append(sample.getInsertQuery())

                dataset = sample.getDataset()
                for data in dataset:
                    sensor = Sensor(data.idSensor)
                    if(not sensor.doesSensorExist()):
                        queries.append(sensor.getInsertQuery())
                    else:
                        print(f"Sensor {sensor.id} already exists in database")

                    queries.append(data.getInsertQuery())

            else:
                print(f"Sample {sample.id} already exists in database")

        print(queries)
        execute(queries)


if __name__ == '__main__':
    unittest.main()

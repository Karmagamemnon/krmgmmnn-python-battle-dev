# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
from utils.db import execute
import threading
import time
import requests
from models.sensor import Sensor
from models.sample import Sample


def jsonToSamples(jsonResponse: str) -> list[Sample]:
    samples: list[Sample] = []
    for sampleData in jsonResponse:
        newSample = Sample(sampleData)
        samples.append(newSample)
    return samples


def getLastSamples():
    response = requests.get(
        "http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    json = response.json()
    samples = jsonToSamples(json)

    for sample in samples:
        if(not sample.doesSampleExist()):
            query = query + sample.getInsertQuery() + "\n"

            dataset = sample.getDataset()
            for data in dataset:
                sensor = Sensor(data.idSensor)
                if(not sensor.doesSensorExist()):
                    query = query + sensor.getInsertQuery() + "\n"
                else:
                    print(f"Sensor {sensor.id} already exists in database")
                query = query + data.getInsertQuery() + "\n"

            execute(query)
        else:
            print(f"Sample {sample.id} already exists in database")

    print(query)
    time.sleep(300)


if __name__ == "__main__":
    threading.Thread(target=getLastSamples()).start()

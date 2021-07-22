# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import threading
import time
import requests
from models.sensor import Sensor
from models.sample import Sample

def jsonToSamples(jsonResponse: str) -> list[Sample]:
    samples = []
    for sampleData in jsonResponse:
        newSample = Sample(sampleData)
        samples.append(newSample)
    return samples

def getLastSamples():
    response = requests.get(
        "http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    json = response.json()
    samples = jsonToSamples(json)

    query = ""

    for sample in samples:
        query = query + sample.getInsertQuery() + "\n"
        dataset = sample.getDataset()

        for data in dataset:
            sensor = Sensor(data.idSensor)
            query = query + sensor.getInsertQuery() + "\n"
            query = query + data.getInsertQuery() + "\n"

    print(query)
    time.sleep(300)


if __name__ == "__main__":
    threading.Thread(target=getLastSamples()).start()

# récupérer relevés

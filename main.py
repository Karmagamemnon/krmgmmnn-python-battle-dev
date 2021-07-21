# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import requests
import db
from sample import Sample


def formatJson(jsonResponse):
    json = {}
    for indexSensor, sensor in enumerate(jsonResponse):
        sensorData = {}
        for indexData, data in enumerate(sensor):
            sensorData[indexData] = data
        json[indexSensor] = sensorData
    return json

def jsonToSamples(jsonResponse):
    samples = []
    for indexSample, sampleData in enumerate(jsonResponse):
        sampleObject = Sample(sampleData)
        samples.append(sampleObject)
    return samples

if __name__ == "__main__":
    response = requests.get("http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    samples = jsonToSamples(response.json())
    db.saveSample(samples[0])

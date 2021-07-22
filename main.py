# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import requests
import db
from models.sample import Sample


def jsonToSamples(jsonResponse):
    samples = []
    for indexSample, sampleData in enumerate(jsonResponse):
        sampleObject = Sample(sampleData)
        samples.append(sampleObject)
    return samples


if __name__ == "__main__":
    response = requests.get(
        "http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    samples = jsonToSamples(response.json())
    for sample in samples:
        db.saveSample(sample)
        sample.decryptRawdata()

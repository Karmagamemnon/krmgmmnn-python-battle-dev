# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import atexit
from utils.db import executeTransaction, executeSelect
import requests
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from models.sensor import Sensor
from models.sample import Sample
from views.details import detailsPage
from views.index import indexPage

app = Flask(__name__)


def jsonToSamples(jsonResponse):
    samples = []
    for sampleData in jsonResponse:
        sampleObject = Sample(sampleData)
        samples.append(sampleObject)
    return samples


@app.route("/")
def index():
    return indexPage()


@app.route("/details/<int:idSensor>")
def details(idSensor: int):
    return detailsPage(idSensor)


def getLastSamples():
    response = requests.get("http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    json = response.json()
    samples = jsonToSamples(json)

    queries: list[str] = []

    for sample in samples:
        if (not sample.doesSampleExist()):
            queries.append(sample.getInsertQuery())

            dataset = sample.getDataset()
            for data in dataset:
                sensor = Sensor(data.idSensor)
                if (not sensor.doesSensorExist()):
                    queries.append(sensor.getInsertQuery())
                else:
                    print(f"Sensor {sensor.id} already exists in database")

                queries.append(data.getInsertQuery())

        else:
            print(f"Sample {sample.id} already exists in database")

    print(queries)
    executeTransaction(queries)


scheduler = BackgroundScheduler()
scheduler.add_job(func=getLastSamples, trigger="interval", seconds=300)
scheduler.start()
app.run(port=8081)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import atexit
from utils.db import execute, executeSelectQuery
import requests
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from models.sensor import Sensor
from models.sample import Sample
from views.index import index_page

app = Flask(__name__)


def jsonToSamples(jsonResponse):
    samples = []
    for sampleData in jsonResponse:
        sampleObject = Sample(sampleData)
        samples.append(sampleObject)
    return samples


@app.route("/")
def index():
    return index_page()

@app.route("/data")
def getData():
    query = "SELECT * FROM (SELECT * FROM `data` ORDER BY `timestamp` DESC) AS orderBy GROUP BY `id_sensor`"
    print(executeSelectQuery(query))
    return str(executeSelectQuery(query))


def getLastSamples():
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


scheduler = BackgroundScheduler()
scheduler.add_job(func=getLastSamples, trigger="interval", seconds=60)
scheduler.start()
app.run(port=8081)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

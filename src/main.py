# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import atexit
from utils.db import execute
import time
import requests
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from models.sensor import Sensor
from models.sample import Sample

app = Flask(__name__)


def jsonToSamples(jsonResponse):
    samples = []
    for sampleData in jsonResponse:
        sampleObject = Sample(sampleData)
        samples.append(sampleObject)
    return samples


@app.route("/")
def index():
    return 'Index page'


def getLastSamples():
    while True:
        response = requests.get(
            "http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
        json = response.json()
        samples = jsonToSamples(json)

        for sample in samples:
            if(not sample.doesSampleExist()):
                query = sample.getInsertQuery() + "\n"

                dataset = sample.getDataset()
                for data in dataset:
                    sensor = Sensor(data.idSensor)
                    if(not sensor.doesSensorExist()):
                        query = query + sensor.getInsertQuery() + "\n"
                    else:
                        print(f"Sensor {sensor.id} already exists in database")
                    query = query + data.getInsertQuery() + "\n"

                print(query)
                execute(query)
            else:
                print(f"Sample {sample.id} already exists in database")


scheduler = BackgroundScheduler()
scheduler.add_job(func=getLastSamples, trigger="interval", seconds=60)
scheduler.start()
# app.run(port=8081)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

getLastSamples()
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
    query = "SELECT `data1`.`timestamp`, `data1`.`temperature`, `data1`.`humidity`, `data1`.`rssi`, `data1`.`battery_voltage_status`, `data1`.`id_sensor` FROM `data` as data1 JOIN (SELECT * FROM `data` as data2 GROUP BY `data2`.`timestamp` ORDER BY `data2`.`timestamp` DESC) as data3 ON `data3`.`id` = `data1`.`id` GROUP BY `data1`.`id_sensor`"
    result = executeSelectQuery(query)
    listData = []
    for row in result:
        data = Data(None, row[0], row[1], row[2], row[3], row[4], row[5])
        listData.append(data)
    return jsonify(dataList=[data.serialize() for data in listData])


def getLastSamples():
    response = requests.get(
        "http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
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
    execute(queries)


scheduler = BackgroundScheduler()
scheduler.add_job(func=getLastSamples, trigger="interval", seconds=300)
scheduler.start()
app.run(port=8081)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

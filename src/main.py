# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import atexit
import src.db
import time
import requests
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from src.models.sample import Sample

app = Flask(__name__)

def getlastsamples():
    while True:
        response = requests.get(
            "http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
        samples = jsonToSamples(response.json())
        for sample in samples:
            src.db.saveSample(sample)
            sample.decryptRawdata()
        time.sleep(300)

def jsonToSamples(jsonResponse):
    samples = []
    for indexSample, sampleData in enumerate(jsonResponse):
        sampleObject = Sample(sampleData)
        samples.append(sampleObject)
    return samples


@app.route("/")
def index():
    return 'Index page'


scheduler = BackgroundScheduler()
scheduler.add_job(func=getlastsamples, trigger="interval", seconds=60)
scheduler.start()
app.run(port=8081)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


from dominate.tags import *
from models.data import Data
from utils.tools import strftimestamp
from repositories.sensor import getSensorById
from views.base import getBasePage, getTitle

def indexPage():

    doc = getBasePage()
    title = getTitle()

    with doc.body:
        with div(cls="container"):

            with div(cls="jumbotron"):
                h1(title, style="font-family: 'Press Start 2P', cursive;")

            with div(cls="d-flex flex-row", style="gap: 1rem;"):
                dataset = Data.getMostRecentDataForEachSensor()
                for data in dataset:

                    with div(cls="card"):

                        img(cls="card-img-top", style="height: 240px; width: 320px;",
                            src="https://www.revolution-energetique.com/wp-content/uploads/2021/05/satellite-5a3c2679b39d030037a12868-768x504.jpg")

                        with div(cls="card-body"):

                            sensor = getSensorById(data.idSensor)
                            h5Title = f"Sensor {sensor.name}" if sensor.name != None else f"Sensor #{str(sensor.id).zfill(8)}"
                            with h5(h5Title, cls="card-title"):
                                if(data.batteryVoltageStatus == 1):
                                    span("Low battery", cls="badge alert-warning")

                            h6(strftimestamp(data.timestamp),
                               cls="card-subtitle mb-2 text-muted")

                            with div():
                                i(cls="fas fa-thermometer-three-quarters fa-fw")
                                span(f" {data.temperature}°C")
                            if(data.humidity != None):
                                with div():
                                    i(cls="fas fa-tint fa-fw")
                                    span(f" {data.humidity}%")
                            with div():
                                i(cls="fa fa-signal fa-fw")
                                span(f" -{data.rssi}dBm")

                            hr()

                            a("Previous data", href=f"/details/{data.idSensor}", cls="btn btn-secondary")

    return doc.render()
from logging import PlaceHolder
from dominate.tags import *
from models.sensor import Sensor
from utils.tools import strftimestamp
from views.base import getBasePage, getTitle
from repositories.sensor import getSensorById

def detailsPage(idSensor):

    doc = getBasePage(delay=300)
    title = getTitle()
    sensor = getSensorById(idSensor)
    dataset = sensor.getData()

    with doc.body:
        attr(style="background-color: darkgrey; min-height: 100%;")
        with div(cls="container", style="background-color: white; min-height: 100%;"):

            with div(cls="jumbotron py-3"):
                h1(title, style="font-family: 'Press Start 2P', cursive;")
                for _ in range(0, 5):
                    i(cls="fas fa-star fa-2x")

            with div(cls="mb-3"):
                with div(cls="d-flex flex-row justify-content-between"):
                    h3Title = f"Sensor {sensor.name}" if sensor.name else f"Sensor #{str(sensor.id).zfill(8)}"
                    h3(h3Title, style="font-family: 'Press Start 2P', cursive;")
                    with form(action=f"/api/sensor/{sensor.id}", method="POST"):
                        with div(cls="d-flex flex-row"):
                            input_(name="name", cls="form-control", type="text", PlaceHolder="ex: capteur du congélateur", max=45)
                            button("CHANGE SENSOR NAME", type="submit", cls="btn btn-secondary")
                a("RETURN TO HOMEPAGE", href="/", style="font-family: 'Press Start 2P', cursive;")

            with table(cls="table table-sm table-striped"):
                with thead():
                    with tr():
                        with th(scope="col"):
                            i(cls="fas fa-clock")
                            span("Date")
                        with th(scope="col"):
                            i(cls="fas fa-thermometer-three-quarters")
                            span("Temperature")
                        with th(scope="col"):
                            i(cls="fas fa-tint")
                            span("Humidity")
                        with th(scope="col"):
                            i(cls="fa fa-signal")
                            span("RSSI")
                with tbody():
                    for data in dataset:
                        with tr():
                            td(strftimestamp(data.timestamp))
                            td(f"{data.temperature}°C")
                            td("No data" if data.humidity == None else f"{data.humidity}%")
                            td(f"-{data.rssi}dBm")

    return doc.render()

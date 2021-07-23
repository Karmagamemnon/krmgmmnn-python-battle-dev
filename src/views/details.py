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
    dataset = sensor.getLast100Data()

    with doc.body:
        with div(cls="container"):

            with div(cls="jumbotron"):
                h1(title, style="font-family: 'Press Start 2P', cursive;")

            with div(cls="mb-3"):
                with div(cls="d-flex flex-row justify-content-between"):
                    h3Title = f"Sensor {sensor.name}" if sensor.name != None else f"Sensor #{str(sensor.id).zfill(8)}"
                    h3(h3Title, style="font-family: 'Press Start 2P', cursive;")
                    with div(cls="d-flex flex-row"):
                        input_(cls="form-control", type="text", PlaceHolder="ex: capteur du congélateur", max=45)
                        button("CHANGE", type="button", cls="btn btn-secondary")
                a("RETURN TO HOMEPAGE", href="/", style="font-family: 'Press Start 2P', cursive;")

            with table(cls="table table-sm table-striped"):
                with thead():
                    with tr():
                        for tag in ["Date", "Temperature", "Humidity", "RSSI"]:
                            th(tag, scope="col")
                with tbody():
                    for data in dataset:
                        with tr():
                            td(strftimestamp(data.timestamp))
                            td(f"{data.temperature}°C")
                            td("No data" if data.humidity == None else f"{data.humidity}%")
                            td(f"-{data.rssi}dBm")

    return doc.render()

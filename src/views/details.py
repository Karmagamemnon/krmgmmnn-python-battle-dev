from dominate.tags import *
from models.sensor import Sensor
from utils.tools import strftimestamp
from views.base import getBasePage, getTitle


def detailsPage(idSensor):

    doc = getBasePage()
    title = getTitle()
    sensor = Sensor(idSensor)
    dataset = sensor.getLast100Data()

    with doc.body:
        with div(cls="container"):

            with div(cls="jumbotron"):
                h1(title, style="font-family: 'Press Start 2P', cursive;")

            with div(cls="mb-3"):
                h3(f"Sensor #{str(idSensor).zfill(8)}", style="font-family: 'Press Start 2P', cursive;")
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
                            td(f"-{data.temperature}dBm")

    return doc.render()

from dominate.tags import *
from dominate import document
from models.data import Data
from models.sample import Sample
from utils.db import executeSelectQuery

title = "Ultimate sensors UI premium deluxe day one master edition standard"


def index_page():

    query = "SELECT * FROM (SELECT * FROM `data` ORDER BY `timestamp` DESC) AS orderBy GROUP BY `id_sensor`"
    dataset = executeSelectQuery(query)

    doc = base_page()
    doc.title = title
    with doc.body:
        with div(cls="container"):

            with div(cls="jumbotron"):
                h1(title, style="font-family: 'Press Start 2P', cursive;")

            with div(cls="d-flex flex-row", style="gap: 1rem;"):
                for databerk in dataset:
                    data = Data()
                    data.idSensor = databerk[6]
                    data.timestamp = databerk[5]
                    data.batteryVoltageStatus = databerk[4]
                    data.temperature = databerk[1]
                    data.humidity = databerk[2]
                    data.rssi = databerk[3]

                    with div(cls="card", style="width: 33%;"):

                        img(cls="card-img-top p-5", style="width: 15rem;",
                            src="https://mon-guide-campingcar.com/wp-content/uploads/2021/01/COMMENT-INSTALLER-UNE-PARABOLE-DE-CAMPING-CAR.png")

                        with div(cls="card-body"):

                            with h5(f"Sensor #{data.idSensor}", cls="card-title"):
                                if(data.batteryVoltageStatus == 1):
                                    span("Low battery", cls="badge alert-warning")

                            h6(data.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
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

                            # div(f"Temperature = {data.temperature}°C",
                            #     cls="card-text")
                            # if(data.humidity != None):
                            #     div(f"Humidity = {data.humidity}%",
                            #         cls="card-text")
                            # div(f"RSSI = -{data.rssi}dBm", cls="card-text")

                            hr()

                            a("Older data", href="#", cls="btn btn-secondary")

    return doc.render()


def base_page():

    doc = document(title=title)

    with doc.head:
        link(rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css')
        link(rel='preconnect', href='https://fonts.googleapis.com')
        link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=True)
        link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap', crossorigin=True)
        script(type='text/javascript', src='https://code.jquery.com/jquery-3.2.1.slim.min.js')
        script(type='text/javascript', src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js')
        script(type='text/javascript', src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js', crossorigin="anonymous")

    return doc

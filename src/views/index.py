from dominate.tags import *
from dominate import document
from models.data import Data
from utils.db import executeSelectQuery

title = "Ultimate sensors UI premium deluxe day one master edition standard"


def index_page():

    doc = base_page()
    doc.title = title
    with doc.body:
        with div(cls="container"):

            with div(cls="jumbotron"):
                h1(title, style="font-family: 'Press Start 2P', cursive;")

            with div(cls="d-flex flex-row", style="gap: 1rem;"):
                dataset = Data.getLastDataForEachSensor()
                for data in dataset:

                    with div(cls="card"):

                        img(cls="card-img-top", style="height: 240px; width: 320px;",
                            src="https://www.revolution-energetique.com/wp-content/uploads/2021/05/satellite-5a3c2679b39d030037a12868-768x504.jpg")

                        with div(cls="card-body"):

                            with h5(f"Sensor #{str(data.idSensor).zfill(8)}", cls="card-title"):
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

                            a("Previous data", href="#", cls="btn btn-secondary")

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
        script(type='text/javascript', src='https://kit.fontawesome.com/fa3537a8a2.js', crossorigin="anonymous")

    return doc

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

            h1(title)

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

                            div(f"Temperature = {data.temperature}°C",
                                cls="card-text")
                            if(data.humidity != None):
                                div(f"Humidity = {data.humidity}%",
                                    cls="card-text")
                            div(f"RSSI = -{data.rssi}dBm", cls="card-text")
                            hr()
                            a("Older data", href="#", cls="btn btn-secondary")

    return doc.render()


def base_page():

    doc = document(title=title)

    with doc.head:
        link(rel='stylesheet',
             href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css')
        script(type='text/javascript',
               src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js')
        script(type='text/javascript',
               src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js')
    return doc

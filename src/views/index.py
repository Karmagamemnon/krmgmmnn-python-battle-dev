from dominate.tags import *
from dominate import document
from utils.db import executeSelectQuery

title = "Ultimate sensors UI deluxe GOTY Day one edition"


def index_page():

    query = "SELECT * FROM (SELECT * FROM `data` ORDER BY `timestamp` DESC) AS orderBy GROUP BY `id_sensor`"
    dataset = executeSelectQuery(query)

    doc = base_page()
    doc.title = title
    with doc.body:
        with div():
            attr(cls="container")
            h1(title)
            with div(cls="card"):
                img(cls="card-img-top p-1", style="width: 15rem;", src="https://mon-guide-campingcar.com/wp-content/uploads/2021/01/COMMENT-INSTALLER-UNE-PARABOLE-DE-CAMPING-CAR.png")
                with div(cls="card-body"):
                    h5("Sensor boobipboop", cls="card-title")
                    div("Timestamp = 2021-07-22 15:59:25", cls="card-text")
                    div("Battery status = 0", cls="card-text")
                    div("Battery voltage = 3670mV", cls="card-text")
                    div("Temperature = 32.8°C", cls="card-text")
                    div("Humidity = 48%", cls="card-text")
                    div("RSSI = -71dBm", cls="card-text")
                    a("Previous data", href="#", cls="btn btn-secondary")

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

import requests
import json

def getTemperature(city: str = "bordeaux"):
    city = city if city else "bordeaux"
    response = requests.get(
        f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=donnees-synop-essentielles-omm&q={city}&sort=date&facet=date&facet=nom&facet=temps_present&facet=libgeo&facet=nom_epci&facet=nom_dept&facet=nom_reg")
    data = response.json()
    for jsonRow in data:
        if("records" in jsonRow):
            records = data[jsonRow][0]
            for recordRow in records:
                if("fields" in recordRow):
                    for fieldRow in records[recordRow]:
                        if("libgeo" in fieldRow):
                            ville = records[recordRow][fieldRow]
                        if("tc" in fieldRow):
                            temperature = records[recordRow][fieldRow]

    data = {"ville": ville, "temperature": temperature}
    return json.dumps(data)

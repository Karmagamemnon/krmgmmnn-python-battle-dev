# Python Battle Dev
# Groups compose of:
#    - Kevin PEETERS
#    - Gregory MOU KUI
import requests
import json

def formatJson(jsonResponse):
    json = {}
    for indexCapteur, capteur in enumerate(jsonResponse):
        capteurData = {}
        for indexData, data in enumerate(capteur):
            capteurData[indexData] = data
        json[indexCapteur] = capteurData
    return json

if __name__ == "__main__":
    response = requests.get("http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    json = formatJson(response.json())
    print(json)

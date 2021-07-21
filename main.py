# Python Battle Dev
# Group composed of :
#    - Kevin PEETERS
#    - Gregory MOU KUI
import requests
import json

def formatJson(jsonResponse):
    json = {}
    for indexSensor, sensor in enumerate(jsonResponse):
        sensorData = {}
        for indexData, data in enumerate(sensor):
            sensorData[indexData] = data
        json[indexSensor] = sensorData
    return json

if __name__ == "__main__":
    response = requests.get("http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    json = formatJson(response.json())
    print(json)

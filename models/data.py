# from tools import getBitFromByte


class Data:

    def __init__(self, tagInformations):

        idSensorStart = 0
        idSensorLength = 8
        idSensorEnd = idSensorStart + idSensorLength

        statusStart = idSensorEnd + 1
        statusLength = 2
        statusEnd = statusStart + statusLength

        batteryVoltageStart = statusEnd + 1
        batteryVoltageLength = 4
        batteryVoltageEnd = batteryVoltageStart + batteryVoltageLength

        temperatureStart = batteryVoltageEnd + 1
        temperatureLength = 4
        temperatureEnd = temperatureStart + temperatureLength

        humidityStart = temperatureEnd + 1
        humidityLength = 4
        humidityEnd = humidityStart + humidityLength

        rssiStart = humidityEnd + 1
        rssiLength = 4
        rssiEnd = rssiStart + rssiLength

        print(tagInformations)
        print(len(tagInformations))
        print(idSensorLength + statusLength + batteryVoltageLength + temperatureLength + humidityLength + rssiLength)

        # Sensor ID
        self.idSensor = tagInformations[idSensorStart:idSensorEnd]
        print("Sensor ID = ", self.idSensor)

        # Battery status
        print("Battery status = ", tagInformations[statusStart:statusEnd])
        # byte = tagInformations[statusStart:statusEnd]
        # bit = getBitFromByte(byte, 7)
        # self.batteryVoltageStatus = bit
        # print("Battery status = ", self.batteryVoltageStatus)

        # Battery voltage
        print("Battery voltage = ", tagInformations[batteryVoltageStart:batteryVoltageEnd])

        # Temperature
        print("Temperature = ", tagInformations[temperatureStart:temperatureEnd])

        # Humidity
        print("Humidity = ", tagInformations[humidityStart:humidityEnd])

        # RSSI
        print("RSSI = ", tagInformations[rssiStart:rssiEnd])

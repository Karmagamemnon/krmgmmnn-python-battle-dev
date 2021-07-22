from tools import getBitFromByte


class Data:

    def __init__(self, tagInformations):

        idSensorStart = 0
        idSensorLength = 8
        idSensorEnd = idSensorStart + idSensorLength

        statusStart = idSensorEnd
        statusLength = 2
        statusEnd = statusStart + statusLength

        batteryVoltageStart = statusEnd
        batteryVoltageLength = 4
        batteryVoltageEnd = batteryVoltageStart + batteryVoltageLength

        temperatureStart = batteryVoltageEnd
        temperatureLength = 4
        temperatureEnd = temperatureStart + temperatureLength

        humidityStart = temperatureEnd
        humidityLength = 2
        humidityEnd = humidityStart + humidityLength

        rssiStart = humidityEnd
        rssiLength = 2
        rssiEnd = rssiStart + rssiLength

        print(tagInformations)
        print(len(tagInformations))
        print(idSensorLength + statusLength + batteryVoltageLength + temperatureLength + humidityLength + rssiLength)

        # Sensor ID
        self.idSensor = tagInformations[idSensorStart:idSensorEnd]
        print("Sensor ID = " + self.idSensor + "mV")

        # Battery status
        print("Battery status = " + tagInformations[statusStart:statusEnd] + "mV")
        bytes = tagInformations[statusStart:statusEnd]
        bit = getBitFromByte(bytes, 7)
        self.batteryVoltageStatus = bit
        print("Battery status = " + self.batteryVoltageStatus + "mV")

        # Battery voltage
        print("Battery voltage = " + tagInformations[batteryVoltageStart:batteryVoltageEnd] + "mV")
        bytes = tagInformations[batteryVoltageStart:batteryVoltageEnd]
        self.batteryVoltage = int(bytes, 16)
        print("Battery voltage = " + self.batteryVoltage + "mV")

        # Temperature
        print("Temperature =" + tagInformations[temperatureStart:temperatureEnd] + "mV")

        # Humidity
        print("Humidity = " + tagInformations[humidityStart:humidityEnd] + "mV")

        # RSSI
        print("RSSI = " + tagInformations[rssiStart:rssiEnd] + "mV")

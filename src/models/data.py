from utils.tools import getBitFromByte

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

        if(len(tagInformations) == idSensorLength + statusLength + batteryVoltageLength + temperatureLength + humidityLength + rssiLength):

            # Sensor ID
            self.idSensor = tagInformations[idSensorStart:idSensorEnd]
            print(f"Sensor ID = {str(self.idSensor)}")

            # Battery status
            bytes = tagInformations[statusStart:statusEnd]
            bit = getBitFromByte(bytes, 7)
            self.batteryVoltageStatus = bit
            print(f"Battery status = {str(self.batteryVoltageStatus)}")

            # Battery voltage
            bytes = tagInformations[batteryVoltageStart:batteryVoltageEnd]
            self.batteryVoltage = int(bytes, 16)
            print(f"Battery voltage = {str(self.batteryVoltage)}mV")

            # Temperature
            bytes = tagInformations[temperatureStart:temperatureEnd]
            isAbnormal = getBitFromByte(bytes, 15) == 1
            isNegative = getBitFromByte(bytes, 14) == 1
            temperature = int(bytes, 16) & 0b1111111111111
            self.temperature = (-1 if isNegative else 1) * (temperature / 10)
            print(f"Temperature = {str(self.temperature)}°C")

            # Humidity
            bytes = tagInformations[humidityStart:humidityEnd]
            humidity = None if bytes == "FF" else int(bytes, 16)
            self.humidity = humidity
            if (self.humidity != None):
                print(f"Humidity = {str(self.humidity)}%")

            # RSSI
            bytes = tagInformations[rssiStart:rssiEnd]
            self.rssi = int(bytes, 16)
            print(f"RSSI = -{str(self.rssi)}dBm")

    def getInsertQuery(self):
        return (
            "INSERT INTO data (id_sensor, battery_voltage_status, temperature, humidity, rssi) " +
            f"VALUES ({self.idSensor}, {self.batteryVoltageStatus}, {self.temperature}, {self.humidity}, {self.rssi});"
        )

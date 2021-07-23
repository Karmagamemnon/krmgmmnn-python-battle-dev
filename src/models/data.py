from __future__ import annotations
from datetime import datetime
from utils.db import count, executeSelect
from utils.tools import getBitFromByte


class Data:

    def __init__(self, tagInformations=None, timestamp: datetime = None, temperature: float = None,
                 humidity: int = None,
                 rssi: int = None, battery_voltage_status: int = None, id_sensor: int = None, name_sensor: str = None):
        if (tagInformations != None and timestamp != None):
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

            if (len(tagInformations) == idSensorLength + statusLength + batteryVoltageLength + temperatureLength + humidityLength + rssiLength):

                # Sensor ID
                self.idSensor = tagInformations[idSensorStart:idSensorEnd]
                print(f"Sensor ID = {str(self.idSensor)}")

                # Timestamp
                self.timestamp = timestamp
                print(f"Timestamp = {self.timestamp}")

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
                self.temperature = (-1 if isNegative else 1) * \
                    (temperature / 10)
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

        elif (timestamp != None and temperature != None and rssi != None and battery_voltage_status != None and id_sensor != None):
            self.temperature = temperature
            self.humidity = humidity
            self.rssi = rssi
            self.batteryVoltageStatus = battery_voltage_status
            self.timestamp = timestamp
            self.idSensor = id_sensor
            self.nameSensor = name_sensor

    def doesDataExist(self) -> bool:
        query = f"SELECT COUNT(1) FROM data WHERE id = {self.id}"
        exists = count(query) > 0
        return exists

    def getInsertQuery(self) -> str:
        humidity = "NULL" if self.humidity == None else self.humidity
        return (
            "INSERT INTO data (id_sensor, timestamp, battery_voltage_status, temperature, humidity, rssi) " +
            f"VALUES ({self.idSensor}, '{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}', {self.batteryVoltageStatus}, {self.temperature}, {humidity}, {self.rssi});"
        )

    def getMostRecentDataForEachSensor() -> list[Data]:
        from models.sensor import Sensor
        query = "SELECT `data1`.`timestamp`, `data1`.`temperature`, `data1`.`humidity`, `data1`.`rssi`, `data1`.`battery_voltage_status`, `data1`.`id_sensor` FROM `data` as data1 JOIN (SELECT * FROM `data` as data2 GROUP BY `data2`.`timestamp` ORDER BY `data2`.`timestamp` DESC) as data3 ON `data3`.`id` = `data1`.`id` GROUP BY `data1`.`id_sensor`"
        result = executeSelect(query)
        listData = []
        for row in result:
            sensorName = Sensor.getSensorNameById(row[5])
            data = Data(None, row[0], row[1], row[2], row[3], row[4], row[5], sensorName)
            listData.append(data)
        return listData

    def serialize(self):
        return {
            "temperature": float(self.temperature),
            "humidity": self.humidity,
            "rssi": self.rssi,
            "battery_voltage_status": self.battery_voltage_status,
            "timestamp": self.timestamp,
            "id_sensor": self.id_sensor,
        }

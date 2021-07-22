from datetime import datetime
from models.sensor import Sensor
from models.data import Data


class Sample:

    startSymbol = "545A"
    stopSymbol = "0D0A"
    startTagIndex = 86

    def __init__(self, sampleData):
        self.id = sampleData[0]
        self.rawdata = sampleData[1]
        self.timestamp = datetime.strptime(
            sampleData[2], '%a, %d %b %Y %H:%M:%S GMT')

    def areRawdataValid(self):
        lenght = len(self.rawdata)
        if (lenght < 98):
            print("There is a problem with rawdata")
            return False
        if (self.rawdata[0:4] != self.startSymbol):
            print("There is a problem with rawdata")
            return False
        if (self.rawdata[lenght-4:lenght] != self.stopSymbol):
            print("There is a problem with rawdata")
            return False
        return True

    def decryptRawdata(self):
        dataset = []

        if(self.areRawdataValid() == True):
            numberOfTags = int(self.rawdata[82:84], 16)
            tagLength = int(self.rawdata[84:86], 16) * 2

            for i in range(0, numberOfTags):
                start = self.startTagIndex + (i * tagLength)
                end = start + tagLength
                tagInformations = self.rawdata[start:end]

                data = Data(tagInformations)
                print("Sensor ID = ", data.idSensor)

                dataset.append(data)

        return dataset

from datetime import datetime
from models.data import Data
from utils.db import count


class Sample:

    startSymbol: str = "545A"
    stopSymbol: str = "0D0A"
    startTagIndex: int = 86

    def __init__(self, sampleData):
        self.id = sampleData[0]
        self.rawdata = sampleData[1]
        self.timestamp = datetime.strptime(
            sampleData[2], '%a, %d %b %Y %H:%M:%S GMT')

    def areRawdataValid(self) -> bool:
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

    def getDataset(self) -> list[Data]:
        dataset = []

        if(self.areRawdataValid() == True):
            numberOfTags = int(self.rawdata[82:84], 16)
            tagLength = int(self.rawdata[84:86], 16) * 2

            for i in range(0, numberOfTags):
                start = self.startTagIndex + (i * tagLength)
                end = start + tagLength
                tagInformations = self.rawdata[start:end]

                data = Data(tagInformations, self.timestamp)
                dataset.append(data)

        return dataset

    def doesSampleExist(self) -> bool:
        query = f"SELECT COUNT(1) FROM sample WHERE id = {self.id}"
        exists = count(query) > 0
        return exists

    def getInsertQuery(self) -> str:
        return (
            "INSERT INTO sample (id, rawdata, timestamp) " +
            f"VALUES ({self.id}, '{self.rawdata}', '{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}');"
        )

from datetime import datetime

class Sample:
    "description de merde"
    def __init__(self, sampleData):
        self.id = sampleData[0]
        self.rawdata = sampleData[1]
        self.timestamp = datetime.strptime(sampleData[2], '%a, %d %b %Y %H:%M:%S GMT')
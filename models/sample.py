from datetime import datetime
#from sensor import Sensor

class Sample:
    def __init__(self, sampleData):
        self.id = sampleData[0]
        self.rawdata = sampleData[1]
        self.timestamp = datetime.strptime(sampleData[2], '%a, %d %b %Y %H:%M:%S GMT')

    def decryptRawdata(self):
        if(self.rawdata[0:4] == "545A"):
            rawdataLength = len(self.rawdata)
            if(rawdataLength >= 98):
                if (self.rawdata[rawdataLength-4:rawdataLength] == "0D0A"):
                    numberOfTag = int(self.rawdata[82:84], 16)
                    lengthOfTag = int(self.rawdata[84:86], 16) * 2
                    startTagIndex = 86

                    for i in range(0, numberOfTag):
                        endTagIndex = startTagIndex+lengthOfTag

                        #Get sensor id
                        sensorIdOffset = startTagIndex + 8
                        print("sensor id :", self.rawdata[startTagIndex:sensorIdOffset])

                        #

                        startTagIndex = startTagIndex + lengthOfTag
                else:
                    print("There is a problem with rawdata")
            else:
                print("There is a problem with rawdata")
        else:
            print("There is a problem with rawdata")
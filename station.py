#Imad MAROUF

import csv
class station():
    name, LineID, LineName = "", "", ""
    def __init__(self, name, LineID, LineName):
        """Constructor of station object"""
        self.name = name
        self.LineID = LineID
        self.LineName = LineName

    def getName(self):
        """Print the name of the station"""
        return self.name

    def getLineID(self):
        """Print the ID of the metro line"""
        return self.LineID

    def getLineName(self):
        """Print the name of the metro line"""
        return self.LineName

    def toString(self):
        """Print string """
        string = "Connected to: " +self.name+" far about: "+self.time
        return string

with open('s.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    dic_stations = {}
    #Row : Name, ID, LineID, String, LineName
    for row in csv_reader:
        element = station(row[0], row[2], row[4])
        dic_stations[row[1]] = element

print(dic_stations["1755"].getName())
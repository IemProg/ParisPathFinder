#Imad MAROUF

import csv
class Connections():
    idOut, time  = "", 0

    def __init__(self, idOut, time):
        """Constructor of connection object station1 ID1 is related to idOut, time between them time"""
        self.idOut = idOut
        self.time = time

    def getIDStation(self):
        """Print the related station"""
        return self.idOut

    def getTime(self):
        """Print the time to get to the station2 idOut"""
        return self.time

    # def getAllConnections(self):
    #     return self.dict_connections

    def toString(self):
        string = "Connected to: " + self.idOut +" far about: "+ self.time
        return string

with open('c.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    dict_connections = {}
    #Row : ID1, ID2, Time
    for row in csv_reader:
        connection = Connections(row[1], row[2])
        if row[0] in dict_connections.keys():
            dict_connections[row[0]].append(connection)
        else:
            dict_connections[row[0]] = [connection]

# print("Connections: ", dict_connections["1629"][0].toString())
# print("Connections: ", dict_connections["1629"][1].toString())
# print("Connections: ", dict_connections["1629"][2].toString())
# print("Connections: ", dict_connections["1629"][3].toString())
#
# for v in dict_connections:
#     print(dict_connections[v].toString)
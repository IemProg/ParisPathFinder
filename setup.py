from collections import defaultdict, deque
import connections
import station
import csv

#Creating stations objects
with open('s.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    dic_stations = {}
    #Row : Name, ID, LineID, String, LineName
    for row in csv_reader:
        element = station.station(row[0], row[2], row[4])
        dic_stations[row[1]] = element

#Establishing the connections between adresses
with open('c.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    nodes = []
    dict_connections = {}

    #Row : ID1, ID2, Time
    for row in csv_reader:
        nodes.append(row[0])
        connection = connections.Connections(row[1], row[2])

        if row[0] in dict_connections.keys():
            dict_connections[row[0]].append(connection)
        else:
            dict_connections[row[0]] = [connection]

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

graph = Graph()

#Adding Nodes to the Graph
for node in nodes:
    graph.add_node(node)

#Adding edge to the Graph
for key in dict_connections.keys():
    for element in dict_connections[key]:
        #print("ID: "+key+" element: "+ element.getIDStation() + " Time " + element.getTime())
        graph.add_edge(key, element.getIDStation(), int(element.getTime()))


# #print(shortest_path(graph, '1722', '2062'))
# output = shortest_path(graph, '1722', '2062')  1722 2062
# print(output)
# output2 = []
#
# for element in output[1]:
#     output2.append(dic_stations[element].getName())
#
# print(output2)
import math
from queue import PriorityQueue

class Map:

    tileList = list()

    def __init__(self, initWidth, initHeight):
        self.width = initWidth
        self.height = initHeight
        self.animateList = {}
        self.inanimateList = {}

        for i in range (0, initHeight):
            for j in range (0, initWidth):
                newTile = self.MapTile((j, i))
                self.tileList.append(newTile);

    def objectInAnimateList(self, testX, testY):
        for i in self.animateList:
            if self.animateList.get((testX, testY)) != None:
                return True

    def objectInInanimateList(self, testX, testY):
        for i in self.inanimateList:
            if self.inanimateList.get((testX, testY)) != None:
                return True

    def printMap(self):
        row = ""
        for i in range (0, self.height):
            for j in range (0, self.width):
                row += '|'
                animateLocation = self.objectInAnimateList(j, i)
                inanimateLocation = self.objectInInanimateList(j, i)
                if animateLocation != None:
                    row += self.animateList[j, i]
                elif (inanimateLocation != None) :
                    row += self.inanimateList[j, i]
                else:
                    row += ' '
            row += '|'
            print(row)
            row = ""

    def dijkstras(self, source):
        adjacencyMatrix = {}
        for i in range (0, self.height):
            for j in range (0, self.width):
                adjacencyMatrix[(j, i)] = list()
        for i in adjacencyMatrix:
            adjacencyMatrix[i].append((i[0] - 1, i[1] - 1))
            adjacencyMatrix[i].append((i[0] + 1, i[1] + 1))
            adjacencyMatrix[i].append((i[0] - 1, i[1] + 1))
            adjacencyMatrix[i].append((i[0] + 1, i[1] - 1))
            adjacencyMatrix[i].append((i[0] - 1, i[1]))
            adjacencyMatrix[i].append((i[0], i[1] - 1))
            adjacencyMatrix[i].append((i[0] + 1, i[1]))
            adjacencyMatrix[i].append((i[0], i[1] + 1))

            if i[0] == 0:
                if adjacencyMatrix[i].count((i[0] - 1, i[1])) != 0:
                    adjacencyMatrix[i].remove((i[0] - 1, i[1]))
                if adjacencyMatrix[i].count((i[0] - 1, i[1] + 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] - 1, i[1] + 1))
                if adjacencyMatrix[i].count((i[0] - 1, i[1] - 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] - 1, i[1] - 1))
            elif i[0] == self.width - 1:
                if adjacencyMatrix[i].count((i[0] + 1, i[1])) != 0:
                    adjacencyMatrix[i].remove((i[0] + 1, i[1]))
                if adjacencyMatrix[i].count((i[0] + 1, i[1] + 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] + 1, i[1] + 1))
                if adjacencyMatrix[i].count((i[0] + 1, i[1] - 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] + 1, i[1] - 1))
            if i[1] == 0:
                if adjacencyMatrix[i].count((i[0], i[1] - 1)) != 0:
                    adjacencyMatrix[i].remove((i[0], i[1] - 1))
                if adjacencyMatrix[i].count((i[0] - 1, i[1] - 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] - 1, i[1] - 1))
                if adjacencyMatrix[i].count((i[0] + 1, i[1] - 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] + 1, i[1] - 1))
            elif i[1] == self.height - 1:
                if adjacencyMatrix[i].count((i[0], i[1] + 1)) != 0:
                    adjacencyMatrix[i].remove((i[0], i[1] + 1))
                if adjacencyMatrix[i].count((i[0] - 1, i[1] + 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] - 1, i[1] + 1))
                if adjacencyMatrix[i].count((i[0] + 1, i[1] + 1)) != 0:
                    adjacencyMatrix[i].remove((i[0] + 1, i[1] + 1))

        parent = {}
        parent[source] = (-1, -1)

        distances = {}
        for i in self.tileList:
            distances[i.coordinates] = math.inf
        distances[source] = 0

        pq = PriorityQueue()
        pq.put((0, source))
        while not pq.empty():
            u = pq.get()[1]
            for i in range (0, len(adjacencyMatrix[u])):
                v = adjacencyMatrix[u][i]
                addedDistance = 0
                if distances[v] > distances[u] + 5:
                    distances[v] = distances[u] + 5
                    parent[v] = u
                    pq.put((distances[v], v))



        return (distances, parent)

    def findPath(self, parentList, target):
        path = list()
        path.append(target)
        parent = parentList[target]
        while parent[0] != -1:
            path.append(parent)
            parent = parentList[parent]
        path.reverse()
        return path

    class MapTile:
        def __init__(self, initCoordinates):
            self.coordinates = initCoordinates




testMap = Map(250, 250)
testMap.animateList[1, 0] = 'A'
testMap.inanimateList[2, 3] = '#'
testMap.printMap()
paths = testMap.dijkstras((1, 2))
print(testMap.findPath((paths[1]), (12, 15)))
print(paths[0][(12, 15)])

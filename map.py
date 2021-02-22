import math
from queue import PriorityQueue


class Map:
    tileList = list()

    def __init__(self, initWidth, initHeight, anim=None, inanim=None):
        self.width = initWidth
        self.height = initHeight
        if anim is None:
            self.animateList = list()
        else:
            self.animateList = anim
        if inanim is None:
            self.inanimateList = list()
        else:
            self.inanimateList = inanim

        for i in range(0, initHeight):
            for j in range(0, initWidth):
                newTile = self.MapTile(init_coors=(i, j))
                self.tileList.append(newTile);

    def object_found(self, testX, testY, animate=True):
        if animate:
            for i in self.animateList:
                if self.animateList.get((testX, testY)) != None:
                    return True
        else:
            for i in self.inanimateList:
                if self.inanimateList.get((testX, testY)) != None:
                    return True

    def printMap(self):
        row = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                row += '|'
                animateLocation = self.object_found(j, i)
                inanimateLocation = self.object_found(j, i, animate=False)
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
        def __init__(self, init_coors=(0, 0), icon="./assets/grasstile.png"):
            self.coordinates = init_coors
            self.icon = icon


# ====================================
# Run
# ====================================
# testMap = Map(15, 15)
# testMap.animateList[1, 0] = 'A'
# testMap.inanimateList[2, 3] = '#'
# testMap.inanimateList[4, 7] = '%'
# testMap.printMap()
# paths = testMap.dijkstras((1, 2))
# print(testMap.findPath((paths[1]), (13, 13)))
# print(paths[0][(13, 13)])

import math
from queue import PriorityQueue
from inanimate import Inanimate
from animate import Animate


class Map:
    tileList = list()

    def __init__(self, initWidth, initHeight, anim=None, inanim=None):
        self.width = initWidth
        self.height = initHeight

        if anim is None:
            anim = list()
        if inanim is None:
            inanim = list()

        self.entities = anim + inanim

        for i in range(0, initHeight):
            for j in range(0, initWidth):
                newTile = self.MapTile(init_coors=(i, j))
                self.tileList.append(newTile)

    def object_found(self, testX, testY, testZ=0):
        for ent in self.entities:
            if ent.get_coors() == [testX, testY, testZ]:
                if type(ent) != Inanimate or ent.get_is_prop():
                    return [True, ent]

        return [False, 0]

    def get_tile_list(self):
        return self.tileList

    def load_map(self, tiles):
        self.tileList = tiles

    # def printMap(self):
    #     row = ""
    #     for i in range(0, self.height):
    #         for j in range(0, self.width):
    #             row += '|'
    #             result = self.object_found(testX=j, testY=i)
    #             if result[0]:
    #                 row += result[1].get_name()[0]
    #             else:
    #                 row += ' '
    #         row += '|'
    #         print(row)
    #         row = ""

    def dijkstras(self, source):
        adjacencyMatrix = {}
        for i in range(0, self.height):
            for j in range(0, self.width):
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

            if self.object_found(i[0] - 1, i[1] - 1)[0] or self.object_found(i[0] - 1, i[1] - 1)[0]:
                adjacencyMatrix[i].remove((i[0] - 1, i[1] - 1))
            if self.object_found(i[0] + 1, i[1] + 1)[0] or self.object_found(i[0] + 1, i[1] + 1)[0]:
                adjacencyMatrix[i].remove((i[0] + 1, i[1] + 1))
            if self.object_found(i[0] - 1, i[1] + 1)[0] or self.object_found(i[0] - 1, i[1] + 1)[0]:
                adjacencyMatrix[i].remove((i[0] - 1, i[1] + 1))
            if self.object_found(i[0] + 1, i[1] - 1)[0] or self.object_found(i[0] + 1, i[1] - 1)[0]:
                adjacencyMatrix[i].remove((i[0] + 1, i[1] - 1))
            if self.object_found(i[0] - 1, i[1])[0] or self.object_found(i[0] - 1, i[1])[0]:
                adjacencyMatrix[i].remove((i[0] - 1, i[1]))
            if self.object_found(i[0], i[1] - 1)[0] or self.object_found(i[0], i[1] - 1)[0]:
                adjacencyMatrix[i].remove((i[0], i[1] - 1))
            if self.object_found(i[0] + 1, i[1])[0] or self.object_found(i[0] + 1, i[1])[0]:
                adjacencyMatrix[i].remove((i[0] + 1, i[1]))
            if self.object_found(i[0], i[1] + 1)[0] or self.object_found(i[0], i[1] + 1)[0]:
                adjacencyMatrix[i].remove((i[0], i[1] + 1))

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

    # def findPath(self, parentList, target):
    #     path = list()
    #     path.append(target)
    #     parent = parentList[target]
    #     while parent[0] != -1:
    #         path.append(parent)
    #         parent = parentList[parent]
    #     path.reverse()
    #     return path

    class MapTile:
        def __init__(self, init_coors=(0, 0)):
            self.coordinates = init_coors


# ====================================
# Run
# ====================================
# coors = (3, 0)
# destination = (5, 1)
#
# anims = [Animate("Harold")]
# anims[0].set_coors(x=coors[0], y=coors[1])
#
# inanims = [Inanimate("Boulder", item_code=0)]
# inanims[0].set_coors(x=1, y=1)
#
# testMap = Map(15, 15, anim=anims, inanim=inanims)
#
# testMap.printMap()
# paths = testMap.dijkstras(coors)
# print(testMap.findPath((paths[1]), destination))
# print(paths[0][destination])

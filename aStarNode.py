#This is the A star node for each town. 
#It is different from the regular nodes used in BFS & DFS

class Node:
    def __init__(self, value):
        self.f = 0
        self.g = 0
        self.h = 0
        self.cummulativeG = 0
        self.value = value
        self.edges = []
        self.searched = False
        self.parent = None

    def setF(self, val):
        self.f = val
        return self.f

    def setG(self, val):
        self.g = val
        return self.g

    def setCummulativeG(self, g):
        if self.parent == None:
            self.cummulativeG += g

        self.cummulativeG = g + self.parent.g
        return self.cummulativeG

    def setH(self, val):
        self.h = val
        return self.h

    def addEdge(self, road):
        self.edges.append(road)
        #print(self.value, road)

    def getEdgeDistance(self, town):
        towns = self.edges
        for t in towns:
            if town in t.keys():
                return t[town]


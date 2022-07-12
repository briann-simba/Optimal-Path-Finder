# Defines the node objects

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.searched = False
        self.parent = None

    def addEdge(self, road_to):
        self.edges.append(road_to)
        #print(self.value, road)

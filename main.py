import json
import node as node
import graph as Graph
import aStarNode as A_S_Node
import priorityQueue as P_Queue
import random

#Town display locations
def townDisplay(town, parent):
    towns = [ 
        ("Kisumu", False, None),
        ("Nakuru", False, None),
        ("Nairobi", False, None),
        ("Thika", False, None),
        ("Mombasa", False, None),
        ("Eldoret", False, None),
        ("Isiolo", False, None),
        ("Garissa", False, None),
        ("Kitui", False, None),
        ("Malindi", False, None)    
    ]
    for i in range(len(towns)):
        if towns[i][0] != town:
            pass
        else:
            if parent == None:
                towns[i] = (towns[i][0], True, None)
            else: 
               towns[i] = (towns[i][0], True, parent)

    return towns

#Import the town data
dataFile = open('towns.json')
data = json.load(dataFile)
dataFile.close()

towns = data["towns"]
straight_line_distances = data["straight_line_distances"]

def getSLD(target, goal): #function to read the straight line distance.
    keys = []
    index = None
    for elem in straight_line_distances:
        keys.append(elem)

    for key in keys:
        if target in key and goal in key:
            index = key

    return straight_line_distances[index]

def create_graph(graph):
    for i in range(len(towns)):
        town = towns[i]["name"]
        roads_to = towns[i]["roads_to"]
        n = node.Node(town)
        
        for j in range(len(roads_to)):
            road = roads_to[j]
            n.addEdge(road)
            # print(road)

        graph.addNode(n)
        # print(graph.nodes)
    

def create_a_star_graph(graph):
    for i in range(len(towns)):
        town = towns[i]["name"]
        roads_to = towns[i]["roads_to"]
        n = A_S_Node.Node(town)
        
        for j in range(len(roads_to)):
            road = roads_to[j]
            n.addEdge(road)
            # print(road)

        graph.addNode(n)

def BreadthFirst(start, end):
    #Create Graph object
    graph_bfs = Graph.Graph()
    #Add nodes to graph
    create_graph(graph_bfs)


    if start not in graph_bfs.nodeNames or end not in graph_bfs.nodeNames:
        print("Unknown Town")
        return 0
    start = graph_bfs.setStart(start)
    end = graph_bfs.setEnd(end)

    queue = []
    attempts = [] #an array of how the towns were tested

    start.searched = True
    queue.append(start)

    while len(queue) > 0:
        current = queue.pop(0)

        #update the attempts and the path.
        if current.parent == None:
            attempts.append(townDisplay(current.value, None))
        else: 
            attempts.append(townDisplay(current.value, current.parent.value))
        
        if current == end:
            # print("Found Target:", current.value)
            break

        edges = current.edges
        for edge in edges:
            neighbour = graph_bfs.getNode(list(edge.keys())[0])

            if not neighbour.searched:
                neighbour.searched = True
                neighbour.parent = current
                queue.append(neighbour)

    path = []
    path.append(end)
    nextNode = end.parent
    while nextNode != None:
        path.append(nextNode)
        nextNode = nextNode.parent

    txt = ""

    for i in range(len(path))[::-1]:
        n = path[i]
        txt += n.value 
        if i != 0:
            txt += " --> "
    
    print("Path using BFS: ", txt)
    # print("BFS attempts: ", attempts)
    return attempts, txt

def DepthFirst(start, end):
    graph_dfs = Graph.Graph()
    create_graph(graph_dfs)
    
    if start not in graph_dfs.nodeNames or end not in graph_dfs.nodeNames:
        print("Unknown Town")
        return 0
    start = graph_dfs.setStart(start)
    end = graph_dfs.setEnd(end)

    attempts = []
    stack = [] #stack.pop()
    start.searched = True
    stack.append(start)

    while len(stack) > 0:
        current = stack.pop()
        
        #update the attempts and the path.
        if current.parent == None:
            attempts.append(townDisplay(current.value, None))
        else: 
            attempts.append(townDisplay(current.value, current.parent.value))

        # print("Checking: ", current.value)
        if current == end:
            # print("Found Tagret: ", current.value)
            break
        edges = current.edges
        for edge in edges:
            neighbour = graph_dfs.getNode(list(edge.keys())[0])
            # print("Neighbour: ", neighbour.value)
            if not neighbour.searched:
                neighbour.searched = True
                neighbour.parent = current
                stack.append(neighbour)
                # for i in stack:
                #     print(i.value)

    path = []
    path.append(end)
    nextNode = end.parent
    while nextNode != None:
        path.append(nextNode)
        nextNode = nextNode.parent
    
    txt = ""
    for i in range(len(path))[::-1]:
        n = path[i]
        txt += n.value
        if i != 0:
            txt += " --> "
    
    # print("DFS Attempts: ", attempts)
    print("Path using DFS ::", txt)
    return attempts, txt

def aStar(start, end):
    #using straight line distance (Euclidean Distance) as a heuristic.
    #list of straight line distances is in the variable straight line distances in towns.json
    
    graph = Graph.Graph()
    create_a_star_graph(graph)

    if start not in graph.nodeNames or end not in graph.nodeNames:
        print("Unknown Town")
        return 0

    start = graph.setStart(start)
    end = graph.setEnd(end)

    #We get the straight line distances of all nodes in the graph to the goal node
    #This is the h() value
    #The g() value is the distance from the current node to one if it's neighbours
    #note that f() = g() + h()

    #the lower the f value, the higher up on the priority queue. It will be removed first
    open_list = P_Queue.PriorityQueue() 
    start.setG(0)
    start.setH(getSLD(start.value, end.value))
    start.searched = True
    open_list.addElem((start.setF(start.g + start.h), start)) #at the beginning, the g value is 0.
    closed_list = [] #holds the names of the towns

    attempts = [] #array to hold how all paths were tried. 

    #open_list elements are a 2-tuple of the form (f(), NodeObject)

    while len(open_list.queue) != 0: 
        closed_list.append(open_list.queue[0][1].value)
        # print(open_list.queue[0][1].value , {"f: ": open_list.queue[0][1].f , "g: ": open_list.queue[0][1].g, "h: ": open_list.queue[0][1].h} )
        current = open_list.pop()[1]
        
        #update the attempts sequence
        if current.parent == None:
            attempts.append(townDisplay(current.value, None))
        else: 
            attempts.append(townDisplay(current.value, current.parent.value))

        if current.value == end.value:
            # print("Found Target:", current.value)
            break

        edges = current.edges
        for edge in edges:
            neighbour = graph.getNode(list(edge.keys())[0]) #get the neighbour node at the end of this edge
            
            if not neighbour.searched:
                neighbour.searched = True
                neighbour.parent = current
                h = getSLD(neighbour.value, end.value )
                g = neighbour.setCummulativeG(current.getEdgeDistance(neighbour.value))
                f = h+g
                neighbour.setF(f)
                neighbour.setG(g)
                neighbour.setH(h)
                
                neighbour.current = current.value
                neighbour.parent = current
                open_list.addElem((neighbour.f ,neighbour))
                #print(open_list.queue[0][1].value, open_list.queue[0][0] )

    path = []
    path.append(end)
    nextNode = end.parent
    while nextNode != None:
        path.append(nextNode)
        nextNode = nextNode.parent
    
    txt = ""
    for i in range(len(path))[::-1]:
        n = path[i]
        txt += n.value
        if i != 0:
            txt += " --> "
            
    print("Path using AStar :: " ,txt)
    #print("A Start Attempts: ", attempts)
    return attempts, txt

def run (start, goal):
    BreadthFirst(start, goal)
    DepthFirst(start, goal)
    aStar(start, goal)

run("Kisumu", "Garissa")
#DFS not optimal on Isiolo -> Malindi
#BFS not optimal Kitui -> Eldoret

# bfs = aStar("Kisumu", "Thika")
# print(bfs)

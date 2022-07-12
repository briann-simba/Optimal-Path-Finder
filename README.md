# Search Algorithms to find a goal node. 

## Breadth First Search. 
This is an algorithm that checks all connected nodes and adds them to a queue. The order in which the nodes are searched are the order in which they are appended to the queue, that is, First in First Out. FIFO

## Depth First Search
This is an algorithm that checks all connected nodes and adds them to a stack. The order in which the nodes are searched are the order in which they are appended to the stack, that is, Last in First Out. LIFO

## A star Search
This is an algorithm similar to Djikstra's algorithm. It uses a heuristic to measure whether or not it is getting closer to the goal node. The node objects are stored in a priority queue with the node with the lowest f() value being popped first from the priority queue. In this implementation, the heuristic I used was the Euclidean distance.

# Implementation

## Classes Used

### Graph
This is the object that holds the nodes and the search is performed on this object

### Node
This object stores data about other towns connected to it, whether it has been searched, the name of the paret node (the node searched before it). It is used in the Depth First && Breadth First searches

### A star Node
Similar to the Node class, but it has the additional properties that it holds the f(), g(), and h() values required by the aStar algorithm

### Priority Queue
A simple python implementation of a priority queue. 

## Breakdown
The data about the towns is stored in a json file. This has the names of the towns, towns connected to that town and the straight line distances between all the towns. (All the towns are in Kenya)

The data is imported into the main function and used to build the graphs in the breadth first, depth first and a star functions. These functions take a start point and an end point and compute the optimal distance between them. 

The graph is visualised using pygame under map.py. 

# Depandancies
pygame

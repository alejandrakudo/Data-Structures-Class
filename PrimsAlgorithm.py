'''I confirm that this submission is my own work and is
consistent with the Queen's regulations on Academic Integrity'''

'''CISC 235
Assignment 4
Alejandra Kudo
10136014
'''

''' reading & opening text file -
filename = open('Test_Cases.txt', 'r')
message = filename.read()
print(message)
filename.close()
'''


import sys
from heap import Heap


def primsMSTAlgorithm(adjList):
    adjList[vertex1] = [(vertex21,weight1,edgeId1), (vertex22,weight2,edgeId2), ...]
return adjList


'''
Updates the heap with entries of all the vertices incident to vertex v that was recently explored
Args:
			
'''
def updateHeap(v):
	
    for vertex,weight,edgeID in adjList[v]:
        if vertex not in explored:
            element = unexplored.delete(vertex)
            if element and element[0] < weight:
                unexplored.insert(element)
            else:
                unexplored.insert((weight,vertex,edgeID))

    source = list(adjList.keys())[0]  
    unexplored, explored, mst = Heap(), set([source]), set()
    updateHeap(source)

    while unexplored.length():
        weight, vertex, edgeID = unexplored.extractMin()
	explored.append(vertex)
	mst.append(edgeID)
	updateHeap(vertex)
	
    return mst

## create graph by opening file Test_Cases.txt
## Using Adjacency Lists since more efficeitn for these algorithms 
def graph(filename):
    adjList, edgeList = {}, {}

    with open(filename, 'r') as f:
    numbers = f.readline().split()
    numVertices, numEdges = int(numbers[0]), int(numbers[1])
    edgeID = 1

    for line in f:
        edge = line.split()
	vertex1, vertex2, weight = int(edge[0]), int(edge[1]), int(edge[2])
			
	if vertex1 in adjList:
            adjList[vertex1].append((vertex2,weight,edgeID))
	else:
            adjList[vertex1] = [(vertex2,weight,edgeID)]
                if vertex2 in adjList:
                    adjList[vertex2].append((vertex1,weight,edgeID))
			else:
                            adjList[vertex2] = [(vertex1,weight,edgeID)]
			
			edgeList[edgeID] = (vertex1,vertex2,weight)
			
			edgeID += 1

	return adjList, edgeList

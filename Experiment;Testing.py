'''I confirm that this submission is my own work and is
consistent with the Queen's regulations on Academic Integrity'''

'''CISC 235
Assignment 4
Alejandra Kudo
10136014
'''


# reading & opening text file -
'''
filename = open('Test_Cases.txt', 'r')
message = filename.read()
print(message)
filename.close()
'''

''' For each test case - generate graph to represent test case
Use BFS to find spanning tree
Use prim to find spanning tree
Then calculates average - getting about 84-88%
'''
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



def breadthFirst(startingNode, soughtValue):
   visitedNodes = set()
   queue = deque([startingNode])

    while len(queue) > 0:
        node = queue.pop()
        if node in visitedNodes:
            continue
        
        visitedNodes.add(node)
        if node.value == soughtValue:
            return True

        for n in node.adjacentNodes:
            if n not in visitedNodes:
                queue.appendleft(n)
    return False 


def primsMSTAlgorithm(adjList):
    adjList[vertex1] = [(vertex21,weight1,edgeId1), (vertex22,weight2,edgeId2), ...]

return adjList


## computes the average of the values of Diff for each of
## the given graph sizes. Diff = (B/P-1)*100
def average(B,P):
    ## Diff is the percentage by which B is larger than P
    Diff = (B/P-1)*100
    return Diff


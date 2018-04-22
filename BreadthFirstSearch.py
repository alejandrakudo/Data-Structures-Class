'''I confirm that this submission is my own work and is
consistent with the Queen's regulations on Academic Integrity'''

'''CISC 235
Assignment 4
Alejandra Kudo
10136014
'''

'''reading & opening text file -
f = open('Test_Cases.txt', 'r')
message = f.read()
print(message)
f.close()
'''


class Node:
   def __init__(self, value):
      self.value = value
      self.adjacentNodes = []

# Graph for breadth first search 
def buildGraph(vertexNames, edges):
    vertices = dict([(vertexNames[i], Node(vertexNames[i])) for i in range(len(vertexNames))])

    for name in vertices:
        vertices[name].value = name

    for (v,w) in edges:
        vertices[v].adjacentNodes.append(vertices[w])

    return vertices[vertexNames[0]]


# Breadth First Search
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



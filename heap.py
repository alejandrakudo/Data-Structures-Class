'''I confirm that this submission is my own work and is
consistent with the Queen's regulations on Academic Integrity'''

'''CISC 235
Assignment 4
Alejandra Kudo
10136014
'''

''' reading & opening text file -
f = open('Test_Cases.txt', 'r')
message = f.read()
print(message)
f.close()
'''
## Using heap data structure for Prim's Algorithm 

class Heap:
    def __init__(self, element = None, batch = None):
        self.heap, self.heapIdx = [], {}
	if batch:
            self.heapify(batch)
	if element:
            self.insert(element)


    def length(self):
	return len(self.heap) 


    def insert(self, element):
        self.heap[self.length():] = [element]
	self.heapIdx[element[1]] = self.length() - 1
        self.__siftUp()


    def __siftUp(self):
        childIdx = self.length() - 1
	parentIdx = int((childIdx - 1) / 2)
	while self.heap[childIdx][0] < self.heap[parentIdx][0]:
            parent, child = self.heap[parentIdx], self.heap[childIdx]
            self.heap[parentIdx], self.heapIdx[child[1]] = child, parentIdx
            self.heap[childIdx], self.heapIdx[parent[1]] = parent, childIdx
            parentIdx, childIdx = int((parentIdx - 1) / 2), parentIdx

    def heapify(self, batch):
        for idx, element in enumerate(batch):  # populates the heap
            self.heap.append(element)
            self.heapIdx[element[1]] = idx
	for i in range(int(self.length() / 2) - 1, -1, -1):  # enforces the heap property
            self.__minHeapify(i)


    def __minHeapify(self, parentIdx):
        leftChildIdx, rightChildIdx = 2 * parentIdx + 1, 2 * parentIdx + 2
	lowest = leftChildIdx
	if leftChildIdx < self.length() and self.heap[leftChildIdx] < self.heap[parentIdx]:
	else:
            parentIdx
	if rightChildIdx < self.length() and self.heap[rightChildIdx] < self.heap[lowest]:
            lowest = rightChildIdx
	if lowest != parentIdx:
			parent, child = self.heap[parentIdx], self.heap[lowest]
			self.heap[parentIdx], self.heapIdx[child[1]] = child, parentIdx
			self.heap[lowest], self.heapIdx[parent[1]] = parent, lowest
			self.__minHeapify(lowest)


    def extractMin(self):
		minElm = self.heap[0]
		del self.heapIdx[minElm[1]]
		lastElm = self.heap.pop()
		if self.length():
			self.heap[0] = lastElm
			self.heapIdx[lastElm[1]] = 0
			self.__siftDown(0)
		return minElm

    def __siftDown(self, parentIdx):
        if 2 * parentIdx + 1 >= self.length():
            return  # if the parent doesn't have children, you are good to go!
	if 2 * parentIdx + 2 >= self.length():  # if the parent has one child...
			# and the child's key is less than the parent's key, it swaps the entries
	if self.heap[parentIdx][0] > self.heap[2 * parentIdx + 1][0]:
            parent, child = self.heap[parentIdx], self.heap[2 * parentIdx + 1]
	    self.heap[parentIdx], self.heapIdx[child[1]] = child, parentIdx
	    self.heap[2 * parentIdx + 1], self.heapIdx[parent[1]] = parent, 2 * parentIdx + 1
	    return

	    parent = self.heap[parentIdx]
            leftChild, rightChild = self.heap[2 * parentIdx + 1], self.heap[2 * parentIdx + 2]
	    minLeft = False
            if leftChild[0] <= rightChild[0]:
                minLeft = True
	    if parent[0] > min(leftChild[0], rightChild[0]):
                self.heap[parentIdx] = leftChild if minLeft
                else rightChild
		self.heapIdx[leftChild[1] if minLeft else rightChild[1]] = parentIdx
			self.heap[2 * parentIdx + 1 if minLeft else 2 * parentIdx + 2] = parent
			self.heapIdx[parent[1]] = 2 * parentIdx + 1 if minLeft else 2 * parentIdx + 2
			self.__siftDown(2 * parentIdx + 1 + (not minLeft))


    def get(self, id):
        if id in self.heapIdx:
            return self.heap[self.heapIdx[id]]
        else:
            None
        return 
        
    

    def delete(self, id):
		'''
		Deletes an object from the heap, and returns that object
		Args:
			id: identifier of the object to be handled
		'''
		if id not in self.heapIdx:
                    return None
		idx = self.heapIdx[id]
		del self.heapIdx[id]
		element = self.heap[idx]
		lastElm = self.heap.pop()
		if idx != self.length():
			self.heap[idx] = lastElm
			self.heapIdx[lastElm[1]] = idx
			self.__siftDown(idx)
		return element

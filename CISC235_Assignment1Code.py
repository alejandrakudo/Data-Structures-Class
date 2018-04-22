'''I confirm that this submission is my own work and is consistent with the
Queen's regulations on Academic Integrity'''

import random, timeit

# CISC 235: Assignment 1
# Name: Alejandra Kudo
# Student Number: 10136014
# Net ID: 13aak15

'''Algorithm MA - Store S in an array, in whatever order it
happens in & searches. Algorithm runs in O(k*n) time'''

def linearSearch(x,S):
    found = False
    position = 0
    while position < len(S) and not found:
        if S[position] == x:
            found = True
           # print("Yes")
            return 
        position = position + 1
    #print("No")
    return found

def getAverage_linearSearch(x,S):
    sum_time = 0 
    for i in range (1,500):
        start = timeit.default_timer()
        linearSearch(x,S)
        end = timeit.default_timer()
        sum_time = sum_time + (end-start)
        
    average_sum_time = sum_time/500
    print("Linear Search Time: ", average_sum_time)
    return average_sum_time
    

'''Algorithm MB - Store S in an array or indexed list using
O(n log n) sort - in this case Quick Sort '''
    
def quicksort(alist):
    if len(alist) == 1 or len(alist) == 0:
        return alist
    else:
        pivot = alist[0]
        i = 0
        for j in range(len(alist)-1):
            if alist[j+1] < pivot:
                alist[j+1],alist[i+1] = alist[i+1], alist[j+1]
                i += 1
        alist[0],alist[i] = alist[i],alist[0]
        first = quicksort(alist[:i])
        second = quicksort(alist[i+1:])
        first.append(alist[i])
        return first + second


# binary search function
def binarySearch(S, n):
    low = 0
    high = len(S)-1
    found =False
    while( low <= high and not found):
        mid = (low + high)//2
        if S[mid] == n:
            found = True
        else:
            if n < S[mid]:
                high = mid - 1
	    else:
                low = mid + 1	
    return found
 
# calculates the average time of a binary search in a sorted list
def average_binarySearch(S,n):
    sum_time = 0 
    for i in range (1,500):
        start = timeit.default_timer()
        binarySearch(S,n)
        end = timeit.default_timer()
        sum_time = sum_time + (end-start)
        
    average_sum_time = sum_time/500
    print("BinarySearch Time:",average_sum_time)
    return average_sum_time

# creates list using random to generate random integers
def create_list(n):
    S=[]
    for i in range(n):
        S.append(random.randint(0,1000))
    return S


''' Main function to print time of linear search & binary search 
def main():
    alist = create_list(1000)
    quicksort(alist)
    average_binarySearch(alist,1000)
    

main()

'''

'''This main function tests and prints average time
for linear search & binary search (Algorithm MA & MB)'''
##def main():
##    l = [1000, 2000, 4000, 8000, 16000]
##    for i in range(0,len(l)):
##        n = l[i]
##        k = 10
##        l = create_list(n)
##        avg_binarySearch = average_binarySearch(l,k)
##        avg_linearSearch = average_linearSearch(l,k)
##        while avg_binarySearch <= avg_linearSearch:
##            k=k+1
##            l = create_list()
##            avg_binarySearch = average_binarySearch(l,k)
##            avg_linearSearch = average_linearSearch(l,k)
##        print(avg_linearSearch)
##        print(avg_binarySearch)
##        print(k)


''' Test binarysearch 
def main():
    l = create_list(100)
    binarySearch(l,10)
main()

'''

''' Test quicksort 
def main():
    S = create_list(100)
    print(len(S))
    quicksort(S,0,99)
    a = average_binarySearch(S,100)
    print(a)
main()
'''


'''Test create_list
def main():
    l = create_list(100)
    print(l)
    
main()
 '''

#binarysearch function taking a really long time to run
#main function to test 
def main():
    #S = []
    #create_list(1000)
    alist = create_list(10)
    print(alist)

    
    x = 1
    linearSearch(x,alist)
    print("LINEAR OK")

    
    quicksort(alist,0,len(alist)-1)
    binarySearch(alist, x)
    print(alist)
    
main()




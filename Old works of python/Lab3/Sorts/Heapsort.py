
from copy import deepcopy

class Heap:

    def __init__(self,lst):
        self.lst=lst
        self.heap_length=len(lst)
        self.heap_size=len(lst)

    def __getitem__(self, key):

        return self.lst[key]

    def __setitem__(self, key, value):

        self.lst[key]=value

def parent(i):
    return i >> 1

def left(i):
    return i << 1

def right(i):
    return (i << 1) + 1

def max_heapify(heap, i,funct):

    l = left(i)
    r = right(i)
    if l < heap.heap_size and funct(heap[i] , heap[l])==True:
        largest = l
    else:
        largest = i
    if r < heap.heap_size and funct(heap[largest] , heap[r])==True:
        largest = r
    if not largest == i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, largest,funct)

def build_max_heap(heap,funct):

    heap.heap_size = heap.heap_length
    for i in range(heap.heap_length >> 1, 0, -1):
        max_heapify(heap, i,funct)

def heapsort(lst,key=None,reverse=False):
    global heap_size
    global heap_length

    heap=Heap(deepcopy(lst))

    funct=key
    # if reverse == True reverse the list by elementary algorithm

    build_max_heap(heap,funct)
    for i in range(heap.heap_length - 1, 1, -1):
        heap[1], heap[i] = heap[i], heap[1]
        heap.heap_size = heap.heap_size - 1
        max_heapify(heap, 1,funct)

    if reverse == True :
        heap.lst.reverse()

    return heap.lst



def is_greater(a,b):
    if a < b :
        return True
    return False

import random

def tests():
    testedList = [1, 7, 2, 6, 3, 4, 9, 33, 77, 22, 55]
    testList=deepcopy(testedList)
    testedList.sort()
    newLst=heapsort(testList,is_greater)

    print(testedList)
    print(newLst)

    testL=[]
    for i in range (0,10000) :
        testL.append(random.randint(0,50000))
    testedLst=deepcopy(testL)
    sorted(testL)
    heapsort(testedList,is_greater)

    assert testL == testedLst



tests()

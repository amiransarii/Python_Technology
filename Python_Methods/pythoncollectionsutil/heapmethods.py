#Heap data structure is mainly used to represent a priority queue. In Python, it is available using “heapq” module
import heapq
class HeapMethod:

    def heapActions(self):
        self.heapMethod()
        self.heapMethod2()
        self.heapMethod3()


    def heapMethod(self):
        print("First Heap Method")
        ''''1. heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
        2. heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap.
        The order is adjusted, so as heap structure is maintained.
        3. heappop(heap) :- This function is used to remove and return the smallest element from heap. 
        The order is adjusted, so as heap structure is maintained.'''

        li = [5, 7, 9, 1, 3]
        heapq.heapify(li) # using heapify to convert list into heap
        print("The created heap is : ", end="")
        print(list(li))

        heapq.heappush(li,4) # pushes 4 # using heappush() to push elements into heap
        print("The modified heap after push is : ", end="") # printing modified heap
        print(list(li))

        print("The popped and smallest element is : ", end="") # using heappop() to pop smallest element
        print(heapq.heappop(li))
        print("The popped and smallest element is : ", end="")
        print(heapq.heappop(li))

    def heapMethod2(self):
        print("\nSecond Heap Method")
        '''1. heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. 
        Heap order is maintained after this operation.
        2. heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from above function. 
        In this, element is first popped, then the element is pushed.i.e, the value larger than the pushed value can be returned. 
        heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop().'''

        li1 = [5, 7, 9, 4, 3]  # initializing list 1
        li2 = [5, 7, 9, 4, 3]  # initializing list 2
        heapq.heapify(li1) # using heapify() to convert list into heap
        heapq.heapify(li2) # using heapify() to convert list into heap
        print("The popped item using heappushpop() is : ", end="")
        print(heapq.heappushpop(li1, 2)) #using heappushpop() to push and pop items simultaneously pop
        print("The popped item using heapreplace() is : ", end="")
        print(heapq.heapreplace(li2, 2))

    def heapMethod3(self):
        print("\n Third Heap Method")
        '''1. nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from 
              the iterable specified and satisfying the key if mentioned.
           2. nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the 
              iterable specified and satisfying the key if mentioned.'''
        # initializing list
        li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
        heapq.heapify(li1)  # using heapify() to convert list into heap
        print("The 3 largest numbers in list are : ", end="") # using nlargest to print 3 largest numbers     # prints 10, 9 and 8
        print(heapq.nlargest(3, li1))
        print("The 3 smallest numbers in list are : ", end="") # using nsmallest to print 3 smallest numbers         # prints 1, 3 and 4
        print(heapq.nsmallest(3, li1))

from  collections import  deque
'''
Deque is preferred over list in the cases where we need quicker append and pop operations from
both the ends of container'''
class DQMethod:

    def dqActions(self):
        self.dqCreation()
        self.dqMethod()
        self.dqMethod2()

    def dqCreation(self):
        print("DQCreation")
        queue = deque(['name','age','DOB']) # Declaring deque
        '''append() :- This function is used to insert the value in its argument to the right end of deque.
           appendleft() :- This function is used to insert the value in its argument to the left end of deque.
           pop() :- This function is used to delete an argument from the right end of deque.
           popleft() :- This function is used to delete an argument from the left end of deque. '''
        de = deque([1, 2, 3])# Declaring deque
        de.append(4) # using append() to insert element at right end   # inserts 4 at the end of deque
        print("The deque after appending at right is : ") # printing modified deque
        print(de)

        de.appendleft(6) # using appendleft() to insert element at left end    # inserts 6 at the beginning of deque
        print("The deque after appending at left is : ")  # printing modified deque
        print(de)

        de.pop()  # using pop() to delete element from right end   # deletes 4 from the right end of deque
        print("The deque after deleting from right is : ") # printing modified deque
        print(de)

        de.popleft() # using popleft() to delete element from left end  # deletes 6 from the left end of deque
        print("The deque after deleting from left is : ")
        print(de)

    def dqMethod(self):
        '''index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
        insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
        remove() :- This function removes the first occurrence of value mentioned in arguments.
        count() :- This function counts the number of occurrences of value mentioned in arguments.'''

        de = deque([1, 2, 3, 3, 4, 2, 4]) # initializing deque
        print("The number 4 first occurs at a position : ")  # using index() to print the first occurrence of 4
        print(de.index(4, 2, 5))

        de.insert(4, 3)  # using insert() to insert the value 3 at 5th position
        print("The deque after inserting 3 at 5th position is : ")
        print(de)

        print("The count of 3 in deque is : ")
        print(de.count(3))# using count() to count the occurrences of 3

        de.remove(3)  # using remove() to remove the first occurrence of 3
        print("The deque after deleting first occurrence of 3 is : ")
        print(de)

    def dqMethod2(self):
        '''extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
        extendleft(iterable) :- This function is used to add multiple values at the left end of deque. The argument passed is an iterable.
         Order is reversed as a result of left appends.
        reverse() :- This function is used to reverse order of deque elements.
        rotate() :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left.
        Else rotation is to right.  '''
        # initializing deque
        de = deque([1, 2, 3, ])

        de.extend([4, 5, 6])# using extend() to add numbers to right end   # adds 4,5,6 to right end
        print("The deque after extending deque at end is : ")
        print(de)

        de.extendleft([7, 8, 9]) # using extendleft() to add numbers to left end  # adds 7,8,9 to right end
        print("The deque after extending deque at beginning is : ")
        print(de)

        de.rotate(-3)  # using rotate() to rotate the deque  # rotates by 3 to left
        print("The deque after rotating deque is : ")
        print(de)

        de.reverse()# using reverse() to reverse the deque
        print("The deque after reversing deque is : ")
        print(de)
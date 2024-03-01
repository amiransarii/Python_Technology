"""Any and All are two built ins provided in python used for successive And/Or.
1. Any->Returns true if any of the items is True. It returns False if empty or all are false
Any can be thought of as a sequence of OR operations on the provided iterables..
2.All->Returns true if all of the items are True (or if the iterable is empty). All can be thought of as
 a sequence of AND operations on the provided iterables It also short circuit the execution i.e. stop the execution as soon as the result is known.

"""
class AnyAllMethod:

    def anyallactions(self):
        self.anyMethod1()
        self.allMethod2()

    def anyMethod1(self):
        print("AnyMethod....")
        print(any([False, False, False, False])) # Since all are false, false is returned
        print(any([False, True, False, False])) # second item (True) and will return True.
        print(any([True, False, False, False])) # first (True) and will return True.

    def allMethod2(self):
        print("\nAll Method")
        print (all([True, True, True, True])) # will return True and the same will be printed
        print(all([False, True, True, False])) # first item (False) and will return False.
        print(all([False, False, False])) # True is found in the iterables

    def practicalExamplesAny(self): # This code explains how can we use 'any' function on list
        print("\npracticalExamplesAny")
        list1 =[]
        list2 =[]
        # Index ranges from 1 to 10 to multiply
        for i in range(1,11):
            list1.append(4*i)

        # Index to access the list2 is from 0 to 9
        for i in range(0,10):
            list2.append(list1[i]%5== 0)

        print('See whether at least one number is divisible by 5 in list 1=>')
        print(any(list2))

    def practicalExamplesAll(self):
        print("\npracticalExamplesAll")
        list1 =[]
        list2 =[]

        for i in range(1, 21): # All numbers in list1 are in form: 4*i-3
            list1.append(4 * i - 3)

        for i in range(0,20): # list2 stores info of odd numbers in list1
            list2.append(list1[i]%2==1)
            
        print('See whether all numbers in list1 are odd =>')
        print(all(list2))

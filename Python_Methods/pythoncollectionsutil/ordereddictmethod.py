'''An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted.
The only difference between dict() and OrderedDict() is that: OrderedDict preserves the order in which the keys are inserted. '''
import collections
from collections import OrderedDict
class OrderedDictMethod:

    def orderedDictActions(self):
        self.orderedDict()
        self.updateMethod()
        self.deleteMethod()

    def orderedDict(self):
        print("Ordered Dictionary Creation")
        mdict ={}
        mdict['a'] = 1
        mdict['b'] = 2
        mdict['c'] = 3
        mdict['d'] = 4
        print("This is a Dict:")
        for k, v in mdict.items():
            print(k, v)

        print("This is an Ordered Dict:")
        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
        for key, value in od.items():
            print(key, value)


    def updateMethod(self): #Key value Change: If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict. '''
        print("\nAfter Changing Value")
        print("Before: ")
        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4

        for key, value in od.items():
            print(key, value)

        print("After:")
        od['c'] = 5
        for k, v in od.items():
            print(k,v)

    def deleteMethod(self): #Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict, however, maintains the order of insertion.
        print("\nDeleteMethod")
        print("Before deleting")
        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
        for key, value in od.items():
            print(key, value)

        print("After deleting:")
        od.pop('c')
        for key, value in od.items():
            print(key, value)
        print("After re-inserting:")
        od['c'] = 3
        for key, value in od.items():
            print(key, value)










'''Python contains a container called “ChainMap” which encapsulates many dictionaries into one unit'''
import collections
from  collections import ChainMap
class ChainMapMethod:
    def chaiMapActions(self):
        self.defineChainMap()
        self.accessOperations()
        self.manipulatingOperations()


    def defineChainMap(self):
        print("Defining Chain Map")
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        d3 = {'e': 5, 'f': 6}
        c = ChainMap(d1,d2,d3)
        print(c)

    def accessOperations(self):
        print("\nChain Map Access Operations")
        '''keys() :- This function is used to display all the keys of all the dictionaries in ChainMap.
        values() :- This function is used to display values of all the dictionaries in ChainMap.
        maps() :- This function is used to display keys with corresponding values of all the dictionaries in ChainMap.'''
        dic1 = {'a': 1, 'b': 2}
        dic2 = {'b': 3, 'c': 4}
        chain = collections.ChainMap(dic1,dic2) # initializing ChainMap
        print("All the ChainMap contents are : ")
        print(chain.maps)
        print("All keys of ChainMap are : ")
        print(list(chain.keys()))
        print("All values of ChainMap are : ")
        print(list(chain.values()))

    def manipulatingOperations(self):
        print("\nManipulating Operation")
        '''new_child() :- This function adds a new dictionary in the beginning of the ChainMap.
        reversed() :- This function reverses the relative ordering of dictionaries in the ChainMap'''
        # initializing dictionaries
        dic1 = {'a': 1, 'b': 2}
        dic2 = {'b': 3, 'c': 4}
        dic3 = {'f': 5}
        chain = collections.ChainMap(dic1, dic2)# initializing ChainMap
        print("All the ChainMap contents are : ")
        print(chain.maps)
        chain1 = chain.new_child(dic3)   # using new_child() to add new dictionary
        # print("Displaying new ChainMap : ")
        print(chain1.maps)
        print("Value associated with b before reversing is : ", end="")  # displaying value associated with b before reversing
        print(chain1['b'])
        chain1.maps = reversed(chain1.maps)  # reversing the ChainMap
        # print("Value associated with b after reversing is : ", end="")  # displaying value associated with b after reversing
        print(chain1['b'])



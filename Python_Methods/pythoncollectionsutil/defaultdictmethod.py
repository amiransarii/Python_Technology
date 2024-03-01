'''Dictionary in Python is an unordered collection of data values that are used to store data values like a map'''
from  collections import  defaultdict
class DefaultDictMethod:

    def defaultDictActions(self):
        self.dictMethod()
        self.defaulDictMethod()
        self.listdefaultfactory()
        self.intdefaultfactory()


    def dictMethod(self):
        print("\nSimple Dict Method")
        Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
        print("Dictionary:")
        print(Dict)
        print(Dict[1])
        #print(Dict[4]) # will raise a KeyError as the  4 is not present in the dictionary

    def def_value(self):# Function to return a default values for keys that is not present
        return "Not Present"

    def defaulDictMethod(self):
        print("\nDefault Dict Method")
        d = defaultdict(self.def_value)
        d["a"] = 1
        d["b"] = 2
        print(d["a"])
        print(d["b"])
        print(d["c"])

    def listdefaultfactory(self): #list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.
        print("\nList Default Method")
        d = defaultdict(list) # Defining a dict
        for i in range(5):
            d[i].append(i)
        print("Dictionary with values as list:")
        print(d)

    def intdefaultfactory(self): #int class is passed as the default_factory argument, then a defaultdict is created with default value as zero.
        print("\nInt Default Method")
        d = defaultdict(int) # Defining the dict
        L = [1, 2, 3, 4, 2, 4, 1, 2]
        for i in L:
            d[i] += 1
        print(d)


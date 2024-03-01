from  collections import  Counter
'''A Counter is a subclass of dict. Therefore it is an unordered collection
where elements and their respective count are stored as a dictionary. This is equivalent to a bag or multiset of other languages.
Initialization :

The constructor of counter can be called in any one of the following ways :
1. With sequence of items
2. With dictionary containing keys and counts
3. With keyword arguments mapping string names to counts '''

class CounterMethod:

    def counterActions(self):
        self.counter_initialization()
        self.update()
        self.countArithmetic()
        self.frequency()


    def counter_initialization(self):
        print("\Initialize method")
        print(Counter(['B','B','A','B','C','A','B','B','A','C'])) ## With sequence of items-> Counter({'B': 5, 'A': 3, 'C': 2})
        print(Counter({'A':3,'B':5,'C':2})) # with dictionary ->Counter({'B': 5, 'A': 3, 'C': 2})
        print(Counter(A=3,B = 5,C=2)) # with keyword arguments ->Counter({'B': 5, 'A': 3, 'C': 2})


    def update(self):
        print("\nUpdate Method")
        count = Counter() #We can also create an empty counter in the following manner :
        count.update([1, 2, 3, 1, 2, 1, 1, 2]) #Counter({1: 4, 2: 3, 3: 1})
        print(count)
        count.update([1,2,4]) #Counter({1: 5, 2: 4, 3: 1, 4: 1})
        print(count)

    def countArithmetic(self): # Counter can be 0 and negative
        print("\nArithmetic")
        c1 = Counter(A=4, B=3, C=10)
        c2 = Counter(A=10, B=3, C=4)
        c1.subtract(c2)
        print(c1)

    def frequency(self):#We can use Counter to count distinct elements of a list or other collections
        print("\nFrequency")
        z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red'] #->Counter({'blue': 3, 'red': 2, 'yellow': 1})
        print(Counter(z))






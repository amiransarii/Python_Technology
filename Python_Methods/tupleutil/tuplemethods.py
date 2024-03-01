class TupleMethods:

    def tupleOperations(self):
        self.tupleCreationMethod()
        self.tupleAccessing()
        self.unpackingTuple()
        self.joinTuple()

    def tupleCreationMethod(self):
        print("Tuple Creation ")
        t = ("Benz","BMW","Toyota")
        print("Tuple Items are:", t)
        print("Length of the Tuple ",len(t))
        t = tuple(("Benz","BMW","Toyota")) #using constructor
        print("Tuple Items are:",t)


    def tupleAccessing(self):
        print("\nAccessing Tuple")
        t = ("Benz", "BMW", "Toyota","Honda","Ford","GMC","Flat")
        print("Item at Index 2",t[2])
        print("Items between 3 and 6 ",t[3:6])
        print("Items upto index 3", t[:3])
        print("Items after given Index till end ",t[3:])
        print("Negative Index ",t[-5])
        print("Negative Range ",t[-5:-2])

    def updateTuple(self):
        """Tuple is immutable, we can not add,remove or modfiy the items once it is created
        However, list is mutable, and we can edit the items in a list by method
        1. Convert tuple to list
        2. update or delete item from list
        3. Change back to tuple-> tuple(list)
        4. Delete Tuple -> del thetuple(tuple name)"""
        pass


    def unpackingTuple(self):
        print("\nUnpacking Tuple")
        """Accessing the items of tuple in order is called , unpacking a tuple"""
        cars = ("Benz","BMW","Toyota")
        (first, second, third) = cars
        print(first,second,third)

        cars =["Benz","BMW","Toyota","Ford","Honda"]
        (first, second,*remaining) = cars
        print("Using *(variable length) ", "First = ",first,"Second =",second," Remaining",remaining)

        (first,*second,last) = cars
        print("Using *(variable length) ", "First = ", first, "Second =", second, " last", last)

    def joinTuple(self):
        print("\nJoin Tuple")
        cars = ("Benz", "BMW", "Toyota")
        added = cars + cars
        print("using +",added)

        multily = cars*2
        print("Using Multiply",multily)
class SetMethod:
    mset = set() # create a set method

    def setOperation(self):
        while True:
            try:
                choice = int(input("0.Display 1.Add 2.Clear 3.Copy Items 4.Difference_And_Difference_Update 5.Discard_Remove\n"
                "6.Intersection_And_Update 7.Isdisjoint 8.Symmetric_Difference 9.IsSubset 10.Issuperset 11.popped Element\n"
                "12.Find Union 13.Update:  "))
                if choice == 0:
                    self.display()
                elif choice == 1:
                    self.add()
                elif choice == 2:
                    self.clear()
                elif choice == 3:
                    self.copy()
                elif choice == 4:
                    self.difference_and_differnceupdate()
                elif choice == 5:
                    self.discard_Remove()
                elif choice == 6:
                    self.intersection_and_update()
                elif choice == 7:
                    self.isdisjoint()
                elif choice == 8:
                    self.symmetric_difference()
                elif choice == 9:
                    self.issubset()
                elif choice == 10:
                    self.issuperset()
                elif choice == 11:
                    self.pop()
                elif choice == 12:
                    self.union()
                elif choice == 13:
                    self.upate()
                else:
                    print("Invalid Choice")
            except ValueError as ve:
                print("Please Enter Correct Integer Choice: ")
                continue


    def add(self): # add item into set
        item = input("Enter Item: ")
        self.mset.add(item)

    def display(self): #display set items
        print("Set Items are :")
        print("Set Items are ",self.mset)

    def clear(self): # clear items from set
        print("Clearing Items from  Set: ")
        self.mset.clear()

    def copy(self):
        mset_copy =self.mset.copy()
        print("Copied Elements ",mset_copy)

    '''List all the unique colors that are present in group3 but not in group2 and group1
       unique_colors = group3.difference(group1, group2)'''
    def difference_and_differnceupdate(self):
        group1 ={"Yellow","White","Blue"}
        group2 ={"White","Blue","Red"}
        group3 ={"Black","Green","White","Blue","Red"}
        diff = group3.difference(group1, group2) # store in  different set variable Return the difference of two or more sets as a new set.
        group3.difference_update(group1,group2) # store in existing set Remove all elements of another set from this set
        print("Using Difference: ",diff)
        print("Using Difference_Update: ", group3)

    """List all the colors of lego blocks present in groups1 or group2 but not
           in group1 and group2"""
    def symmetric_difference(self):
        group1 = {"Yellow", "White", "Blue"}
        group2 = {"White", "Blue", "Red"}
        result = group1.symmetric_difference(group2) #group1^group2
        print(result)


    def discard_Remove(self): # Remove and discard element
        item = input("Enter the items, which you want to remove from set: ")
        print("Discarding element from Set ...")
        self.mset.discard(item) # will not throw exception
        print("Removing Element from Set ...")
        try:
            self.mset.remove(item)   # will throw exception, if value is not available in set
        except KeyError:
            print("Value is not found in set")

    def intersection_and_update(self):
        group1 = {"Yellow", "White", "Blue"}
        group2 = {"Green", "Blue", "Red"}
        mset_intersection = group1.intersection(group2) #Return the intersection of two sets as a new set.
        print("Sets using after intersection ",mset_intersection)
        group2.intersection_update(group1) #Update a set with the intersection of itself and another.
        print("Sets using after intersection_update ", group2)

    #Return True if two sets have a null intersection.
    def  isdisjoint(self): #Find if there are any colors that are present in both group1 and group2
        group1 = {"Yellow", "White", "Blue"}
        group2 = {"Green","Red"}
        isDisjoint = group1.isdisjoint(group2)
        print("Is it Disjoint ",isDisjoint)

    def issubset(self):
        mset1 ={10,20,30,40,50}
        mset2 = {20,30,40}
        print("mset2 is subset of mset1",mset2.issubset(mset1))

    def issuperset(self):
        mset1 = {10, 20, 30, 40, 50}
        mset2 = {20, 30, 40}
        print("mset1 is superset of mset2", mset1.issuperset(mset2))

    # Remove and return an arbitrary set element.
    def pop(self):
        try:
            val =self.mset.pop()
            print("Popped Element ",val)
        except KeyError as ke:
            print("Key Does not Exist")

    def union(self): #Return the union of sets as a new set.
        mset1 = {10, 20, 30, 40, 50}
        mset2 = {20, 30, 40}
        unionset = mset1.union(mset2)
        print("Union of Two sets ",unionset)

    def upate(self): #Update a set with the union of itself and others.
        mset1 = {10, 20, 30, 40, 50}
        mset2 = {20, 30, 40}
        mset1.update(mset2)
        print("Updated two set ",mset1)













class ListMethods:
    mlist =[] # initialize

    def listOperation(self):
        while True:
            try:
                choice = int(input("0.Display 1.Append 2.Clear 3.Copy 4.count_items 5.Extend List,6.Find Index 7.Insert New Item 8.Pop Element "
                 "9.Remove Element 10.Reverse List 11.Sort Items: "))
                if choice == 0:
                    self.display()
                elif choice == 1:
                    self.append()
                elif choice == 2:
                    self.clear()
                elif choice == 3:
                    self.copy()
                elif choice == 4:
                    item = input("Enter that item, you want to check repetition: ")
                    self.count_items(item)
                elif choice == 5:
                    self.extendList([10,20,30,40])
                elif choice == 6:
                    ele = input("Enter the Element which you want to get Index : ")
                    self.findIndex(ele)
                elif choice == 7:
                    pos,item = input("Enter Item and Position you want to insert in same line with space: ").split()
                    self.insert(pos,item)
                elif choice == 8:
                    idx = int(input("Please Enter Index, which you want to pop: "))
                    self.pop()
                elif choice == 9:
                    ele = input("Enter Element , which you want to remove: ")
                    self.remove(ele)
                elif choice == 10:
                    self.reverse()
                elif choice == 11:
                    self.sort()
                else:
                    pass
            except ValueError:
                print("Please Enter correct Integer choice")
                continue

    def append(self): #append item into list
        item = input("Enter Item: ")
        self.mlist.append(item) #append new item into list


    def display(self):  # display list of items
        print("List Items are ",self.mlist)

    def clear(self): # clear items from list
        self.mlist.clear() # clear list

    def copy(self):
        mlist_copy = self.mlist.copy() #All items copied from mlist copy to mlist_copy
        print("Copied All Items from mlist to mlist_copy ",mlist_copy)
        mlist_copy_1_3 =self.mlist.copy()[1:3]
        print("Copied 3 items",mlist_copy_1_3)
        mlist_copy =[]
        mlist_copy.extend(self.mlist) #copy self.mlist into
        mlist_copy = self.mlist

    def count_items(self,item):
        #count_item = self.mlist.count(item) # count item repetition
        count_item = self.mlist[1:3].count(item) # count item from index 1 to 4
        print(count_item)

    def extendList(self,new_items:list):
        self.mlist.extend(new_items) # extend new list with existing list
        print("New List After appending with existing List ",self.mlist)


    def findIndex(self,item):
        if self.mlist != [] and item in self.mlist:
            idx = self.mlist.index(item)
            #idx = self.mlist.index(item,0,3)
            # idx = self.mlist[1:3].index(item) search inside subslist
            print("{0} item exist at {1} position ".format(item, idx))
        else:
            print(item, "does not exit")
        # or
        """try:
        idx = self.mlist.index(item)
        except ValueError:
        print("Index value not found")
        """

    def insert(self,pos,item):
        self.mlist.insert(int(pos),item) # insert item at given position


    def pop(self,index = -1): #Remove and return item at index (default last).
        try:
            self.mlist.pop(index)
            print("Removing Item at Index {}".format(index))
        except IndexError:
            print("Invalid Index, please Check it again")

    def remove(self,value):
        try:
            self.mlist.remove(value)
        except ValueError:
            print("Value does not exist in the list, Please check it again")


    def reverse(self):
        print("List Items are successfully reversed")
        # self.mlist.reverse() first method
        #self.mlist=self.mlist[::-1]
        self.mlist = list(reversed(self.mlist))

    def sort(self):
         if self.mlist ==[] or len(self.mlist) == 0:
             print("Sorry List is Empty")
             return None
         print("Successfully Sorted List Items")
         #self.mlist =  list(map(int,self.mlist)) # convert string item into integer
         #self.mlist.sort()
         #self.mlist.sort(key=len,reverse=True) #reverse order sorted first maximum length
         self.mlist = sorted(self.mlist,key=len,reverse=True) #sorted() method will return a new list with sorted item
         #self.mlist.sort(key=str.lower)
         #self.mlist.sort(reverse=True) descending order
         # sort() method is case sensitive, and it position the uppercase letters before  the lowercase letters

         '''def func(a):
             return abs(a-0)
         self.mlist.sort(key=func)'''




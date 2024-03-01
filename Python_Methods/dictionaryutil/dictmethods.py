class DictMethods:
    mdict = dict()

    def dictOperation(self):
        while True:
            try:
                choice = int(input("0.Display 1.Create Dictionary 2.Copy_And_Creation 3.Clear_Remove 4.Get Value\n"
                                   "5.items_kyes_values 6.setdefault: "))
                if choice == 0:
                    self.display()
                elif choice == 1:
                    self.addKeyValue()
                elif choice == 2:
                    self.copy_And_Creation()
                elif choice == 3:
                   self.clear_Remove_pop()
                elif choice == 4:
                    self.getValue()
                elif choice == 5:
                    self.items_kyes_values()
                elif choice == 6:
                    self.setdefault()
                else:
                    print("Invalid Choice")


            except ValueError:
                print("Please Enter correct Integer choice")
                continue


    def display(self):
        print("Dictionary Items are: ")
        print(self.mdict)

    def addKeyValue(self):
        k, v = input("Enter Key and Value in same line with space ").split()
        self.mdict[k] = v

    def copy_And_Creation(self):
        mdict_copy = self.mdict.copy()
        print("Copied Dictionary Using Copy:{}".format(mdict_copy))
        mdict_copy ={}
        mdict_copy = dict(self.mdict)
        print("Using Empty Dictionary ",mdict_copy)
        # update dictionary self.mdict.update(mdict_copy)

    def clear_Remove_pop(self):
         try:
             key = input("Enter Key, which you want to remove: ")
             del self.mdict[key]
         except KeyError as ke:
             print("Key Does not exist")
         print("After Removing given Key {} and dic is {}".format(key,self.mdict))
         #popped_item = self.mdict.pop(key)
         popped_item= self.mdict.popitem() # remove last key from

         print("Clearing Dict Items: ")
         self.mdict.clear()

    def getValue(self): #Return the value for key if key is in the dictionary, else default.
        key = input("Enter the Key: ")
        value = self.mdict.get(key,"Key Does not exit")
        print(value)

    def items_kyes_values(self):
        keys = self.mdict.keys()
        items = self.mdict.items()
        values = self.mdict.values()

        print("Keys are:: ")
        for key in keys:
            print(key,end =' ')

        print("\nItems are:: ")
        for k,v in items:
            print(k,v, end =' ')

        print("\nValues are :: ")
        for val in values:
            print(val, end =' ')

    def setdefault(self): #Insert key with a value of default if key is not in the dictionary.
        key = input("Enter the Key, to set Default Value: ")
        self.mdict.setdefault(key,"Default Value is set for this given key")


    #Sort by frequency, if frequncy same sort by element
    def sortbyFrequency(self):
        from collections import Counter
        def perseus_sort(l):
            counter = Counter(l)
            return sorted(l, key=lambda x: (counter[x], x)) #ascending order frequency
            return sorted(a, key=lambda x: (-counter[x], x)) #descending order frequency, if frequncy same , pickup lower value




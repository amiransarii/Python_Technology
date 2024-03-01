class FactMethod:

    def factActions(self):
        self.funcdriver()
        self.unpackList()
        self.InfinitiesValues()





    def funcdriver(self):
        print("1st Case:")
        a = [2]
        self.func(a)
        print("2nd Case:")
        a = [1]
        self.func(a)

    def func(self,array): # Multiple Return Values in Python!
        print("1.For Else Statement")
        for num in array:
            if num%2 == 0:
                print(num)
                break # Case1: Break is called, so 'else' wouldn't be executed.
        else: # Case 2: 'else' executed since break is not called
            print("No call for Break. Else is executed")

    def point(self,x,y):
        print(x,y)


    def unpackList(self):
        """One can unpack a list or a dictionary as function arguments using * and ** respectively. This is commonly known as the Splat operator"""
        foo_list =(3,4)
        bar_dict ={'y': 3, 'x': 2}
        self.point(*foo_list)# Unpacking Lists 3 4
        self.point(**bar_dict) # Unpacking Dictionaries 2 3

    def InfinitiesValues(self):
        """We can’t define Infinities right? But wait! Not for Python. See this amazing example"""
        p_infinity = float('Inf')   # Positive Infinity
        if 99999999999999 > p_infinity:
            print("The number is greater than Infinity!")
        else:
            print("Infinity is greatest")

        n_infinity = float('-Inf')  # Negative Infinity
        if -99999999999999 < n_infinity:
            print("The number is lesser than Negative Infinity!")
        else:
            print("Negative Infinity is least")


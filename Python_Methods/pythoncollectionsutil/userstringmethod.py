"""This class is useful when one wants to create a string of their own with some modified functionality or with some new functionality
collections.UserString(seq)"""
from  collections import  UserString
class UserStringMethod:

    def userStringActions(self):
        self.userStringMethod1()
        self.userStringMethod2()

    def userStringMethod1(self):
        d = 12344
        userS = UserString(d) # Creating an UserString
        print(userS.data)

        userS = UserString("") # Creating an empty UserDict
        print(userS.data)

    def userStringMethod2(self):
        s1 = MyString("Geeks")
        print("Original String:",s1.data)

        s1.append("s") # Appending to string
        print("String After Appending:",s1.data)

        s1.removed("e") # Removing from string
        print("String After Removing:",s1.data)



class MyString(UserString):# Python program to demonstrate # Creating a Mutable String

    def append(self,s): #Function to append to string
        self.data += s

    def removed(self,s): #Function to remove from sring
        self.data = self.data.replace(s,"")


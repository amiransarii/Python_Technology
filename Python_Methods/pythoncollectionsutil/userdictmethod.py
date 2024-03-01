"""Python supports a dictionary like a container called UserDict present in the collections module. This class acts
 as a wrapper class around the dictionary objects. This class is useful when one wants to create a dictionary
of their own with some modified functionality or with some new functionality. """

from collections import  UserDict
class UserDictMethod:

    def userDictActions(self):
        self.userDictMethod1()
        self.userDictMethod2()

    def userDictMethod1(self):
        d = {'a':1,'b': 2, 'c': 3}
        userD = UserDict(d) # creating an user dict
        print(userD.data)

        userD = UserDict() #creating an empty userDict
        print(userD.data)

    def userDictMethod2(self): #create a class inheriting from UserDict to implement a customized dictionary.
        d =  MyDict({'a':1,'b': 2,'c': 3})
        print("Original Dictionary")
        print(d)
        d.pop(1)


class MyDict(UserDict): # Creating a Dictionary where deletion is not allowed

    def __del__(self): #Function to stop deletion rom dictionary
        raise RuntimeError("Deletion is not allowed")

    def pop(self): # Function to stop pop from  dictionary
        raise RuntimeError("Deletion is not allowed")

    def popitem(self,s=None):
        raise RuntimeError("Deletion is not allowed")





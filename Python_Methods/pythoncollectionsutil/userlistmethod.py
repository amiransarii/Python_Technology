from collections import  UserList
"""Python supports a List like a container called UserList present in the collections module.
This class acts as a wrapper class around the List objects.
This class is useful when one wants to create a list of their own with some modified functionality or with some new functionality.
collections.UserList([list])"""

class UserListMethod:
    def userListActions(self):
        self.userListMethod1()
        self.userListMethod2()

    def userListMethod1(self):
        L = [1, 2, 3, 4]
        userL = UserList(L) # Creating a userlist
        print(userL.data)

        userL = UserList() # Creating empty userlist
        print(userL.data)

    def userListMethod2(self):
        L = MyList([1,2,3,4])
        print("Original List")
        L.append(5) # Inserting to List
        print("After Insertion")
        print(L)

        L.remove() #deleting from list




class MyList(UserList):# deletion is not allowed

    def remove(self,s = None): #Function to stop deletion
        raise RuntimeError("Deletion not allowed")

    def pop(self,s = None):# Function to stop pop from
        raise RuntimeError("Deletion not allowed")




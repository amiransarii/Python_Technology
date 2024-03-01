from pythoncollectionsutil import  countersmethod
from pythoncollectionsutil import ordereddictmethod
from  pythoncollectionsutil import defaultdictmethod
from  pythoncollectionsutil import chainmapmethod
from pythoncollectionsutil import  namedtuplemethods
from  pythoncollectionsutil import  dqmethods
from  pythoncollectionsutil import  heapmethods
from pythoncollectionsutil import userdictmethod
from  pythoncollectionsutil import  userlistmethod
from pythoncollectionsutil import  userstringmethod

class PythonCollections:
    def pythoncollectionAction(self):
        choice = int(
            input("Enter Choice 1.Counter 2.OrderedDict 3.DefaultDict 4.ChainMap 5.NamedTuple 6.Deque 7.Heap 8.UserDict 9.UserList 10.UserString : "))
        if choice == 1:
            countersmethod.CounterMethod().counterActions()
        elif choice == 2:
            ordereddictmethod.OrderedDictMethod().orderedDictActions()
        elif choice == 3:
            defaultdictmethod.DefaultDictMethod().defaultDictActions()
        elif choice == 4:
            chainmapmethod.ChainMapMethod().chaiMapActions()
        elif choice == 5:
            namedtuplemethods.NamedTupleMethod().nameTupleActions()
        elif choice == 6:
            dqmethods.DQMethod().dqActions()
        elif choice == 7:
            heapmethods.HeapMethod().heapActions()
        elif choice == 8:
            userdictmethod.UserDictMethod().userDictActions()
        elif choice == 9:
            userlistmethod.UserListMethod().userListActions()
        elif choice == 10:
            userstringmethod.UserStringMethod().userStringActions()










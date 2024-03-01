''' they contain keys that are hashed to a particular value. But on contrary,
it supports both access from key-value and iteration, the functionality that dictionaries lack.'''
from collections import namedtuple
class NamedTupleMethod:
    def nameTupleActions(self):
        self.namedtupleCreation()
        self.namedtupleOperations()


    def namedtupleCreation(self):
        Student = namedtuple('Student', ['name', 'age', 'DOB'])# Declaring namedtuple()
        S = Student('Nandini', '19', '2541997') # Adding values
        print("The Student age using index is : ", end="")
        print(S[1])
        print("The Student name using keyname is : ", end="") # Access using name
        print(S.name)

    def namedtupleOperations(self):
        print("\nnamedtuple operations")
        '''1. Access by index: The attribute values of namedtuple() are ordered and can be accessed using the index number
        unlike dictionaries which are not accessible by index.
        2. Access by keyname: Access by keyname is also allowed as in dictionaries.
        3. using getattr(): This is yet another way to access the value by giving namedtuple and key value as its argument'''
        Student = namedtuple('Student', ['name', 'age', 'DOB'])
        S = Student('Nandini', '19', '2541997') # Adding values
        # Access using index
        print("The Student age using index is : ", end="")
        print(S[1])
        # Access using name
        print("The Student name using keyname is : ", end="")
        print(S.name)
        # Access using getattr()
        print("The Student DOB using getattr() is : ", end="")
        print(getattr(S, 'DOB'))


class FunctionMethod:

    def functionAction(self):
        self.eveodd(3)
        self.defaultFunc(10)
        self.keywordFunc(lastname='Ansari',firstname='Amir')
        self.argFunc('Hello', 'Welcome', 'to', 'GeeksforGeeks')
        self.kwargsFun(first='Geeks', mid='for', last='Geeks')
        print(self.docFunc.__doc__)
        self.refCall()

    # Simple function
    def eveodd(self,x):
        if x%2 == 0:
            print("Even")
        else:
            print("Odd")

    # Default Argument
    def defaultFunc(self, x, y = 50):
        print("x: ",x)
        print("y: ",y)

    #Keyword arguments
    def keywordFunc(self,firstname, lastname):
        print("First Name is {} and Last Name are {} ".format(firstname,lastname))

    #*args (Non-Keyword Arguments)
    def argFunc(self,*argv):
        for arg in argv:
            print(arg,end =' ')

    #**kwargs (Keyword Arguments)'''
    def kwargsFun(self,**kwargs):
        print("")
        for key,value in kwargs.items():
            print("%s == %s" % (key, value), end ='->')
        print()

   #The first string after the function is called the Document string or Docstring
    def docFunc(self,x):
        """Function to check if the number is even or odd"""
        if x%2 == 0:
            print("Even")
        else:
            print("Odd")


    def refCall(self):
        lst = [10, 11, 12, 13, 14, 15]
        self.pythonRef(lst)
        print(lst)

        self.pythonRef2(lst)
        print(lst)

        x = 10
        self.pythonRef3(x)
        print(x)

    def pythonRef(self,x):
        '''One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function,
        a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.'''
        x[0] = 20 #Here x is a new reference to same list lst

    def pythonRef2(self,x):
        """When we pass a reference and change the received reference to something else, the connection
        between the passed and received parameter is broken. For example, consider the below program."""
        x = [20, 30, 40]

    def pythonRef3(self,x):
        """Another example to demonstrate that the reference link is broken if we assign a new value (inside the function)."""
        x = 20


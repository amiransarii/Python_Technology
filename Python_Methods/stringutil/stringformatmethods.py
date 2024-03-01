import datetimemethodutil
class StringFormat:

    def stringformatOperations(self):
        self.formatMethodUsingPlaceHolder()
        self.formatMethodUsingIndex()
        self.formatUsingKeyWordArgument()
        self.customizedFormat()


    def formatMethodUsingPlaceHolder(self):
        print("\nFormat Method Using Place Holder")
        car ="Benz"
        msg ="The car is:{}"
        print(msg.format(car))

        # Values from dictionary
        person ={"name":"Sara","age":34}
        msg ="Hi {}, You are {} old".format(person["name"],person["age"])
        print(msg)

        msg = "Hi {0[name]} you are {1[age]} old".format(person,person) # access the variable from placeholder
        print(msg)

        '''
        The 0 index here represent the same student object in format() method
        student = Person("Sara",34)
        msg ="Hi{0.name}. You are {0.age} years old".format(student) '''

    def formatMethodUsingIndex(self):
        print("\nFormat Using Index")
        name ="Amir Ansari"
        age = 29
        msg ="Hi {0}, You are {1} old. Happy life {0}".format(name,age)
        print(msg)

    def formatUsingKeyWordArgument(self):
        print("\nformatUsingKeyWordArgument")
        msg = "Hi {name} Age:{age} years old".format(name="Sara",age ="34")
        print(msg)

        thedic ={"name":"Amir Ansari","age":34} #unpackinf the dictionary in format method
        msg = "Hi {name}.  You are {age} years old".format(**thedic)
        print(msg)


    def customizedFormat(self):
        num = 3.14159265359
        msg = "Number with two decimal is {:.2f}".format(num) #Do not forget to add colon(:) symbol
        print(msg)

        num =314159265359
        msg ="Number with commad is:{:,}".format(num) # Comma separatd
        print(msg)

        mydate = datetimemethodutil.datetime(1986, 11, 23)
        msg ="{:%Y %B %d}".format(mydate)
        print(msg)
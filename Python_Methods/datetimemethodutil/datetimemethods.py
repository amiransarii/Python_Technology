import datetime

class DateTimeMethod:
    def datetimeOperations(self):
        self.datetimeMethod1()
        self.datetimeFormat()
        self.strfimeMethod()

    def datetimeMethod1(self):
        time = datetime.datetime.now()
        print("Time is ",time)

    def datetimeFormat(self):
        print("\nDateTime Format")
        time = datetime.datetime.now()
        print(time.strftime("%B")) #November
        time = datetime.datetime(1986,11,23) #1986-11-23 00:00:00
        print(time)
        time = datetime.datetime(1986,11,23,14,30)
        print(time)


    def strfimeMethod(self):
        print("\nstrtime Method")
        """datetime object provides strftime() method to format date object into readable format
        strftime() method requires only one argument. The argument is the format which is chosen by user
        """
        time = datetime.datetime.now()
        print(time.strftime("%B"),end =' ') #November
        print(time.strftime("%A"), end =' ') #Sunday
        print(time.strftime("%Y"), end=' ') #2021


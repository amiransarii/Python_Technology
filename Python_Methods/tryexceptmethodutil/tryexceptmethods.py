class TryExcept:

    def tryExceptOpetation(self):
        self.NameException()
        self.NameErrorElseException()
        self.finallyBlock()
        self.specifiedException()
        self.customizeException()

    def NameException(self):
        try:
            print(a)
        except NameError:
            print("a is not defined")
        except:
            print("Something else is wrong")

    def NameErrorElseException(self):
        print("\nNameErrorElseException")
        """The else block runs the actual code that need to be executed if the try and except block did not catch any error"""
        try:
            print("Hi Sara")
        except NameError:
            print("Something was wrong")
        except:
            print("Something was wrong!")
        else:
            print("Everything is okay")

    def finallyBlock(self):
        print("\nFinally Block")
        """The finally block will run regardless of what happend to the previous blocks"""
        try:
            print("Hi Sara")
        except NameError:
            print("Something was wrong")
        finally:
            print("Executed any way")

        try:
            print(a)
        except NameError:
            print("Something was wrong")
        finally:
            print("Executed any way")

    def specifiedException(self):
        print("\nSpecified Exception")
        try:
            print(a)
        except NameError as ne:
            print(ne)

        except ValueError as ve:
            print(ve)

        except:
            print("Something else was wrong")

    def customizeException(self):
        x = 5
        if x < 7:
            raise Exception("x is less than 7")
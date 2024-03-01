class UserInputMethod:

    def printUserInput(self,choice):
        if choice == 1:
            mlist = input("Enter Inputs: ").split()  # mix inputs like integer, float, boolean,string etc
            #mlist =   list(map(int,input("Enter Inputs: ").split())) #integer inputs
            print("User Inputs in List Form are {}".format(mlist))

        elif choice == 2:
            arg1, arg2 = input("Enter First and Second Argument:").split() # mix inputs like integer, float, boolean,string etc
            #arg1, arg2  = map(int,input("Enter First and Second integer value ").split()) # interger value
            print("Your first Argument and Second Argument is {} {} respectively".format(arg1, arg2 ))


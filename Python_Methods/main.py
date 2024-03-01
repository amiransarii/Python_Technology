from userinput import userinputmethod
from listmethodsutil import listmethod
from setmethodsutil import setmethods
from dictionaryutil import dictmethods
from stringutil import  stringmethods
from pythoncollectionsutil import pythoncollections
from mathutil import mathmethods
from functionutil import functionmethods
from tupleutil import tuplemethods
from regexutil import regexmethods
from datetimemethodutil import datetimemethods
from tryexceptmethodutil import  tryexceptmethods
from operatorutils import  operatormethods
from databaseutil import databasemethods
from tipsutil import tipsmethod

def callUserInputMethods(): #call user input methods
    choice = int(input("Enter a choice 1 for store input in List form 2 is to store another variables: "))
    userinputmethod.UserInputMethod().printUserInput(choice)

def callListMethods():#call list methods
    listmethod.ListMethods().listOperation()

def callSetMethods():
    setmethods.SetMethod().setOperation()

def callDictMethods():
    dictmethods.DictMethods().dictOperation()

def callStringMethods():
    stringmethods.StringMethods().stringOperations()

def callCollectionMethod():
    pythoncollections.PythonCollections().pythoncollectionAction()

def callMathFunction():
    mathmethods.MathMethod().matchconverter()

def callFunctions():
    functionmethods.FunctionsMethod().functionsMethods()

def callTupleMethods():
    tuplemethods.TupleMethods().tupleOperations()

def callregexmethods():
    regexmethods.RegularExpression().regexOpertions()

def calldateTimeMethod():
    datetimemethods.DateTimeMethod().datetimeOperations()

def calltryexceptMethod():
    tryexceptmethods.TryExcept().tryExceptOpetation()

def calloperatorMethod():
    operatormethods.OperatorMethod().operatorActions()

def calldatabaseMethod():
    databasemethods.DatabaseMethod().databaseActions()

def calltipsMethod():
    tipsmethod.TipsMethod().tipsActions()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     ''' choice = int(input("1.callUserInputMethod 2.callListMethods 3.callSetMethods 4.callDictMethods 5.callStringMethods:
     6.callCollectionMethod 7.callMathFunction 8.callFunctions 9.callTupleMethods 10.callregexmethods 11.calldateTimeMethod()
     12.calltryexceptMethod 12.calloperatorMethod:"))
     if choice == 1:
         callUserInputMethods()
    elif choice == 2:
        callListMethods()
        elif choice == 3:
            callSetMethods()
        elif choice == 4:
            callDictMethods()
        elif choice == 5:
            callStringMethods()
        else:
            print("Invalid Choice") '''
     callMathFunction()


    #calltipsMethod()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

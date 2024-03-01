from functionutil import  functionmethod
from  functionutil import  lambdamethod
from functionutil import  yieldmethods
from  functionutil import  comprehensionsmethod

class FunctionsMethod:

    def functionsMethods(selfs):
        choice = int(input("Enter your choice 1.Function 2.Lambda 3.Yield 4.Comprehensions : "))
        if choice == 1:
            functionmethod.FunctionMethod().functionAction()
        elif choice == 2:
            lambdamethod.LambdaMethod().lambadFuncAction()
        elif choice == 3:
            yieldmethods.YieldMethod().yieldActions()
        elif choice == 4:
            comprehensionsmethod.ComprehensionsMethod().comprehensionsAction()



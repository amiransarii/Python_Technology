from operatorutils import  basicoperatormethod
from operatorutils import  ternaryoperatormethod
from  operatorutils import  anyallmethod
class OperatorMethod:
    def operatorActions(self):
        choice = int(input("1.BasicOperator 2.TernaryOperator 3.AnyAll:"))
        if choice == 1:
            basicoperatormethod.BasicOperator().basicoperatoractions()
        elif choice== 2:
            ternaryoperatormethod.TernaryOperator().ternaryOperatorActions()
        elif choice == 3:
            anyallmethod.AnyAllMethod().anyallactions()


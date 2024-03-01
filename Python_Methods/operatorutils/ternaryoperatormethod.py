class TernaryOperator:

    def ternaryOperatorActions(self):
        self.ternaryOperatorMethod1()
        self.nestedOperator()

    def ternaryOperatorMethod1(self):
        a, b = 10, 20
        min = a if a < b else b # Copy value of a in min if a < b else copy b
        print(min)

        min = a < b and a or b
        print(min)

    def nestedOperator(self):
        print("\nNested Operator")
        a, b = 10,20
        if a != b:
            if a > b:
                print("a is greater than b")
            else:
                print("b is greater than a")
        else:
            print("Both a and b are equal")



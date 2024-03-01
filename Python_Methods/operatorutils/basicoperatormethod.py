class BasicOperator:
    def basicoperatoractions(self):
        self.identityOperator()
        self.membershipOperator()
        self.operatorPrecedence()
        self.operatorAssociativity()

    def identityOperator(self):
        print("Identity Operator")
        a = 10
        b = 20
        c = a
        print(a is not b)
        print(a is c)

    def membershipOperator(self):
        print("\nMembership Operator")
        """in and not in are the membership operators; used to test whether a value or variable is in a sequence.
        1. in True if value is found in the sequence
        2. not in True if value is not found in the sequence"""

        x = 24
        y = 20
        list = [10, 20, 30, 40, 50]

        if (x not in list):
            print("x is NOT present in given list")
        else:
            print("x is present in given list")

        if (y in list):
            print("y is present in given list")
        else:
            print("y is NOT present in given list")

    def operatorPrecedence(self):
        print("\noperatorPrecedence")
        expr = 10 + 20 * 30 # Precedence of '+' & '*'
        print(expr)

        name ="Alex" # Precedence of 'or' & 'and'
        age = 0

        if name =="Alex" or name =="John" and age >=2:
            print("Hello| Welcome.")
        else:
            print("Good Bye !!")

    def operatorAssociativity(self):
        print("\nOperator Associativity")
        # Left-right associativity
        # 100 / 10 * 10 is calculated as
        # (100 / 10) * 10 and not
        # as 100 / (10 * 10)
        print(100 / 10 * 10)
        # Left-right associativity
        # 5 - 2 + 3 is calculated as
        # (5 - 2) + 3 and not
        # as 5 - (2 + 3)
        print(5 - 2 + 3)
        # left-right associativity
        print(5 - (2 + 3))
        # right-left associativity
        # 2 ** 3 ** 2 is calculated as
        # 2 ** (3 ** 2) and not
        # as (2 ** 3) ** 2
        print(2 ** 3 ** 2)
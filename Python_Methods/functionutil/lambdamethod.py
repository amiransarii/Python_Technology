
class LambdaMethod:
    def lambadFuncAction(self):
        self.lambdaFunc1()
        self.lambdafilterMethod()
        self.innerLmabda()

    def lambdaFunc1(self):
        """ ''' def cube(self,x):
        return  x*x*x '''"""
        cube_v2 = lambda x: x * x * x # cube
        print("Cube of the Value",cube_v2(7))

        add_num = lambda a, b, c: a + b + c #sum
        print("Sum is {:.2f}".format(add_num(5.1344, 5, 5)))

        average = lambda a,b,c : a*b/c  #average
        print("Average of the numbers: ",average(10,10,2))

        add_num = (lambda a,b:a*b)(2,5) #passing argument
        print("Sum Using Passing Argument",add_num)

    def lambdafilterMethod(self):
        """Python has a built in filter() method which filter a collections(iterable) by using function
        syntax:->filter(function,iterable)"""
        thelist=[3,5,8,5,6,9,1,3,5,8,6,4]
        newlist =list(filter(lambda a:a%2 == 0,thelist)) # strore only even numbers in new list
        print("\nEven Number list is: ", newlist)

        thelist = [3,5,8,5,6,9,1,3,5,8,6,4] # return number greater than 4
        newlist = list(filter(lambda a:a>4, thelist))
        print("The list which number is greater than 4: ", newlist)

    def add_num(self,x):
        return lambda a:a+x

    def innerLmabda(self):
        """An example,usinglambda function inside a function"""
        print("\nInner Lambda example")
        my_num = self.add_num(5)
        print("Result of 4 is: ",my_num(4))
        print("Result of 5 is: ",my_num(5))
        print("Result of 6 is: ",my_num(6))





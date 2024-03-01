"""The yield statement suspends function’s execution and sends a value back to the caller, but retains enough
state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the
last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list."""

class YieldMethod:

    def yieldActions(self):
        self.yieldMethod1()


    def yieldMethod1(self):
        for num in self.yieldMethod11():
            if num > 100:
                break
            print(num,end =' ')

    def yieldMethod11(self):
        i = 1
        # An Infinite loop to generate squares
        while True:
            yield  i*1
            i += 1 # Next execution resumes from this point
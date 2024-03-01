import  heapq
from  collections import Counter
class CompetitiveCoding:

    def competitiveCodingActions(self):
        self.most_common()
        self.n_largest_smallest_in_heapq()
        self.zipMethod()
        self.mapMethod()


    def most_common(self): # Code to find top 3 elements and their counts
        print("1.Find top 3 elements and their counts")
        """This function analyses a list/string and helps to return the top n entities in the list/string according to their number
         of occurrences in descending order where n is a number that is specified by the programmer."""
        arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]
        counter = Counter(arr)
        top_three = counter.most_common(3)
        print(top_three)

    def n_largest_smallest_in_heapq(self): #Python code to find 3 largest and 4 smallest
        print("\n2.Python code to find 3 largest and 4 smallest")
        """This function helps to return the top n smallest/largest elements in any lists and here again n is a number specified by the programmer."""
        grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
        print(heapq.nlargest(3,grades))
        print(heapq.nsmallest(4,grades))

    def zipMethod(self):
        print("\n3.Python code to demonstrate use of zip.")
        stocks = {'Goog': 520.54,'FB': 76.45,'yhoo': 39.28,'AMZN': 306.21,'APPL': 99.76}
        zipped_1 = zip(stocks.values(),stocks.keys())
        print(sorted(zipped_1)) # sorting according to values
        zipped_2 = zip(stocks.keys(), stocks.values())
        print(sorted(zipped_2)) #sorting according to keys

    def double_money(self, dollars):
        return  dollars*2

    def mapMethod(self):
        print("\n4.Map Method")
        income = [10, 30, 75] # Python code to apply a function on a list
        new_income =  list(map(self.double_money,income))
        print(new_income)

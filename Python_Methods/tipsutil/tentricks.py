import  os
import  socket
import sys
from collections import Counter
class TenTricks:

    def tipsmethods(self):
        print("1.In-Place Swapping Of Two Numbers")
        x, y = 10,20
        print(x,y)
        x,y = y,x
        print(x,y)

        print("\n2.Reversing a string in python")
        a ="GeeksForGeeks"
        print("Reverse is",a[::-1])

        print("\n3.Create a single string from all the elements in list")
        a =["Geeks", "For", "Geeks"]
        print(" ".join(a))
        print('List by using join method: %s' % ', '.join(a))

        print("\n4.Chaining Of Comparison Operators.")
        n = 10
        result = 1 <n<20
        print(result)
        result = 1>n<=9
        print(result)

        print("\n5.Print The File Path Of Imported Modules.")
        print(os)
        print(socket)

        print("\n6.Use Of Enums In Python")
        print(MyName.Geek, " ", MyName.For, " ", MyName.Geeks)

        print("\n7.Return Multiple Values From Functions")
        a,b,c,d = MyName().x()
        print(a," ",b, " ",c," ",d)

        print("\n8.Find The Most Frequent Value In A List.")
        test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
        print(max(set(test),key=test.count))

        print("\n9.Check The Memory Usage Of An Object.")
        x = 1
        print(sys.getsizeof(x))

        print("\n10.Print string N times")
        n = 2
        a = "GeeksforGeeks"
        print(a*n)

        print("\n11.Checking if two words are anagrams")
        print(MyName().is_anagram('geek', 'eegk'))
        print(MyName().is_anagram('geek', 'peek'))



class MyName:
    Geek, For, Geeks = range(3)

    def x(self):
        return  1,2,3,5

    def is_anagram(self, str1,str2):
        return  Counter(str1) == Counter(str2)

    # or without having to import anything
    def is_anagram2(self,str1,str2):
        return  sorted(str1) == sorted(str2)


import itertools
class AmazingHacksMethod:

    def amazinghacksActions(self):

        print("1.Transpose a matrix")
        print("Using Nested List Comprehension")
        m = [[1, 2], [3, 4], [5, 6]]
        for row in m:
            print(row)
        rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        print("")
        for row in rez:
            print(row)

        print("\nUsing Zip")
        matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
        for row in matrix:
            print(row)
        print("")
        t_matrix = zip(*matrix)
        for row in t_matrix:
            print(row)

        """Explanation: [iter(geek)] * 2 produces a list containing 2 items of geek[] list, i.e. a list of length 2. 
        *arg unpacks a sequence into arguments for a function call. Therefore we are passing the same iterator 2 times to zip()."""

        print("2.Partition a list into N groups") #We used iter() as an iterator over a sequence
        geek = ['Sun', 'Flowers', 'Peoples', 'Animals', 'Day', 'Night']
        partition = list(zip(*[iter(geek)]*2))
        print(partition)

        print("\n3.Printing more than one list’s items simultaneously")
        list1 = [1, 3, 5, 7]
        list2 = [2, 4, 6, 8]

        for a,b in zip(list1,list2):
            print(a, b)

        print("\n4.Take the string as input and convert it into list:")
        #formatted_list = list(map(int, input().split()))
        #print(formatted_list)

        print("\n5.Convert list of list into single list")
        geek = [[1, 2], [3, 4], [5, 6]]
        # chain.from_iterable() function returns the elements of nested list and iterate from first list
        # of iterable till the last end of the list
        lst = list(itertools.chain.from_iterable(geek))
        print(lst)

        print("\n6.Printing the repeated characters") #Task is to print the pattern like this Geeeeekkkkss
        print("G" + "e" * 5 + "k" * 4 + "s" * 2) # + used for string concatenatio  To repeat the character n times, just multiply n  with that character  





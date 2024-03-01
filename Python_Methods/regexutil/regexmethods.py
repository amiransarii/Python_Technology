import  re
class RegularExpression:

    def regexOpertions(self):
        self.regexMethod1()
        self.regexSetPattern()
        self.regexFunctions()
        self.matchobjectFunction()

    def regexMethod1(self):
        print("Regular Expression Example1 ")
        txt =" Hello World"
        pattern = re.findall("o",txt) # search for lower letter
        for match in pattern:
            print(match, end =' ')
        print()

    def regexSetPattern(self):
        """The set is used to define a set of characters in search patten put "[A-Z]"  define set using []"""
        print("\nSet Pattern")
        txt ="23 of November 86"
        pattern = re.findall("[0-9]",txt) # Search for number 0 to 9
        print("Digits are: ",end =' ')
        for match in  pattern:
            print( match, end =' ')

        print()
        print("All Capital Letters are : ", end =' ')
        txt ="TodDay IS a grEAT day"
        pattern = re.findall("[A-Z]",txt) # Search for capital letters
        for match in pattern:
            print(match, end =' ')


    def regexFunctions(self):
        print("\n Regex Functions")
        txt = "Beautifulday,Beautiful life"
        patten = re.findall("au",txt) #This method return a list of all matches found in the string by their order
        print(patten) #['au','au']

        txt ="Beautiful,Beautiful,Beautiful"
        pattern = re.search("au",txt) #This function searches for the first natch in the string and returns a match object
        #if there was a match, and None if there was no match
        print(pattern)

        pattern = re.split("au",txt,2) # This function returns a list containing the string splitted on defined patten, number of occurance
        print(pattern) #['Be', 'tiful,Be', 'tiful,Beautiful']

        txt = "Belltiful,Belltiful"
        pattern = re.sub("||","au",txt,1) #This function replace the found match with the given text by user, also can specify number of replacement
        print(pattern)


    def matchobjectFunction(self):
        print("\nMatch Object Function")
        txt ="Beautiful Day"
        pattern = re.search(r"Day",txt)
        print(pattern.span())  # Return the location of start position and the end position(indexes) of first match

        txt ="Today was a beautiful day"
        patten = re.search(r"\b\b\w+",txt)
        print(patten.group()) # Return a part of the string where the match occurred

        patten = re.search(r"\bb\w+",txt)
        print(patten.string)  #Returns  the string which is passed to the function








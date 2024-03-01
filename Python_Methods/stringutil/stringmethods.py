import keyword

from stringutil import stringformatmethods


class StringMethods:

    def stringOperations(self):
        print("String Methods are: ")
        mstr ="Welcome World"
        print(mstr.capitalize()) #Welcome world -Return a capitalized version of the string.
        print(mstr.casefold()) #welcome world ->Return a version of the string suitable for caseless comparisons.
        print(mstr.center(20,"Z")) #ZZZwelcome WorldZZZZ ->Return a centered string of length width. Padding is done using the specified fill character (default is a space)
        print(mstr.count("o"),mstr[5:].count("o")) #2 1 ->Return the number of non-overlapping
        print(mstr.encode('utf-8',errors='strict')) #b'welcome World' -> Encode the string using the codec registered for encoding.
        print(mstr.endswith("d")," and using slice",mstr.endswith("e",0,7)) #True  and using slice True -Return True if  ends with given string
        print(mstr.expandtabs(200)) # Return a copy where all tab characters are expanded using spaces
        print(mstr.find("o"), mstr[8:].find("o")) #4 1 -> Return the lowest index in S where substring sub is found
        print("My Name is {} and a {}".format("Amir Ansari","Software Engineer"))
        print("I am a {1} and name is {0}".format("Amir Ansari", "Software Engineer"))
        print(mstr.index("o"), mstr[8:].index("o")) #4 1 ->  Raises ValueError when the substring is not found.
        print(mstr.isalnum()) #False(as it is containing space)
        print(mstr.isalpha()) #False(as it is containing space)
        print(mstr.isascii()) #True ->Return True if all characters in the string are ASCII, False otherwise
        print("1234".isdecimal()) #Return True if the string is a decimal string, False otherwise
        print("120".isdigit()) #Return True if the string is a digit string, False otherwise
        print("abc".isidentifier()) #True->Return True if the string is a valid Python identifier
        print(keyword.iskeyword("if")) #Call to test whether string s is a reserved identifier, such as "def" or "class".
        print("abc".islower()) #Return True if the string is a lowercase string, False otherwise
        print("1050".isnumeric()) #Return True if the string is a numeric string, False otherwise.
        print("20".isprintable()) #Return True if the string is printable, False otherwise.
        print(repr(mstr)) #'welcome World'-repr() or if it is empty.
        print(" ".isspace()) #True -Return True if the string is a whitespace string, False otherwise.
        print(mstr.istitle()) #True -Return True if the string is a title-cased string, False otherwise.
        print("AMIR".isupper()) #True-Return True if the string is an uppercase string, False otherwise.
        print("-".join(["Amir","Akil","Azmi"])) #Amir-Akil-Azmi
        print(mstr.ljust(20,"@")) #Return a left-justified string of length width. Padding is done using the specified fill character
        print(mstr.lower()) #Return a copy of the string converted to lowercase. mstr.lower()
        print(mstr.lstrip("$")) #Return a copy of the string with leading whitespace removed.
        print("amir-akil-azmi-zeeshan".partition("-")) #Partition the string into three parts using the given separator.
        print("amir-akil-azmi".removeprefix("am")) #ir-akil-azmi- Return a str with the given prefix string removed if present
        print("amir-akil-azmi".removesuffix("mi")) #amir-akil-az -Return a str with the given suffix string removed if present.
        print(mstr[1:4]) #Otherwise, return a copy of the originalstring.
        print(mstr.replace("World","Byee",1)) #Return a copy with all occurrences of substring old
        print(mstr.rfind("o"),mstr.rfind("o",5,-1)) #Return the highest index in S where substring
        print("Indexes are ",mstr.rindex("o"), mstr.rindex("o",1,5))
        print(mstr.rjust(30,"$")) #Return a right-justified string of length width
        print("amir@akil$zeeshan@azmi$Hello".rpartition("$"))
        print("Hello@Amir@Ansari".rsplit("@",1)) #Return a list of the words in the string, using sep  count 1
        print("Amir Ansari Akil Zeeshan                    ".rstrip()) #Return a copy of the string with trailing whitespace removed.
        print("amir-akil-zeeshan-azmi".split("-")) # Return a list of the lines in the string, breaking at line
        print("amir".startswith("am"),"am".startswith("am",1,5)) #Return True if S starts with the specified prefix
        print(" amir ansari akil zeeshan ".strip())
        print("amir".swapcase()) #AMIR -Convert uppercase characters to lowercase and lowercase characters to uppercase
        print("amir ansari".title()) #Amir - Return a version of the string where each word is titlecased
        #print("amir".translate(100,200)) #Replace each character in the string using the given translation table
        print("amir".upper()) #Return a copy of the string converted to uppercase
        print("amir".zfill(10)) #Return a copy of the string converted to uppercase
        #print("amir".maketrans(10)) #Return a translation table usable for str.translate()

        stringformatmethods.StringFormat().stringformatOperations()







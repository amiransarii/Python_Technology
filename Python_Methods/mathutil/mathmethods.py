import  math
class MathMethod:
    def matchconverter(self):
        # convert float value at decimal place, and store it in string format
        a_float = 3.14159
        formatted_float = "{:.2f}".format(a_float)
        print(formatted_float) #3.14

        #print("\n")
        a_float = 13.949999999999999
        print("%.2f" %round(a_float,2)) #13.95

        a_float = 13.95
        print("{:.15f}".format(round(a_float, 2))) #13.949999999999999

        a_float = 12.16785
        print("The value of number is: ", end="")
        print(math.trunc(a_float)) #12

        ''' 1-> 3.1415926	{:.2f}	3.14	Format float 2 decimal places
            2-> 3.1415926	{:+.2f}	+3.14	Format float 2 decimal places with sign
            3-> -1	{:+.2f}	-1.00	Format float 2 decimal places with sign
            4->  2.71828	{:.0f}	3	Format float with no decimal places
            5 -> 5	{:0>2d}	05	Pad number with zeros (left padding, width 2)
            6->  5	{:x<4d}	5xxx	Pad number with x’s (right padding, width 4)
            7->  10	{:x<4d}	10xx	Pad number with x’s (right padding, width 4)
            8->  1000000	{:,}	1,000,000	Number format with comma separator
            9->  0.25	{:.2%}	25.00%	Format percentage
            10-> 1000000000	{:.2e}	1.00e+09	Exponent notation
            11-> 13	{:10d}	        13	Right aligned (default, width 10)
            12-> 13	{:<10d}	13	Left aligned (width 10)
            13-> 13	{:^10d}	    13	Center aligned (width 10)'''
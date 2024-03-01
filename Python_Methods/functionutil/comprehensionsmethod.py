class ComprehensionsMethod:
    def comprehensionsAction(self):
        self.listcomprehensions()


    def listcomprehensions(self):
        cars = ["Benz","BMW","Toyota","Honda","Ford"]
        newlist = [car for car in cars if "a" in car]
        print("\nUsing List Comprehension First ", newlist)

        newlist = [a for a in range(12)] # create a list using range
        print("List Creation using List",newlist)

        newlist =[car.upper() for car in cars] # change all outcome to upper case
        print("UpperCase Car Names",newlist)

        newlist = [car if car !="BMW" else "Jeep" for car in cars] # if else Jeep
        print("Using If Else Statement ",newlist)






from tipsutil import  tentricks
from tipsutil import  amazinghacksmethod
from  tipsutil import factmethods
from  tipsutil import  competitivecoding

class TipsMethod:
    def tipsActions(self):
        choice = int(input("1.10Tricks 2.amazinghacksmethod 3.factmethod  4.CompetitiveCoding :"))
        if choice == 1:
            tentricks.TenTricks().tipsmethods()
        elif choice == 2:
            amazinghacksmethod.AmazingHacksMethod().amazinghacksActions()
        elif choice == 3:
            factmethods.FactMethod().factActions()
        elif choice == 4:
            competitivecoding.CompetitiveCoding().competitiveCodingActions()



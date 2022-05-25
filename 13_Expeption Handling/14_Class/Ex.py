class GetMarraySoon:
    def __init__(self,args):
        self.msg = args


age = int(input("Your age : "))

if age>25:
    print("Eligible for marriage")
else:
    raise GetMarraySoon ("Not eligible for marriage")
print("HELLOOOOOO")
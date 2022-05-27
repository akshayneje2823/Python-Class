class Bank:
    def __init__(self,bankName,city):
        self.bankName =  bankName           # these are instance variables
        self.bankAdress = city              # these are instance variables

    def getAccount(self,name):
        self.myName = name                  # these are instance variables
        print("The Bank Is "+ self.bankName + " Bank")
        print("In"+self.bankAdress + " You will get bank")
        print("Account holder is Mr. "+ self.myName)

otp = Bank("HDFC","Maratahalli")

otp2 = Bank("HDFC","Maratahalli")

otp.getAccount("Joe tribiyani")
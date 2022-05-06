def empDetails(fname,lname):
    print(fname + " " + lname)

empDetails("Akshay", "Neje")


def Akshay(*kids):
    print(kids[1] + " is son of Akshay.")

Akshay("Monika","Dev","Ankit")


def Dev(state = "Maharashtra"):
    print("He is from " + state +"." )

Dev()
Dev("Karnataka")
Dev("Madhya Pardesh")
Dev("Gujrat")
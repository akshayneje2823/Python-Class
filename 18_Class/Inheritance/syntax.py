# Parent Class

class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
    
    def printName(self):
        print(self.firstName,self.lastName)

# x = Person("Akshay","Neje")
# print(x.__dict__)
# x.printName()


# Child Class

class Student(Person):
   def __init__(self, fname, lname):
       super().__init__(fname, lname)
       self.educationYear = 2019
       print("My name is " + self.firstName + self.lname +".")

x = Student("Mike","Tribbiani")
print(x.__dict__)
x.printName()
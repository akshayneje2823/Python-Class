# ?Example 1
class its_Constructor:
    def __init__(self,name,age,city):
        self.name= name
        self.age = age
        self.city = city

    def myFun(self):
        print("Hello this is "+ self.name + ". I am from "+self.city)

p1 = its_Constructor("Akshay",22,"Kolhapur")
p1.myFun()



# Example 2

class Person:
    def __init__(person,name,city):
        person.name = name
        person.city = city
    
    def myFun(person):
        print("Hello Thi is " + person.name +". I am from " + person.city)


p2 = Person("Darshan","Delhi")
p2.myFun()
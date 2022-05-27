class Person:
    def __init__(self,name):
        self.name = name
    
    def myFunc(self):
        print("Hello this is " + self.name)

p1 = Person("Akshay")
p1.age = 40
print(p1.age)

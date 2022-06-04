class Parent():
    def __init__(self,name):
        self.name =name

    def getName(self):
        return self.name

class Child(Parent):
    def __init__(self, name,age):
        Parent().__init__(self,name)
        self.age = age
    
    def getAge(self):
        return self.age

# class GrandChild(Child):
#     def __init__(self, name, age,location):
#         Child().__init__(name, age)
#         self.location = location
    
#     def getLocation(self):
#         return self.location

GC = Child("Akshay",23,)
print(GC.getName().GC.getAge())

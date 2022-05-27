from unicodedata import name


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myFun(self):
        print("Hello This Is" + self.name)

p1 = Person("AKshay",22)
print(p1)

p2 = Person("AKshay",22)
print(p2)



# Delete

print(p1)
del p1                  # will get error because we already deleted

print(p1)

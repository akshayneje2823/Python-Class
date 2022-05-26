
# class Employee:
#     def __init__(self,id,name,sal):
#         self.eid = id
#         self.ename=name
#         self.esal = sal
    
# e1=Employee(101,"Rahul", 45000)
# print(e1)
# print(e1.__dict__)
    
from queue import Full


class Fullname:
    def __init__(self,a,b):
        self.firstName = a
        self.lastName = b

r = Fullname("Akshay","Neje")
print(r)
print(r.__dict__)      # Return in key value pairs

# A variable is only avialable from inside the region it is created.This is called scope.

# LOCAL SCOPE:
from re import X


def myFunc():
    x = 90
    print(x)

myFunc()

# GLOBAL SCOPE:
x = 300
def myFunc2():
    print(x)

myFunc2()
print(x)
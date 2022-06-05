def myFun(x):
    return len(x)


x = map(myFun, (12, 34, 56, 78, 98))

print(x)
print(list(x))
print("Akshay")


def myfun(a, b):
    return a+b


# def myfun(1,2)    ==>   We are passing two arguments one as function other as sequence

x = map(myfun, ('apple', 'banana', 'cherry'), (" APPLE", " BANANA", " CHERY"))    # In Pyrhon everything is object so we have to convert list
print(list(x))

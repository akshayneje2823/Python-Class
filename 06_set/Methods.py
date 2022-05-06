langName = {"Java","Python","C","C++","#","Javascript","React","R-lan",""}

# langName.add(100)
# print(langName)

# langName.clear()
# print(langName)          # Remvoes all elements from the set

x =langName.copy()        # copy as it is
print(x)

x.pop()
print(x)


x.remove("Javascript")
print(x)


dataBase = {101,102,103,104}
x.update(dataBase)
print(x)
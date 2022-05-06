langName = {"Java","C","C++","#","Javascript","Python"}

# langName.remove("C")             # ==> Remoes specific elements
# print(langName)

# langName.discard("Python")         
langName.discard("Py")             # It wont no throw error
print(langName)


langName.pop()                     # it eill remove randomly item
print(langName)


del langName
print(langName)

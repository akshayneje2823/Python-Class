# numbers = {1,2,4,56,7,12}
# numbers.add("num")
# print(numbers)

# set1 = {"apple", "banana", "cherry"}
# set2 = {1,2,4,56,7,12}
# set2.update(set1)
# print(set2)

# empName = {"Java","Python","Java","C","C++","#","Javascript","Python"}
# empName.update()  # ==> Removes duplictes elements
# print(empName)


s = {10}
l1 =[20]
l2 =[30]

s.update(l1,l2,range(6))
print(s)
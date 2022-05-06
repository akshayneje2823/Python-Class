name = ["List","Append","Insert","Extends"]

name.append("python")    # ==> Appends last of the list
print(name)


id = [101,102,103,104]

id.insert(0,"Nothing")    # ==> Expects Two argumnets first one should be index number and another should br value
print(id)


empId = [101,102,103,104]
empName = ["List","Append","Insert","Extends"]
empName.extend(empId)
print(empName)


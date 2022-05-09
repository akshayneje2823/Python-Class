def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)
        
result = fact(5)
print(result)

result1 = fact(7)
print(result1)
from unittest import result


num = 4

def fact(num):
    result = 1
    while num > 1:
        result = result*num
        num = num -1

    return result

print(fact(4))
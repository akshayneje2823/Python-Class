# Tuple
myTuple = ("Iterator","Iterable","Both","Different") # tuple

myit = iter(myTuple)     #<tuple_iterator object at 0x00000249B4DB7D60>

print(myit)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



# String
myStr = "Akshay"          # <str_iterator object at 0x000001F08B17FBE0>

myItr = iter(myStr)        
print(myItr)
print(next(myItr))
print(next(myItr))
print(next(myItr))
print(next(myItr))
print(next(myItr))
print(next(myItr))
print('')

something = "Itearator"
for x in something:
    print(x)
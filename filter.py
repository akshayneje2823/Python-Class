from msilib import sequence
from unittest import result


# Filter :
#         if want to filter the sequence based 
#         on true or false then we use filter method



# Print first 10 even number using filter function
print(list(filter(lambda x: x%2 ==0,range(0,21))))




# Print first 10 0dd number using filter function
print(list(filter(lambda x: x%2 !=0,range(0,21))))

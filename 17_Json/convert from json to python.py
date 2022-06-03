import json

# Some json

x = '{"name":"Akshay","age":22,,"city":"New York"}'


#  the result  is a python dictionary:
y = json.loads(x)
print(y["age"])
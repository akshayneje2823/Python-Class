
buyCar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(buyCar)

buyCar["origin"] = "Germany"
print(buyCar)

# Update

buyCar.update({"year":1999})
print(buyCar)

buyCar["color"] = "red"
print(buyCar)
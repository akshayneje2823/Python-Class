f = open("sample.txt","a")
f.write(" Now we can write")
f.close()

# ope and read the file after appending
f = open("sample.txt","r")
print(f.read())


# Self parctice
f = open("akshay.txt","a")
f.write("Woops! I have created another file")
f.close()

check = open("akshay.txt","r")
print(check.read())

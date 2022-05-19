f = open("lets_check.txt","w")
f.write("I want to check")
f.close()


# we have to open trigger and read operator the we can read the file
f = open("lets_check.txt","r")
print(f.read())

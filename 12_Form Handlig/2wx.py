f = open("sample.txt","a")
f.write("Now we can erite")
f.close()

f =open("sample.txt","r")
print(f.read())
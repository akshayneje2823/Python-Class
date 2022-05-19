# import os
# os.remove("myfile.txt")






# already created file here i want to delete this file

f = open("name.txt","x")


# Check if File exist:

import os 
if os.path.exists("name.txt"):
    os.remove("name.txt")
else:
    print("File odesnt exist")
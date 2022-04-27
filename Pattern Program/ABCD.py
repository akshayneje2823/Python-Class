'''
Print ABCD in given type
A B C D
A B C D
A B C D
A B C D

'''

for i in range(1,5):
    for j in range(1,5):
        print(chr(64 + j), end=" ")
    print()
''' 
Print ABCD in given type

A  A  A  A 
B  B  B  B 
C  C  C  C
D  D  D  D
E  E  E  E
F  F  F  F
G  G  G  G

'''

from turtle import end_fill


for i in range(1,8):
    for j in range(1,8):
        print(chr(64+j), end="  ")
    print() 

from array import *

arr = array('i',[])
n = int(input("Enter how many value you went to add ? :"))

for x in range(n):
    val = int(input("Enter next value :"))
    arr.append(val)



print(arr)

var = int(input("Enter the number what your went to search :"))
k = 0
for e in arr:
    if e==var:
        print("The Indext Number is :",k)

    k += 1

print("The Index Numebr is :",arr.index(var))





from array import*

arr = array('i',[])
val = int(input("How many element yout went to add :"))

for x in range(val):
    ele = int(input("Enter The Element Number :"))
    arr.append(ele)

print(arr)

search = int(input("What Element You Went To Search :"))
ind = 0
for y in arr:
    if y == search:
        print()

print("The Index Number is :",arr.index(y))

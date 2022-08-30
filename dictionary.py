
dict = {

}

n = int(input("how many element you went to add :"))

for x in range(n):
    roll = int(input("Enter Your Roll :"))
    name = input("Enter Your Name :")

    dict [roll] = name

print(dict)


search = int(input("Enter The Roll For Search :"))
for y in dict:
    if search == dict.items():

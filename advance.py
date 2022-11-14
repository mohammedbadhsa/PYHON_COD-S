"""
a = input("Enter the value of a :")
a = int(a)
if a > 9:
    print("A is gaterthen 9 ")

else:
    print("A is not gaterthen you enter the value!")

#enumerate

list1 = ["moahmmed badsha",483017,"jibon rohoman","3.15244"]

list1 = [ "mohammed badsha",483017,"the time to do ture from man",3.55]
for item in list1:
    print(list1)

books = ["bangla","english","math","physic","chemistry"]

for index,item in enumerate(books):
    print(index,item)
"""

#--> Creating a enumerate list on python! enumerate holo amon akta podoti jekane for loop ar maje enumerate use
#kore list a thaka index_number and item aksate print kora jay ...!

mes_members = ["M.Badsha","M.Hamim","M.Abdullah","M.Moniruzzaman","M.Jubayed",]

for index,item in enumerate(mes_members):
    print(index,item)
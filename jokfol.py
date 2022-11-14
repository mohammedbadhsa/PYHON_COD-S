
class area:

    x = ""
    y = ""

    def __init__(self,x,y):
        self.Roll = x
        self.Name = y

    def val(self):
        print(f"Student Roll :{self.Roll}\nStudent Nmame:{self.Name}")

ob1 = area(483017,"Mohammed Badsha\n")
ob2 = area(483021,"jibon\n")
ob3 = area(483017,"Durjoy Vai\n")
ob4 = area(483017,"Mohammed Hamim")
ob1.val()
ob2.val()
ob3.val()
ob4.val()

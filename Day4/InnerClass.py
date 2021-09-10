class BE_first_year:
    def __init__(self):
        self.collage_name = "YCCE"
        self.branch_name = "EE"
        self.objsem = self.FirstSem()
    
    def display(self):
        print("College Name = ", self.collage_name)
        print("Branch Name = ", self.branch_name)
    

    class FirstSem:
        def __init__(self):
            self.sub1 = "M1"
            self.sub2 = "Phy"
            self.sub3 = "Chem"
            self.sub4 = "Eng"
            self.sub5 = "C - Language"

        def show(self):
            print("subject1 = " , self.sub1)
            print("subject2 = " , self.sub2)
            print("subject3 = " , self.sub3)
            print("subject4 = " , self.sub4)
            print("subject5 = " , self.sub5)


obj = BE_first_year()
obj.display()
objsem = obj.objsem
objsem.show()


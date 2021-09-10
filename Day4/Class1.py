class Student:
    rollno = 155
    maths = 80
    phy = 90
    che = 70
    eng = 99

    def add(self):
        print(self.maths+self.phy+self.che+self.eng)
    
    def mul(self):
        print(self.maths*self.phy*self.che*self.eng)
    
    def div(self):
        print(self.maths/self.phy/self.che/self.eng)
        
    def sub (self):
        print(self.maths-self.phy-self.che-self.eng)

obj = Student()
obj.div()
print(obj.rollno)



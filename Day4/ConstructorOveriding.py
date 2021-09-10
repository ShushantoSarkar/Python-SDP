class Father:
    def __init__(self):
        print('Father: = I am on time at breakfast table')
    
class Child (Father):
    def __init__(self):
        print("Child: = I will be late for breakfast")


obj = Child()
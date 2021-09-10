class Faculty:
    def __init__ ( self, f_name, department, f_id):
        self.f_name = f_name
        self.dpartment = department
        self.f_id = f_id

    def print_info(self):
        print("faculty information = ", self.f_name, self.dpartment, self.f_id)

    
class EE(Faculty):
    pass

obj = EE("Shushanto", "EE", 155)
obj.print_info()
from company_component import CompanyComponent

class Department(CompanyComponent):
    
    def __init__(self, name):
        self.name = name
        self.sub_employee = list()
    
    def add(self, component):
        self.sub_employee.append(component)
    
    def print_info(self, level):
        print(level*"+", self.name, ', with SubEmployee : { ')
        for component in self.sub_employee:
            component.print_info(level+1)
        print('}')
        



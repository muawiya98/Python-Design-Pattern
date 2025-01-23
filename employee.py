from company_component import CompanyComponent
class Employee(CompanyComponent):
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self, level):
        print(level*"-", f"Name :: {self.name}, with salary :: {self.salary}")
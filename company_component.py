from abc import ABC

class CompanyComponent(ABC):

    def print_info(self, level):pass
    
    def add(self):raise Exception("Unimplemented Method")
        
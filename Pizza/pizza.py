from abc import ABC

class Pizza(ABC):
    def __init__(self):
        self.name=""
        self.dough=""
        self.sauce=""
        self.toppings=[]
    
    def get_name(self):
        return self.name
    
    def prepare(self):
        print(f"Preparing : {self.name}")

    def bake(self):
        print(f"Baking : {self.name}")

    def cut(self):
        print(f"Cutting : {self.name}")

    def box(self):
        print(f"Boxing : {self.name}")

    def __str__(self) -> str:
        print(5*"-", self.name, 5*"-")
        print(self.dough)
        print(self.sauce)
        for topping in self.toppings:
            print(topping)
        return super().__str__()
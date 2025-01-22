from abc import ABC

class Pizza(ABC):
    def __init__(self):
        self.name=None
        self.dough=None
        self.sauce=None
        self.cheese=None
        self.clam=None
        self.pepperoni = None
        self.toppings=[]
    
    def get_name(self):
        return self.name
    
    def prepare(self):pass

    def bake(self):
        print(f"Baking : {self.name}")

    def cut(self):
        print(f"Cutting : {self.name}")

    def box(self):
        print(f"Boxing : {self.name}")

    def __str__(self) -> str:
        print(5*"-", self.name, 5*"-")
        
        if self.dough!=None:print(self.dough)
        if self.sauce!=None:print(self.sauce)
        if self.cheese!=None:print(self.cheese)
        if self.clam!=None:print(self.clam)
        if self.pepperoni!=None:print(self.pepperoni)
        if self.toppings!=[]:        
            for topping in self.toppings:
                print(topping)
        return super().__str__()
from Pizza.pizza import Pizza

class ClamPizza(Pizza):

    def __init__(self, ingredient_factory):
        super().__init__()
        self.name="Chicago Clam Pizza"
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        print(f"Preparing : {self.name}")
        self.dough = self.ingredient_factory.createDough()
        self.sauce =self.ingredient_factory.createSauce()
        self.calm = self.ingredient_factory.createClam()

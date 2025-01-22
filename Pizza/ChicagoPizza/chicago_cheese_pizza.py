from Pizza.pizza import Pizza

class CheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        super().__init__()
        self.name="Chicago Cheese Pizza"
        self.ingredient_factory = ingredient_factory
    
    def prepare(self):
        print(f"Preparing : {self.name}")
        self.dough = self.ingredient_factory.createDough()
        self.sauce =self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()


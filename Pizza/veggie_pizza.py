from Pizza.pizza import Pizza

class VeggiePizza(Pizza):

    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory
        self.name="Veggie Pizza"

    def prepare(self):
        print(f"Preparing : {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce =self.ingredient_factory.create_sauce()
        self.veggies = self.ingredient_factory.create_veggies()

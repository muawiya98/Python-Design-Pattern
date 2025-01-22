from Pizza.pizza import Pizza

class ClamPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="NY Clam Pizza"
        self.dough="Thin Crust"
        self.sauce="White gralic Sauce"
        self.toppings.append("Grated parmesan cheese")
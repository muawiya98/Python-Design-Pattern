from Pizza.pizza import Pizza

class ClamPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="Chicago Clam Pizza"
        self.dough="Thik Crust"
        self.sauce="Gralic Sauce"
        self.toppings.append("Grated parmesan cheese")
        self.toppings.append("Mozzella")

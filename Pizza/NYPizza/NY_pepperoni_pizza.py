from Pizza.pizza import Pizza

class PepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="NY Pepperoni Pizza"
        self.dough="Crust"
        self.sauce="Marinara sauce"
        self.toppings.append("Pepperoni")
        self.toppings.append("Sliced paramesan cheese")

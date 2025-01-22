from Pizza.pizza import Pizza

class PepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="Chicago Pepperoni Pizza"
        self.dough="Thin Crust"
        self.sauce="Marinara sauce"
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Sliced paramesan cheese")

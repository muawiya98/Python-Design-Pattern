from Pizza.pizza import Pizza

class CheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="Chicago Cheese Pizza"
        self.dough="IRRegular Crust"
        self.sauce="Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzella")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Parmesan")
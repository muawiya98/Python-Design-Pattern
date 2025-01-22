from Pizza.Pizza import Pizza

class CheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="Cheese Pizza"
        self.dough="Regular Crust"
        self.sauce="Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzella")
        self.toppings.append("Parmesan")
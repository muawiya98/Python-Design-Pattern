from Pizza.pizza import Pizza

class CheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="NY Cheese Pizza"
        self.dough="Regular Crust"
        self.sauce="Marinara Pizza Sauce"
        self.toppings.append("Cheese")
        self.toppings.append("Parmesan")
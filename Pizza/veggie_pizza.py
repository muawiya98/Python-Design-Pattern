from Pizza.Pizza import Pizza

class VeggiePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name="Veggie Pizza"
        self.dough="Crust"
        self.sauce="Marinara Sauce"
        self.toppings.append("Shredded mozzarella")
        self.toppings.append("Grated parmesan")
        self.toppings.append("Diced onion")
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced red pepper")
        self.toppings.append("Sliced black olives")


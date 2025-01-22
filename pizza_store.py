class PizzaStore:

    def __init__(self, pizza_factory):
        self.pizza_factory = pizza_factory


    def order_pizza(self, type=...):
        pizza = self.pizza_factory.creat_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
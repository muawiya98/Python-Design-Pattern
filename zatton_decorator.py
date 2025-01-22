from topping_decorator import ToppingDecorator
class ZattomDecorator(ToppingDecorator):

    def __init__(self, given_pizza):
        self.given_pizza = given_pizza

    def get_description(self):
        return self.given_pizza.get_description() + ", zatton"
    
    def get_cost(self):
        return self.given_pizza.get_cost() + 1

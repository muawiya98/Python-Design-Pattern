from mozarilla_decorator import MozarillaDecorator
from zatton_decorator import ZattomDecorator
from plain_pizza import PlainPizza

class PizzaBuilder:
    def __init__(self):
        self.temp_pizza = PlainPizza()
    
    def add_mozarilla(self):
        self.temp_pizza = MozarillaDecorator(self.temp_pizza)
        return self

    def add_zatton(self):
        self.temp_pizza = ZattomDecorator(self.temp_pizza)
        return self
    
    def build_pizza(self):
        toreturn = self.temp_pizza
        self.temp_pizza = PlainPizza()
        return toreturn 
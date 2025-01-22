from Pizza.cheese_pizza import CheesePizza
from Pizza.clam_piazza import ClamPizza
from Pizza.pepperoni_pizza import PepperoniPizza
from PizzaFactory.pizza_factory import PizzaFactory
from Pizza.veggie_pizza import VeggiePizza
import random

class RandomOnePizzaFactory(PizzaFactory):
    
    def creat_pizza(self, my_type=...):
        pizza = None
        random_number = random.randint(0, 11)
        if random_number==0:
            pizza=CheesePizza()
        elif random_number==1:
            pizza=PepperoniPizza()
        else:
            pizza=VeggiePizza()
        return pizza
        
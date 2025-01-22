from Pizza.cheese_pizza import CheesePizza
from Pizza.clam_piazza import ClamPizza
from Pizza.pepperoni_pizza import PepperoniPizza
from PizzaFactory.pizza_factory import PizzaFactory
from Pizza.veggie_pizza import VeggiePizza

class SimplePizzaFactory(PizzaFactory):
    
    def creat_pizza(self, my_type=...):
        pizza = None
        if (type(my_type) is list) and (len(my_type)>=1):
            my_type=my_type[0]
        if my_type=="cheese":
            pizza=CheesePizza()
        elif my_type=="pepperoni":
            pizza=PepperoniPizza()
        elif my_type=="clam":
            pizza=ClamPizza()
        elif my_type=="veggie":
            pizza=VeggiePizza()
        return pizza
        
from Pizza.NYPizza.NY_cheese_pizza import CheesePizza
from Pizza.NYPizza.NY_clam_piazza import ClamPizza
from Pizza.NYPizza.NY_pepperoni_pizza import PepperoniPizza
from PizzaStoreFactory.pizza_store_factory import PizzaStoreFactory
from Pizza.veggie_pizza import VeggiePizza

class NYPizzaStore(PizzaStoreFactory):
    
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
        
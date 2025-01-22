from Pizza.NYPizza.NY_cheese_pizza import CheesePizza
from Pizza.NYPizza.NY_clam_piazza import ClamPizza
from Pizza.NYPizza.NY_pepperoni_pizza import PepperoniPizza
from PizzaStoreFactory.pizza_store_factory import PizzaStoreFactory
from Pizza.veggie_pizza import VeggiePizza
from PizzaIngredientFactory.NY_pizza_ingredient_factory import ChicagoPizzaIngredientFactory

class NYPizzaStore(PizzaStoreFactory):
    
    def creat_pizza(self, my_type=...):
        pizza = None
        NY_ingredient_factory = ChicagoPizzaIngredientFactory()
        if (type(my_type) is list) and (len(my_type)>=1):
            my_type=my_type[0]
        if my_type=="cheese":
            pizza=CheesePizza(NY_ingredient_factory)
        elif my_type=="pepperoni":
            pizza=PepperoniPizza(NY_ingredient_factory)
        elif my_type=="clam":
            pizza=ClamPizza(NY_ingredient_factory)
        elif my_type=="veggie":
            pizza=VeggiePizza(NY_ingredient_factory)
        return pizza
        
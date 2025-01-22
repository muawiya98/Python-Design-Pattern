from Pizza.ChicagoPizza.chicago_cheese_pizza import CheesePizza
from Pizza.ChicagoPizza.chicago_clam_piazza import ClamPizza
from Pizza.ChicagoPizza.chicago_pepperoni_pizza import PepperoniPizza
from PizzaStoreFactory.pizza_store_factory import PizzaStoreFactory
from Pizza.veggie_pizza import VeggiePizza
from PizzaIngredientFactory.chicago_pizza_ingredient_factory import ChicagoPizzaIngredientFactory

class ChicagoPizzaStore(PizzaStoreFactory):
    
    def creat_pizza(self, my_type=...):
        pizza = None
        chicago_ingredient_factory = ChicagoPizzaIngredientFactory()
        if (type(my_type) is list) and (len(my_type)>=1):
            my_type=my_type[0]
        if my_type=="cheese":
            pizza=CheesePizza(chicago_ingredient_factory)
        elif my_type=="pepperoni":
            pizza=PepperoniPizza(chicago_ingredient_factory)
        elif my_type=="clam":
            pizza=ClamPizza(chicago_ingredient_factory)
        elif my_type=="veggie":
            pizza=VeggiePizza(chicago_ingredient_factory)
        return pizza
        
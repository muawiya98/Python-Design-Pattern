from PizzaIngredientFactory.pizza_ingredient_factory import PizzaIngredientFactory
from PizzaIngedients.Dough.thin_crust_dough import ThinCrustDough
from PizzaIngedients.Sauce.marinara_sause import MarinaraSauce
from PizzaIngedients.Cheeses.reggiano_cheese import ReggianoCheese
from PizzaIngedients.Veggies.black_olives import BlackOlives
from PizzaIngedients.Veggies.onion import Onion 
from PizzaIngedients.Veggies.spinach import Spinach
from PizzaIngedients.Pepperoni.red_pepperoni import RedPepperoni
from PizzaIngedients.Clams.clam import Clam


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()
    
    def create_sauce(self):
        return MarinaraSauce()
    
    def create_cheese(self):
        return ReggianoCheese()
    
    def create_veggies(self):
        return [Spinach(), BlackOlives(), Onion()]
    
    def create_pepperoni(self):
        return RedPepperoni()
    
    def create_clam(self):
        return Clam()
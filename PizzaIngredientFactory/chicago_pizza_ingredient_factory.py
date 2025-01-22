from PizzaIngredientFactory.pizza_ingredient_factory import PizzaIngredientFactory
from PizzaIngedients.Dough.thick_crust_dough import ThickCrustDough
from PizzaIngedients.Sauce.plum_tomato_sause import PlumTomatoSause
from PizzaIngedients.Cheeses.mozzarella_cheese import MozzarellaCheese
from PizzaIngedients.Veggies.black_olives import BlackOlives
from PizzaIngedients.Veggies.eggplant import Eggplant 
from PizzaIngedients.Veggies.spinach import Spinach
from PizzaIngedients.Pepperoni.sliced_pepproni import SlicedPepproni
from PizzaIngedients.Clams.clam import Clam


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()
    
    def create_sauce(self):
        return PlumTomatoSause()
    
    def create_cheese(self):
        return MozzarellaCheese()
    
    def create_veggies(self):
        return [BlackOlives(), Eggplant(), Spinach()]
    
    def create_pepperoni(self):
        return SlicedPepproni()
    
    def create_clam(self):
        return Clam()
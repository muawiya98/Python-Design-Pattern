from abc import ABC, abstractmethod

class PizzaStoreFactory(ABC):
    
    def order_pizza(self, type=...):
        pizza = self.creat_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
    
    @abstractmethod
    def creat_pizza(self, type=...):pass
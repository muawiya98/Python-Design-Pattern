from abc import ABC, abstractmethod

class PizzaFactory(ABC):

    @abstractmethod
    def creat_pizza(self, type=...):pass
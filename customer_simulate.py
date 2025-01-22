from pizza_store import PizzaStore
from PizzaFactory.simple_pizza_factory import SimplePizzaFactory
from PizzaFactory.random_one_factory import RandomOnePizzaFactory
from PizzaFactory.random_tow_factory import RandomTowPizzaFactory

class CustomerSimulate:
    
    def run(self):
        self.pizza_factory = RandomOnePizzaFactory()
        store = PizzaStore(self.pizza_factory)
        pizza = store.order_pizza("cheese")
        print(pizza)


if __name__ == '__main__':
    customer_simulate = CustomerSimulate()
    customer_simulate.run()
from PizzaStoreFactory.chicago_pizza_store import ChicagoPizzaStore
from PizzaStoreFactory.NY_pizza_store import NYPizzaStore

class CustomerSimulate:
    
    def run(self):
        Chicago_store = ChicagoPizzaStore()
        NY_store = NYPizzaStore()
        pizza = NY_store.order_pizza("cheese")
        print(pizza)


if __name__ == '__main__':
    customer_simulate = CustomerSimulate()
    customer_simulate.run()
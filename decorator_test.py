from pizza_builder import PizzaBuilder

class DecoratorTest:
    
    def run(self):
        pizza = PizzaBuilder().add_mozarilla().add_zatton().add_mozarilla().build_pizza()
        print(f"The description :: {pizza.get_description()}")
        print(f"The cost :: {pizza.get_cost()}")

if __name__ == '__main__':
    decorator_test = DecoratorTest()
    decorator_test.run()
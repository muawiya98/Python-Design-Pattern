from Ipizza import IPizza
from abc import ABC
class ToppingDecorator(IPizza, ABC):

    def __inti__(self, given_pizza):
        self.tepm_pizza = given_pizza
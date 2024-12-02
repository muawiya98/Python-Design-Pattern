from abc import ABC, abstractmethod
from FlyBehavior.fly_can_fly import CanFly
from MoveBehavior.move_can_move import CanMove

class Batta(ABC):

    counter = 0

    def __init__(self):
        self.id = self.counter
        self.name = "Batta #"+str(self.id)
        self.flyable = CanFly() # Defult
        self.moveable = CanMove() # Defult
        Batta.counter+=1
    
    
    def make_sound(self):
        return "KWAK! KWAK! KWAK! KWAK!"

    def performm(self):
        print(f"Hi my name is {self.name} and my id is {self.id}")
        print(self.make_sound())
        print(self.flyable.fly())
        print(self.moveable.move())




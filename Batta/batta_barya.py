from FlyBehavior.fly_can_fly import CanFly
from FlyBehavior.fly_no_fly import NOFly
from MoveBehavior.move_can_move import CanMove
from MoveBehavior.move_no_move import NOMove
from Batta.batta import Batta

class BattaBarya(Batta):

    def __init__(self):
        super().__init__()
        self.name="Batta Barya"
        self.flyable=CanFly()
        self.moveable=CanMove()
        
    def get_shoot(self):
        self.flyable=NOFly()
        self.moveable=NOMove()

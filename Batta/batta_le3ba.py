from FlyBehavior.fly_no_fly import NOFly
from MoveBehavior.move_can_move import CanMove
from Batta.batta import Batta

class BattaLe3ba(Batta):

    def __init__(self):
        super().__init__()
        self.name="Batta Le3ba"
        self.flyable=NOFly()
        self.moveable=CanMove()
        

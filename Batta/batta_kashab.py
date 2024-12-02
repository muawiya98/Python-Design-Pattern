from FlyBehavior.fly_no_fly import NOFly
from MoveBehavior.move_no_move import NOMove
from Batta.batta import Batta

class BattaKashab(Batta):

    def __init__(self):
        super().__init__()
        self.name="Batta Kashab"
        self.flyable=NOFly()
        self.moveable=NOMove()
        

from MoveBehavior.moveable_behavior import Moveable

class NOMove(Moveable):

    def move(self):
        return "I can not move"
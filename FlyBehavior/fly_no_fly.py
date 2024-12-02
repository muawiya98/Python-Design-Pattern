from FlyBehavior.flyable_behavior import Flyable

class NOFly(Flyable):

    def fly(self):
        return "I can not fly"
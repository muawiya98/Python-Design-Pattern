from mediator import Mediator
from my_calendar import Calender
from smart_window import SmartWindow
from moving_robot import MovingRobot
from coffee_machine import CoffeeMachine
from alarm import Alarm


class MediatorTester:
    
    def run(self):
        mediator = Mediator()
        alarm = Alarm(mediator)
        my_calender = Calender()
        smart_window = SmartWindow()
        moving_robot = MovingRobot(mediator)
        coffee_machine = CoffeeMachine(mediator)

        mediator.set_objects(alarm, my_calender, moving_robot, coffee_machine, smart_window)

        alarm.snooze()




if __name__=="__main__":
    mediator_tester = MediatorTester()
    mediator_tester.run()
from coffee_machine import CoffeeMachine
from moving_robot import MovingRobot
from smart_window import SmartWindow
from my_calendar import Calender
from alarm import Alarm
class Mediator:

    def __init__(self, 
                 alarm:Alarm = None, 
                 calender:Calender = None, 
                 moving_robot:MovingRobot = None, 
                 coffee_machine:CoffeeMachine = None, 
                 smart_window:SmartWindow = None):
        self.alarm = alarm
        self.calender = calender
        self.moving_robot = moving_robot
        self.coffee_machine = coffee_machine
        self.smart_window = smart_window

    def set_objects(self, 
                    alarm:Alarm, 
                    calender:Calender, 
                    moving_robot:MovingRobot, 
                    coffee_machine:CoffeeMachine, 
                    smart_window:SmartWindow):
        self.alarm = alarm
        self.calender = calender
        self.moving_robot = moving_robot
        self.coffee_machine = coffee_machine
        self.smart_window = smart_window

    def get_time(self):
        return self.calender.get_time()

    def make_coffe(self):
        return self.coffee_machine.start()
    
    def tranport(self):
        return self.moving_robot.tranport()

    def ring_alarm(self):
        return self.alarm.ring()
    
    def open_window(self):
        return self.smart_window.open()
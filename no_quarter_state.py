from state import State

class NoQuarterState(State):

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine
    
    def insert_quarter(self):
        print("You inserted a quarter")
        # self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())
        return 0
    
    def eject_quarter(self):
        print("Sorry you cann't do it because you are in NoQuarterState")
        return 0
    
    def trun_qrank(self):
        print("Sorry you cann't do it because you are in NoQuarterState")
        return 0

    def despense(self):
        print("Sorry you cann't do it because you are in NoQuarterState")
        return 0

    def refill():pass

    def __str__(self):
        return "NoQuarterState"
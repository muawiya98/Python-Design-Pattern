from state import State
import random
import numpy as np
class HasQuarterState(State):
    
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine
    
    def insert_quarter(self):
        print("Sorry you cann't do it because you are in HasQuarterState")
        return 0
    
    def eject_quarter(self):
        print("Quarter Retruned")
        # self.gumball_machine.set_state(self.get_no_quaeter_state())
        return 0
    
    def trun_qrank(self):
        print("You turned...")
        winner = random.randint(0, 10)
        if winner==0 and self.gumball_machine.get_count()>1:
            # self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
            return 2
        else:
            # self.gumball_machine.set_state(self.gumball_machine.get_sold_state())
            return 1

    def despense(self):print("Sorry you cann't do it because you are in HasQuarterState")

    def refill():pass

    def __str__(self):
        return "HasQuarterState"

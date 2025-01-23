from state import State

class SoldState(State):

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine
    
    def insert_quarter(self):print("Sorry you cann't do it because you are in SoldState")
    
    def eject_quarter(self):
        print("Quarter Retruned")
        return 0
        # self.gumball_machine.set_state(self.get_no_quaeter_state())
    
    def trun_qrank(self):
        print("Sorry you cann't do it because you are in SoldState")
    
    def despense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count()>0:
            return 0
            # self.gumball_machine.set_state(self.gumball_machine.get_no_quaeter_state())
        else:
            print("Oops out of gunmball")
            return 1
            # self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())

    def refill():pass

    def __str__(self):
        return "SoldState"
from state import State

class WinnerState(State):
    
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine
    
    def insert_quarter(self):
        print("Sorry you cann't do it because you are in WinnerState")
        return 0
    
    def eject_quarter(self):
        print("Sorry you cann't do it because you are in WinnerState")
        return 0
    
    def trun_qrank(self):
        print("Sorry you cann't do it because you are in WinnerState")
        return 0
    
    def despense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count()==0:
            self.gumball_machine.set_state(self.get_sold_state())
        else:
            self.gumball_machine.release_ball()
            print("YOU ARE A WINNER! You got two gumballs for you quarter")
            if self.gumball_machine.get_counter()>0:
                # self.set_state(self.gumball_machine.get_no_quaeter_state())
                return 1
            else:
                print("Oops, out of gumballs!")
                # self.set_state(self.gumball_machine.get_sold_out_state())
                return 2

    def __str__(self) -> str:
        return "WinnerState"

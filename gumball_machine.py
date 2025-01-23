from has_quarter_state import HasQuarterState
from no_quarter_state import NoQuarterState
from SoldOutState import SoldOutState
from winner_state import WinnerState
from sold_state import SoldState
from transition import Trandition
from enum import Enum

class actions(Enum):
    INSERT = 1
    EJECT = 2
    TURN = 3
    DISPENSE = 4

class GumballMachine:
    def __init__(self, number_of_gumball):

        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
        self.state = self.soldOutState
        self.count = number_of_gumball
        self.actions = actions
        self.action = None
        self.transtions = []
        if number_of_gumball>0:
            self.state = self.noQuarterState
        self.creat_transition_table()

    def creat_transition_table(self):
        self.transtions.append(Trandition(self.noQuarterState,
                                          self.actions.INSERT,
                                          0,
                                          self.hasQuarterState))
        
        self.transtions.append(Trandition(self.hasQuarterState,
                                          self.actions.EJECT,
                                          0,
                                          self.noQuarterState))
        
        self.transtions.append(Trandition(self.hasQuarterState,
                                          self.actions.TURN,
                                          1,
                                          self.soldState))
        
        self.transtions.append(Trandition(self.hasQuarterState,
                                          self.actions.TURN,
                                          2,
                                          self.winnerState))
        
        self.transtions.append(Trandition(self.soldState,
                                          self.actions.DISPENSE,
                                          1,
                                          self.soldOutState))
        
        self.transtions.append(Trandition(self.soldState,
                                          self.actions.DISPENSE,
                                          0,
                                          self.noQuarterState))
        
        self.transtions.append(Trandition(self.winnerState,
                                          self.actions.DISPENSE,
                                          0,
                                          self.noQuarterState))
        
        self.transtions.append(Trandition(self.winnerState,
                                          self.actions.DISPENSE,
                                          1,
                                          self.soldOutState))
    
    def set_next_state(self, status):
        for transtion in  self.transtions:
            if self.state == status and self.actions == transtion.action and status==transtion.status:
                self.state = transtion.to_state

    def insert_quarter(self):
        self.action = self.actions.INSERT
        self.set_next_state(self.state.insert_quarter())

    def eject_quarter(self):
        self.action = self.actions.EJECT
        self.set_next_state(self.state.eject_quarter())

    def turn_crank(self):
        self.action = self.actions.TURN
        self.set_next_state(self.state.trun_qrank())
        self.action = self.actions.DISPENSE
        self.set_next_state(self.state.despense())

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print("A gumball comes rolling out the slot ...")
        if self.count!=0:self.count-=1

    def get_count(self):
        return self.count

    def refill(self, count):
        self.count+=count
        print(f"the gumball machine was just refill; it's new count is : {self.count}")

    def get_state(self):
        return self.state
    
    def get_sold_out_state(self):
        return self.soldOutState
   
    def get_no_quaeter_state(self):
        return self.noQuarterState

    def get_has_quarter_state(self):
        return self.hasQuarterState

    def get_sold_state(self):
        return self.soldState

    def get_winner_state(self):
        return self.winnerState
    
    def __str__(self) -> str:
        return f"the machin in state : {self.state} with number of gumball : {self.count}"

    
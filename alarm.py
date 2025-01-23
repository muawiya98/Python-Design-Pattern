import random
class Alarm:

    def __init__(self, mediator):
        self.mediator = mediator

    def snooze(self):
        day = self.mediator.get_time()
        if day!=0 and day!=6:
            self.mediator.make_coffe()
    
    def ring(self):
        print("Ringingggggg")
        

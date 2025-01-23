class CoffeeMachine:

    def __init__(self, mediator):
        self.mediator = mediator

    def start(self):
        print("Preparing coffee")
        print("Finshed preparing coffee")

        day = self.mediator.get_time()
        if day == 3 :
            print("Adding sugar")
        self.mediator.tranport()
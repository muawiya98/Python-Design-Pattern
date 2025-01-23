class MovingRobot:
    def __init__(self, mediator):
        self.mediator = mediator

    def tranport(self):
        print("Robot transporting !!")
        print("Reached Destination !!")
        self.mediator.ring_alarm()
        self.mediator.open_window()

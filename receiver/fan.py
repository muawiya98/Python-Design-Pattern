class Fan:
    def __init__(self, place):
        self.place = place
        self.speed = 0

    def speed_up(self):
        self.speed = (self.speed + 1) % 4
        print(f"The Fan's speed in {self.place} now is: {self.speed}")

    def speed_down(self):
        self.speed = (self.speed - 1) % 4
        print(f"The Fan's speed in {self.place} now is: {self.speed}")
class Light:
    def __init__(self, place):
        self.place = place

    def ON(self):
        print(f"Light In {self.place} ON")

    def OFF(self):
        print(f"Light in {self.place} OFF")

class TheaterLights:
    
    def __init__(self, description):
        self.description = description

    def dim(self, level):
        print(f"{self.description} {level}")

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def __str__(self):
        return f"{self.description}"
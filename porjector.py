
class Projector:
     
    def __init__(self, description, dvd_player):
        self.description = description
        self.dvd_palyer = dvd_player

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def wide_screen(self):
        print(f"{self.description} in widescreen mode (16*9 aspect ratio)")

    def tv_mode(self):
        print(f"{self.description} in gtv mode (4*3 aspect ratio)")

    def __str__(self):
        return f"{self.description}"
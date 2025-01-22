
class CDPlayer:

    def __init__(self, description, amplifier):
        self.description = description
        self.amplifier = amplifier
        self.current_track = 0
        self.title = ''

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def eject(self):
        self.title=None
        print(f"{self.description} eject")

    def play(self, title:str):
        self.title = title
        self.current_track = 0 
        print(f"{self.description} palying {self.title}")
    
    def play(self, track:int):
        if self.title is None:
            print(f"{self.description} can't paly track {self.current_track} no cd inseted")
        else:
            self.current_track = track
            print(f"{self.description} palying track {self.current_track}")

    def stop(self):
        self.current_track=0
        print(f"{self.description} stopped")

    def puase(self):
        print(f"{self.description} paused  {self.title}")

    def __str__(self):
        return f"{self.description}"
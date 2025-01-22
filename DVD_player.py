
class DVDPlayer:

    def __init__(self, description, amplifier):
        self.description = description
        self.amplifier = amplifier
        self.current_track = 0
        self.movie = ''

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def eject(self):
        self.title=None
        print(f"{self.description} eject")

    def play(self, movie:str):
        self.movie = movie
        self.current_track = 0 
        print(f"{self.description} is playing")
    
    def play(self, track:int):
        if self.movie is None:
            print(f"{self.description} can't paly track {self.current_track} no cd inseted")
        else:
            self.current_track = track
            print(f"{self.description} palying track {self.current_track}")

    def stop(self):
        self.current_track=0
        print(f"{self.description} stopped")

    def puase(self):
        print(f"{self.description} paused")

    def __str__(self):
        return f"{self.description}"
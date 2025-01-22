
class Amplifier:
    
    def __init__(self, description):
        self.description = description
        self.turner = None
        self.dvd = None
        self.cdpalyer = None

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def set_streo_sound(self):
        print(f"{self.description} streo mode on")

    def set_surround_sound(self):
        print(f"{self.description} surround sound on (5 speakers, 1 subwoofer)")
    
    def set_volume(self, level):
        print(f"{self.description} setting volume to {level}")

    def set_truner(self, turner):
        print(f"{self.description} setting truner to {self.dvd}")
        self.turner = turner

    def set_dvd(self, dvd):
        print(f"{self.description} setting DVD palyer to {dvd}")
        self.dvd = dvd

    def set_cd(self, cd):
        print(f"{self.description} setting CD palyer to {cd}")
        self.cd = cd

    def __str__(self):
        return f"{self.description}"
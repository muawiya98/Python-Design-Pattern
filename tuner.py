
class Tuner:

    def __init__(self, description, amp):
        self.description = description
        self.amp = amp

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def set_frequency(self, frequency):
        print(f"{self.description} setting frequency to {frequency}")
    
    def __str__(self):
        return f"{self.description}"
    


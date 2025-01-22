
class PopcornPopper:

    def __init__(self, description):
        self.description = description

    def cn(self):
        print(f"{self.description} creat")
    
    def pop(self):
        print(f"{self.description} pop")

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def __str__(self):
        return f"{self.description}"
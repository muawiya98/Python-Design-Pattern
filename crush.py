
class Crush:
    
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"I'm {self.name}, I am {self.status}"
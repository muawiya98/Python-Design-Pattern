from lover_observer import Lover

class ShyLover(Lover):
    
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.subject.subscribe(self)
    
    def update(self, crushes):
        print(f"{self} I got this information: ")
        for crush in crushes:
            print(crush)

    def __str__(self):
        return f"I am shy lover my name is :{self.name}::"
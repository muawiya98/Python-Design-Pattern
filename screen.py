
class Screen:

    def __init__(self, description):
        self.description = description

    def down(self):
        print(f"{self.description} going down")
    
    def up(self):
        print(f"{self.description} going up")

    def __str__(self):
        return f"{self.description}"
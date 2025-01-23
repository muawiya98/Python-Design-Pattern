from example_1.beverage import Beverage

class Coffee(Beverage):

    def __init__(self, wanted_edafat=True):
        self.wanted_edafat = wanted_edafat

    def want_edafat(self):
        return self.wanted_edafat

    def add_main_component(self): print("Brewing Coffee")

    def add_edafat(self): print("Add Milke and Sugar")
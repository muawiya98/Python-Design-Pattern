
class Beverage:
    
    def prepare(self):
        self.boil_water()
        self.add_main_component()
        self.add_water2cup()
        if self.want_edafat():
            self.add_edafat()

    def boil_water(self): print("Boilling Water")

    def add_water2cup(self): print("Add Water to Cup")

    def add_main_component(self):pass

    def add_edafat(self):pass

    # Hook Function
    def want_edafat(self): return True
from Batta.batta_barya import BattaBarya
from Batta.batta_kashab import BattaKashab
from Batta.batta_le3ba import BattaLe3ba

class Simulater:

    def __init__(self):
        self.batta_barya = BattaBarya()
        self.batta_kashab = BattaKashab()
        self.batta_le3ba = BattaLe3ba()
    
    def run(self):
        print(10*"*", "BattaBarya", 10*"*")
        self.batta_barya.performm()
        print(10*"*", "BattaBarya After shooting", 10*"*")
        self.batta_barya.get_shoot()
        self.batta_barya.performm()
        print(10*"*", "BattaKashab", 10*"*")
        self.batta_kashab.performm()
        print(10*"*", "BattaLe3ba", 10*"*")
        self.batta_le3ba.performm()

if __name__ == '__main__':
    simulater = Simulater()
    simulater.run()
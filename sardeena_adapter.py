from sardeena import Sardeena
from Ienemy import IEnemy

# Object Adapter
class SardeenaAdapter(IEnemy):
    def __init__(self, temp_sardeena):
        self.temp_sardeena = temp_sardeena

    def fireCannons(self):
        self.temp_sardeena.EqsefGabha()
    
    def refillBanzeen(self):
        self.temp_sardeena.Edrab7agareen()

# # Class Adapter
# class SardeenaAdapter(IEnemy, Sardeena):

#     def fireCannons(self):
#         self.EqsefGabha()
#     def refillBanzeen(self):
#         self.Edrab7agareen()
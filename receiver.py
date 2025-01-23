from add_handler import AddHandler
from subtrac_handler import SubtracHandler
from mul_handler import MulHandler
from power_handler import PowerHandler
from div_handler import DivHandler



class Receiver:

    def __init__(self):
        self.add_handler = AddHandler()
        self.sub_handler = SubtracHandler()
        self.mul_handler = MulHandler()
        self.power_handler = PowerHandler()
        self.div_handler = DivHandler()

        self.add_handler.set_next_chain(self.sub_handler)
        self.sub_handler.set_next_chain(self.mul_handler)
        self.mul_handler.set_next_chain(self.power_handler)
        self.power_handler.set_next_chain(self.div_handler)

    def send_request(self, request):
        self.add_handler.calculate(request)
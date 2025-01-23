from math_handler import MathHandler
from request import Request
class SubtracHandler(MathHandler):

    def set_next_chain(self, handler:MathHandler):
        self.next_handler = handler

    def calculate(self, request:Request):
        if request.operation=='-':
            print(request.first_parameter - request.second_parameter)
        else:
            self.next_handler.calculate(request)
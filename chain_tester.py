from request import Request
from receiver import Receiver


class ChainTester:

    def run(self):
        request = Request(5, 10, "$")
        receiver = Receiver()
        receiver.send_request(request)

if __name__=="__main__":
    chain_tester = ChainTester()
    chain_tester.run()
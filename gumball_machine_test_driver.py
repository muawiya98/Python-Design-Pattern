from gumball_machine import GumballMachine

class GumballMachineTestDriver:
    
    def run(self):
        gumball_machine = GumballMachine(2)
        print(gumball_machine)

        gumball_machine.insert_quarter()
        gumball_machine.turn_crank()

        print(gumball_machine)

        gumball_machine.insert_quarter()
        gumball_machine.turn_crank()
        gumball_machine.insert_quarter()
        gumball_machine.turn_crank()

        gumball_machine.refill(5)
        gumball_machine.insert_quarter()
        gumball_machine.turn_crank()

        print(gumball_machine)



if __name__=="__main__":
    gumballMachineTestDriver = GumballMachineTestDriver()
    gumballMachineTestDriver.run()
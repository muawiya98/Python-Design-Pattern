from pancake_house_menu import PancakeHouseMenu
from diner_menu import DinerMenu
from waitress import Waitress

class IteratorTester:

    def run(self):
        pancake_house_menu = PancakeHouseMenu()
        diner_menu = DinerMenu()
        waitress = Waitress([pancake_house_menu, diner_menu])
        waitress.print_menu()


if __name__=="__main__":
    iterator_tester = IteratorTester()
    iterator_tester.run()
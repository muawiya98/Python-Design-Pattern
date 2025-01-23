
class Waitress:
    def __init__(self, menus):
        self.menus = menus

    def print_menu(self):
        for i in self.menus:
            print("--------------------")
            self.menu_print(i)

    def menu_print(self, iterator):
        for ite in iterator.get_iterator():
            print(ite.get_description() )
from menu_item import MenuItem
from menu import Menu

class PancakeHouseMenu(Menu):

    def __init__(self):
        self.menu_items = []
        
        self.add_item("K&B's Pancak Breakfast", 
                      "Pancake with scrambled eggs, and toast", 
                      True, 2.99)

        self.add_item("Regular Pancak Breakfast", 
                      "Pancake with fried eggs, sausage", 
                      False, 2.99)

        self.add_item("Bluebarry Pancakes", 
                      "Pancake made with fresh blueberry, and blueberry syurp", 
                      True, 2.49)

    def add_item(self, name:str, description:str, vegtarian:bool, price:float):
        menu_item = MenuItem(name, description, vegtarian, price)
        self.menu_items.append(menu_item)

    def get_iterator(self):
        return self.menu_items
        

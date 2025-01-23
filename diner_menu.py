from menu_item import MenuItem
from menu import Menu
import numpy as np

class DinerMenu(Menu):
    
    def __init__(self):
        self.menu_items = []
        self.add_item("Vegetarian BLT", 
                      "(Fakin') Bacom with lettuce & tomato on whole wheat", 
                      True, 2.99)

        self.add_item("BLT", 
                      "Bacom with lettuce & tomato on whole wheat", 
                      False, 2.99)

        self.add_item("Hotdog", 
                      "A hot dog, with saurkraut, relish, onions, topped with cheese", 
                      False, 3.05)

    def add_item(self, name:str, description:str, vegtarian:bool, price:float):
        menu_item = MenuItem(name, description, vegtarian, price)
        self.menu_items.append(menu_item)

    def get_iterator(self):
        return self.menu_items

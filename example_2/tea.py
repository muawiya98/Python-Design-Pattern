from example_1.beverage import Beverage
from example_2.sorting import Sorting

class Tea(Beverage, Sorting):

    def __init__(self, wanted_edafat=True, cub_size=None):
        self.wanted_edafat = wanted_edafat
        self.cub_size = cub_size

    def __str__(self):
        return f"Tea Object with cub_size {self.cub_size}"

    def want_edafat(self):
        return self.wanted_edafat
    
    def compare_to(self, first, second):
        if first.cub_size is None or second.cub_size is None:return -1
        elif first.cub_size>second.cub_size:return 1
        elif first.cub_size<second.cub_size:return 0
        else:return -1
    
    def add_main_component(self): print("Adding Tea Bag")

    def add_edafat(self): print("Adding Lemon")

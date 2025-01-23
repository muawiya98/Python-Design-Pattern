from visitor.visitable import Visitable
from visitor.visitor import Visitor

class Manga(Visitable):

    def __init__(self, price):
        self.price = price

    def set_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price
    
    def accept(self, visitor:Visitor):
        visitor.manga_visit(self)
    
from visitor.visitor import Visitor
from product.car import Car
from product.manga import Manga
from product.cherr import Cherr

class Sales(Visitor):

    def car_visit(self, obj:Car):
        obj.set_price(obj.get_price() * 1.2)
    def manga_visit(self, obj:Manga):
        obj.set_price(obj.get_price() * 1.1)
    def cherr_visit(self, obj:Cherr):
        obj.set_price(obj.get_price() * 1.4)

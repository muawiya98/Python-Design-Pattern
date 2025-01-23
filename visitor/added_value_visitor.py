from visitor.visitor import Visitor
from product.car import Car
from product.manga import Manga
from product.cherr import Cherr

class AddedValue(Visitor):

    def car_visit(self, obj:Car):
        obj.set_price(obj.get_price() * 1.9)
    def manga_visit(self, obj:Manga):
        obj.set_price(obj.get_price() * 1.4)
    def cherr_visit(self, obj:Cherr):
        obj.set_price(obj.get_price() * 1.7)
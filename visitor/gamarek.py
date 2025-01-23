from visitor.visitor import Visitor
from product.car import Car
from product.manga import Manga
from product.cherr import Cherr

class Gamarek(Visitor):

    def car_visit(self, obj:Car):
        print("here 1")
        obj.set_price(obj.get_price() * 1.05)
    def manga_visit(self, obj:Manga):
        print("here 2")
        obj.set_price(obj.get_price() * 1.07)
    def cherr_visit(self, obj:Cherr):
        print("here 3")
        obj.set_price(obj.get_price() * 1.09)
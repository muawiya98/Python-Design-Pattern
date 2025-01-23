from product.manga import Manga
from product.car import Car
from product.cherr import Cherr

from visitor.added_value_visitor import AddedValue
from visitor.sales_visitor import Sales
from visitor.gamarek import Gamarek


class VisitorTester:

    def run(self):
        manga, car, cherr = Manga(100), Car(2500), Cherr(500)

        visitor1, visitor2, visitor3 = Sales(), AddedValue(), Gamarek()

        print(car.get_price())
        car.accept(visitor1)
        print(car.get_price())
        car.accept(visitor3)
        print(car.get_price())

        print(50*"*")

        print(manga.get_price())
        manga.accept(visitor2)
        print(manga.get_price())
        manga.accept(visitor3)
        print(manga.get_price())

        print(50*"*")

        print(cherr.get_price())
        cherr.accept(visitor1)
        print(cherr.get_price())
        cherr.accept(visitor2)
        print(cherr.get_price())
        cherr.accept(visitor3)
        print(cherr.get_price())



if __name__=="__main__":
    visitor_tester = VisitorTester()
    visitor_tester.run()
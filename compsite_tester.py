from department import Department
from employee import Employee
class CompsiteTester:

    def run(self):
        e1 = Employee('Muawiya Al Danaf', 700)
        e7 = Employee('Yazen Al Jerody', 600)
        e2 = Employee('Yasser Zaidan', 500)
        e3 = Employee('Amjad Mohammad', 400)
        e4 = Employee('Khaled Abd', 300)
        e5 = Employee('Yassin Khalil', 200)
        e6 = Employee('Omar Mujahed', 100)


        d1 = Department('Main')
        d2 = Department('AI')
        d3 = Department('Software')

        d1.add(e1)
        d1.add(e2)
        d2.add(e3)
        d2.add(e4)
        d3.add(e5)
        d3.add(e6)
        d3.add(e7)
        d2.add(d3)
        d1.add(d2)

        d1.print_info(1)





if __name__=="__main__":
    compsite_tester = CompsiteTester()
    compsite_tester.run()
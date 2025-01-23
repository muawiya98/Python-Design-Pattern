from example_1.coffee import Coffee
from example_1.tea import Tea
from example_2.sorting import Sorting
from example_2.tea import Tea
class TemplateMethodTester:

    def run_example_1(self):
        tea = Tea()
        tea.prepare()
        print(50*"*")
        tea1 = Tea(False)
        tea1.prepare()
        print(50*"*")
        coffee = Coffee()
        coffee.prepare()
        print(50*"*")
        coffee1 = Coffee(False)
        coffee1.prepare()
    
    def run_example_2(self):
        a = [55, -1, 2, 18]
        print(a)
        a = Sorting().sort(a)
        print(a)

        print()
        print(50* "*")
        print()
        
        tea_list = [Tea(False, 5), Tea(False, 6), Tea(False, 1)]
        tea_list = Tea().sort(tea_list)
        for t in tea_list:
            print(t)



if __name__=="__main__":
    template_method_tester = TemplateMethodTester()
    # template_method_tester.run_example_1()
    template_method_tester.run_example_2()
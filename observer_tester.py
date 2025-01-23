from listener import Listener
from shy_lover_observer import ShyLover
from active_lover_observer import ActiveLover


class ObserverTester:
    
    def run(self):
        listener = Listener()
        l1 = ShyLover("Khaled", listener)
        l2 = ActiveLover("Muawiya", listener) 
        l3 = ShyLover("Sami", listener)
        l4 = ShyLover("Amjad", listener)
        listener.set_new_info(listener.crushes[0].name, True)
        print(50*"*")
        l3.subject.unsubscribe(l3)
        listener.set_new_info(listener.crushes[1].name, True)

if __name__=="__main__":
    observer_tester = ObserverTester()
    observer_tester.run()
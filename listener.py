from crush import Crush
from subject import Subject

class Listener(Subject):
    
    def __init__(self):
        self.crushes = [Crush("Leen", False), Crush("Lana", False), Crush("Sana", True)]
        self.observers = []

    def subscribe(self, new_observer):
        self.observers.append(new_observer)

    def unsubscribe(self, observer):
        for ind, obs in enumerate(self.observers):
            if obs == observer: 
                del self.observers[ind]
                break

    def have_new_info(self):
        for observer in self.observers:
            observer.update(self.crushes)

    def set_new_info(self, name, status):
        for ind, crush in enumerate(self.crushes):
            if crush.name==name:
                self.crushes[ind].status = status
        self.have_new_info()

    


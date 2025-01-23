from abc import ABC

class Subject(ABC):
    def subscribe(self, new_observer):pass
    def unsubscribe(self, crushes):pass
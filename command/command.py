from abc import ABC

class Command(ABC):
    def execute(self):pass
    def unexecute(self):pass
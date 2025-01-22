from abc import ABC
from Producte.robot import Robot

class RobotBuilder(ABC):
    def __init__(self):
        self.type = None
        self.price = None
        self.warranty_years = None
        self.head_type = None
        self.body_type = None
        self.legs_type = None

    def setType(self):pass
    def setPrice(self):pass
    def setWarrantyYears(self):pass
    def set_HeadType(self):pass
    def setBodyType(self):pass
    def setLegsType(self):pass
    def build(self):
        if self.legs_type is None:print("legs_type is not valid")
        if self.body_type is None:print("body_type is not valid")
        if self.head_type is None:print("head_type is not valid")
        if self.warranty_years is None:print("warranty_years is not valid")
        if self.price is None:
            self.price = 60000 if self.type=='spherical' else 20000
        return Robot(self.type, self.price, self.warranty_years, self.head_type, self.body_type, self.legs_type)
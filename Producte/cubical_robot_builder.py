from Producte.robot_builder import RobotBuilder

class CubicalRobotBuilder(RobotBuilder):
    def setType(self):
        self.type='cubical'
        return self
    def setPrice(self):
        self.price=20000
        return self
    def setWarrantyYears(self):
        self.warranty_years=5
        return self
    def set_HeadType(self):
        self.head_type='cubical'
        return self
    def setBodyType(self):
        self.body_type='cubical'
        return self
    def setLegsType(self):
        self.legs_type='cubical'
        return self
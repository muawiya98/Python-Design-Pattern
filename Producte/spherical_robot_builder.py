from Producte.robot_builder import RobotBuilder

class SphericalRobotBuilder(RobotBuilder):
    def setType(self):
        self.type='spherical'
        return self
    def setPrice(self):
        self.price=60000
        return self
    def setWarrantyYears(self):
        self.warranty_years=10
        return self
    def set_HeadType(self):
        self.head_type='spherical'
        return self
    def setBodyType(self):
        self.body_type='spherical'
        return self
    def setLegsType(self):
        self.legs_type='spherical'
        return self
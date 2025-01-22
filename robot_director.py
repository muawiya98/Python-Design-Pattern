
class RobotDirector:

    def __init__(self, robot_builder):
        self.robot_builder = robot_builder

    def get_robot(self):
        self.robot_builder.setType().\
            setPrice().\
            setWarrantyYears().\
            set_HeadType().\
            setBodyType().\
            setLegsType()
        return self.robot_builder.build()
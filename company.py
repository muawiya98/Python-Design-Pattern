from Producte.spherical_robot_builder import SphericalRobotBuilder
from Producte.cubical_robot_builder import CubicalRobotBuilder
from robot_director import RobotDirector
class Company:

    def run(self):
        robot_director = RobotDirector(CubicalRobotBuilder())
        robot = robot_director.get_robot()
        print(robot)

if __name__ == '__main__':
    company = Company()
    company.run()
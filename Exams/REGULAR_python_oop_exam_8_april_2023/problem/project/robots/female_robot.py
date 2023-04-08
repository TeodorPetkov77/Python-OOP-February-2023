from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    __DEFAULT_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.__DEFAULT_WEIGHT)

    def eating(self):
        self.weight += 1

from abc import ABC, abstractmethod
from project.robots.base_robot import BaseRobot


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name: str = name
        self.capacity: int = capacity
        self.robots: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @abstractmethod
    def details(self):
        ...

    def is_full(self):
        return len(self.robots) == self.capacity

    def robot_in_service(self, robot_name: str):
        found_robot = [r for r in self.robots if r.name == robot_name]
        if found_robot:
            return found_robot[0]


    def add_robot(self, robot: BaseRobot):
        self.robots.append(robot)

    def remove_robot(self, robot: BaseRobot):
        self.robots.remove(robot)
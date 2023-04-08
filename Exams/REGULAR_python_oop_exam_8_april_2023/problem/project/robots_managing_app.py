from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    @property
    def valid_service_types(self):
        return {
            "MainService": MainService,
            "SecondaryService": SecondaryService
        }

    @property
    def valid_robot_types(self):
        return {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot
        }

    def add_robot_to_collection(self, robot: BaseRobot):
        self.robots.append(robot)

    def remove_robot_from_collection(self, robot: BaseRobot):
        self.robots.remove(robot)

    def get_robot_by_name(self, robot_name: str):

        found_robot = [r for r in self.robots if r.name == robot_name]

        if found_robot:
            return found_robot[0]

    def get_service_by_name(self, service_name: str):

        found_service = [s for s in self.services if s.name == service_name]

        if found_service:
            return found_service[0]

    def add_service(self, service_type: str, name: str):

        if service_type not in self.valid_service_types.keys():
            raise Exception("Invalid service type!")

        new_service = self.valid_service_types[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in self.valid_robot_types.keys():
            raise Exception("Invalid robot type!")

        new_robot = self.valid_robot_types[robot_type](name, kind, price)
        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):

        suitable_services = {
            "MaleRobot": "MainService",
            "FemaleRobot": "SecondaryService"
        }

        robot = self.get_robot_by_name(robot_name)
        service = self.get_service_by_name(service_name)

        robot_type = robot.__class__.__name__
        service_type = service.__class__.__name__

        if suitable_services[robot_type] != service_type:
            return "Unsuitable service."

        if service.is_full():
            raise Exception("Not enough capacity for this robot!")

        self.remove_robot_from_collection(robot)
        service.add_robot(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = self.get_service_by_name(service_name)
        found_robot = service.robot_in_service(robot_name)

        if not found_robot:
            raise Exception("No such robot in this service!")

        service.remove_robot(found_robot)
        self.add_robot_to_collection(found_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):

        service = self.get_service_by_name(service_name)
        robots_fed = 0

        for robots_fed, robot in enumerate(service.robots, 1):
            robot.eating()

        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name: str):

        service = self.get_service_by_name(service_name)
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([s.details() for s in self.services])

# https://judge.softuni.org/Contests/Compete/Index/3911#1



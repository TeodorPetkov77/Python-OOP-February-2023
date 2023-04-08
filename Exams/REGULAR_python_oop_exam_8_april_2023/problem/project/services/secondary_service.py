from project.services.base_service import BaseService


class SecondaryService(BaseService):
    __DEFAULT_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.__DEFAULT_CAPACITY)

    def details(self):
        result = f"{self.name} Secondary Service:\nRobots: "
        if self.robots:
            return result + " ".join(r.name for r in self.robots)
        return result + "none"

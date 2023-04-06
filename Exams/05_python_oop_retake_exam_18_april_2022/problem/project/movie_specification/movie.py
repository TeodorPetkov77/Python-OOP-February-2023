from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        self.title: str = title
        self.year: int = year
        self.owner = owner
        self.age_restriction: int = age_restriction
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @abstractmethod
    def details(self):
        ...

    def is_owner(self, username: str):
        return username == self.owner.username

    def receive_like(self):
        self.likes += 1

    def receive_dislike(self):
        self.likes -= 1

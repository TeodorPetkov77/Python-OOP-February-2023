import unittest
from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        room.take_room(people)
        self.guests = sum([r.guests for r in self.rooms])

    def free_room(self, room_number):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        room.free_room()
        self.guests = sum([r.guests for r in self.rooms])

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken is False])}\n" \
               f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken is True])}"

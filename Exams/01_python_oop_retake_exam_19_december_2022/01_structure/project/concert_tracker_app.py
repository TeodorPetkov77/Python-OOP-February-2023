from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List = []
        self.musicians: List = []
        self.concerts: List = []

    @property
    def valid_musicians(self):
        return {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer
        }

    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type not in self.valid_musicians:
            raise ValueError("Invalid musician type!")

        if [m for m in self.musicians if m.name == name]:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.valid_musicians[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name):

        if [b for b in self.bands if b.name == name]:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        if [c for c in self.concerts if c.place == place]:
            raise Exception(f"{place} is already registered for {genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name]
        band = [b for b in self.bands if b.name == band_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band[0].members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name]

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = [m for m in band[0].members if m.name == musician_name]

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band[0].members.remove(musician[0])
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        musician_types = [m.__class__.__name__ for m in band.members]

        if len(set(musician_types)) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        rock_req = {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing high pitch notes"],
            "Guitarist": ["play rock"]
        }

        metal_req = {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing low pitch notes"],
            "Guitarist": ["play metal"]
        }

        jazz_req = {
            "Drummer": ["play the drums with drum brushes"],
            "Singer": ["sing high pitch notes", "sing low pitch notes"],
            "Guitarist": ["play jazz"]
        }

        chosen_genre_req = {
            "Rock": rock_req,
            "Metal": metal_req,
            "Jazz": jazz_req
        }

        genre_req = chosen_genre_req[concert.genre]

        for musician_type, requirements in genre_req.items():
            for musician in [m for m in band.members if m.__class__.__name__ == musician_type]:
                for req in requirements:
                    if req not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

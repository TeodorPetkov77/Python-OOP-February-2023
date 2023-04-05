from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    @property
    def valid_horse_types(self):
        return {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred
        }

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        found_horse = [h for h in self.horses if h.name == horse_name]

        if horse_type in self.valid_horse_types:

            if found_horse:
                raise Exception(f"Horse {horse_name} has been already added!")

            new_horse = self.valid_horse_types[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        found_jockey = [j for j in self.jockeys if j.name == jockey_name]

        if found_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        found_race = [r for r in self.horse_races if r.race_type == race_type]

        if found_race:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse_found = [h for h in self.horses if h.__class__.__name__ == horse_type and h.is_taken is False]
        jockey_found = [j for j in self.jockeys if j.name == jockey_name]

        if not jockey_found:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse_found:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey_found[0].horse:
            return f"Jockey {jockey_name} already has a horse."

        horse = horse_found[-1]
        jockey = jockey_found[0]

        horse.is_taken = True
        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race_found = [r for r in self.horse_races if r.race_type == race_type]
        jockey_found = [j for j in self.jockeys if j.name == jockey_name]

        if not race_found:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey_found:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = jockey_found[0]
        race = race_found[0]

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        race_found = [r for r in self.horse_races if r.race_type == race_type]

        if not race_found:
            raise Exception(f"Race {race_type} could not be found!")

        race = race_found[0]

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        racers = race.jockeys

        fastest_racer = list(sorted(racers, key=lambda x: -x.horse.speed))[0]

        return f"The winner of the {race_type} race, with a speed of " \
               f"{fastest_racer.horse.speed}km/h is {fastest_racer.name}! " \
               f"Winner's horse: {fastest_racer.horse.name}."


# https://judge.softuni.org/Contests/Practice/Index/3558#1

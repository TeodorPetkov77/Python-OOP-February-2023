from collections import deque
from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def __find_player_by_name(self, name):
        player = [n for n in self.players if name == n.name]
        if player:
            return player[0]

    def add_player(self, *args: Player):

        new_players = []

        for player in args:

            if player not in self.players and player not in new_players:
                new_players.append(player)

        self.players.extend(new_players)
        return "Successfully added: " + ", ".join([p.name for p in new_players])

    def add_supply(self, *args: Supply):

        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):

        player = self.__find_player_by_name(player_name)

        if player:

            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            if sustenance_type in ("Food", "Drink"):

                for index in range(len(self.supplies) - 1, -1, -1):
                    if self.supplies[index].__class__.__name__ == sustenance_type:
                        food_to_consume = self.supplies.pop(index)
                        player.sustain_player(food_to_consume)
                        return f"{player_name} sustained successfully with {food_to_consume.name}."
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):

        message = []

        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        for player in (first_player, second_player):

            if player.is_stamina_zero():
                message.append(f"Player {player.name} does not have enough stamina.")

        if message:
            return "\n".join(message)

        player_order = deque(sorted([first_player, second_player], key=lambda x: x.stamina))

        for i in range(2):

            attack_player = player_order[0]
            defend_player = player_order[1]
            damage_done = attack_player.stamina / 2

            if defend_player.stamina - damage_done <= 0:
                defend_player.stamina = 0
                return f"Winner: {attack_player.name}"

            else:
                defend_player.stamina -= damage_done

            player_order.appendleft(player_order.pop())

        winner = sorted([first_player, second_player], key=lambda x: x.stamina)[-1]

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        players = "\n".join([str(p) for p in self.players])
        supplies = "\n".join([p.details() for p in self.supplies])
        return "\n".join([players, supplies])

# https://judge.softuni.org/Contests/Practice/Index/3426#1

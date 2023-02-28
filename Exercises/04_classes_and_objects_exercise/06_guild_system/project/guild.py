class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player not in self.players:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            else:
                return f"Player {player.name} is in another guild."
        else:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str):
        for name in self.players:
            if name.name == player_name:
                self.players.remove(name)
                name.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join([info.player_info() for info in self.players])

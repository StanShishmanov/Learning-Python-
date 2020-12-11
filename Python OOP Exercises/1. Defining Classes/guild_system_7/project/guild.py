# from guild_system_7.project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = list()

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for p in self.players:
            if p.name == player_name:
                p.guild = "Unaffiliated"
                self.players.remove(p)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        first_line = f"Guild: {self.name}\n"
        text = ""
        for p in self.players:
            if p == self.players[-1]:
                text += f"{p.player_info()}"
            else:
                text += f"{p.player_info()}\n"
        return first_line + text

# #
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.add_skill("Different Stuff", 120))
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# guild2 = Guild("Master Assassins")
# print(guild.assign_player(player))
# print(guild.guild_info())
#
# player2 = Player("Alex", 20, 50)
# print(player2.add_skill("Ultra Stun", 30))
# print(player2.player_info())
# print(guild2.assign_player(player2))
# print(guild2.guild_info())
# print(guild.assign_player(player2))
# print(guild2.kick_player("Alex"))
# print(guild.assign_player(player2))
# print(guild.guild_info())
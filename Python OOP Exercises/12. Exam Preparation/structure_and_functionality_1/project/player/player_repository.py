from project.player.player import Player


class PlayerRepository:

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player in self.players:
            raise ValueError(f"Player {player.username} already exists!")
        else:
            self.players.append(player)
            self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        else:
            self.players.remove(self.find(player))
            self.count -= 1

    def find(self, username):
        p = [p for p in self.players if p.username == username][0]
        return p


# p = Beginner("test")
#
# pr = PlayerRepository()
# pr.add(p)
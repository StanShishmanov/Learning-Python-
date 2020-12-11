from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type_p: str, username: str):
        if type_p == "Beginner":
            player = Beginner(username)
        elif type_p == "Advanced":
            player = Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type_p} with username: {username}"

    def add_card(self, type_c: str, name: str):
        if type_c == "Magic":
            card = MagicCard(name)
        elif type_c == "Trap":
            card = TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type_c}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attacker_name: str, enemy_name: str):
        attacker = self.player_repository.find(attacker_name)
        enemy = self.player_repository.find(enemy_name)

        battlefield = BattleField()
        battlefield.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for p in self.player_repository.players:
            result += f"Username: {p.username} - Health: {p.health} - Cards {len(p.card_repository.cards)}\n"
            for c in p.card_repository.cards:
                result += f"### Card: {c.name} - Damage: {c.damage_points}\n"
        return result

#
# control = Controller()
#
# p1 = Beginner("George")
# p2 = Advanced("Peter")
#
# control.player_repository.add(p1)
# control.player_repository.add(p2)
#
# c1 = MagicCard("Heal")
# c2 = TrapCard("Magic Arrow")
#
# c3 = MagicCard("Cure")
# c4 = TrapCard("Lightning Strike")
# print(control.card_repository.add(c1))
# print(control.card_repository.add(c2))
# print(control.card_repository.add(c3))
# print(control.card_repository.add(c4))
#
# print(control.add_player_card("George", "Heal"))
# print(control.add_player_card("George", "Cure"))
# print(control.add_player_card("Peter", "Magic Arrow"))
# print(control.add_player_card("Peter", "Lightning Strike"))
#
# print(control.fight("George", "Peter"))
# print(control.report())
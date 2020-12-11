import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):

    def test_attacker_is_dead(self):
        p1 = Advanced("test")
        p1.health = 0
        p2 = Advanced("test2")
        bf = BattleField()
        with self.assertRaises(ValueError) as ex:
            bf.fight(p1, p2)
        self.assertEqual(str(ex.exception), "Player is dead!")

    def test_enemy_is_dead(self):
        p1 = Advanced("test")
        p2 = Advanced("test2")
        p2.health = 0
        bf = BattleField()
        with self.assertRaises(ValueError) as ex:
            bf.fight(p1, p2)
        self.assertEqual(str(ex.exception), "Player is dead!")

    def test_damage_points_and_health_increased_without_cards(self):
        p1 = Advanced("test")
        beginner = Beginner("test2")
        bf = BattleField()
        bf.fight(p1, beginner)
        self.assertEqual(p1.health, 250)
        self.assertEqual(beginner.health, 90)

    def test_health_increased_from_cards(self):
        p1 = Advanced("test")
        beginner = Beginner("test2")
        bf = BattleField()

        magic = TrapCard("magiccard")
        p1.card_repository.add(magic)
        magic = TrapCard("magiccard2")
        p1.card_repository.add(magic)
        magic = TrapCard("magiccard3")
        p1.card_repository.add(magic)
        trap = MagicCard("trapcard")
        beginner.card_repository.add(trap)

        with self.assertRaises(ValueError) as ex:
            bf.fight(p1, beginner)
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")
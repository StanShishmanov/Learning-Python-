import unittest

from project.controller import Controller


class TestController(unittest.TestCase):

    def setUp(self) -> None:
        self.controller = Controller()

    def test_add_player(self):
        self.assertEqual(self.controller.player_repository.count, 0)
        self.assertEqual(self.controller.card_repository.count, 0)
        res = self.controller.add_player("Beginner", "test")
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(self.controller.card_repository.count, 0)
        self.assertEqual(res, f"Successfully added player of type Beginner with username: test")

    def test_add_card(self):
        self.assertEqual(self.controller.player_repository.count, 0)
        self.assertEqual(self.controller.card_repository.count, 0)
        res = self.controller.add_card("Magic", "test")
        self.assertEqual(self.controller.player_repository.count, 0)
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(res, f"Successfully added card of type MagicCard with name: test")

    def test_player_add_card(self):
        self.assertEqual(self.controller.card_repository.count, 0)
        self.assertEqual(self.controller.player_repository.count, 0)
        self.controller.add_card("Magic", "testcard")
        self.controller.add_player("Beginner", "test")
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(self.controller.player_repository.count, 1)
        res = self.controller.add_player_card("test", "testcard")
        self.assertEqual(res, f"Successfully added card: testcard to user: test")

    def test_fight(self):
        self.controller.add_player("Beginner", "beginner")
        self.controller.add_player("Advanced", "advanced")
        res = self.controller.fight("advanced", "beginner")
        self.assertEqual(res, f"Attack user health 250 - Enemy user health 90")

    def test_report(self):
        self.controller.add_player("Beginner", "beginner")
        self.controller.add_player("Advanced", "advanced")
        self.controller.add_card("Magic", "test")
        self.controller.add_player_card("beginner", "test")
        res = self.controller.report()
        self.assertEqual(res, f"Username: beginner - Health: 50 - Cards 1\n### Card: test - Damage: 5\nUsername: advanced - Health: 250 - Cards 0\n")
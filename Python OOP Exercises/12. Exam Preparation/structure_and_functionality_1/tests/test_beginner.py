import unittest

from project.player.beginner import Beginner


class TestABeginner(unittest.TestCase):
    def test_set_attr(self):
        beginner = Beginner("test")
        self.assertEqual(beginner.username, "test")
        self.assertEqual(beginner.health, 50)
        self.assertEqual(beginner.card_repository.__class__.__name__,  "CardRepository")
        self.assertFalse(beginner.is_dead)

    def test_username_raises(self):
        with self.assertRaises(ValueError) as ex:
            advanced = Beginner("")
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_health_raises(self):
        beginner = Beginner("test")
        with self.assertRaises(ValueError) as ex:
            beginner.health = -2
            self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_is_dead(self):
        beginner = Beginner("test")
        self.assertFalse(beginner.is_dead)
        beginner.health = 0
        self.assertTrue(beginner.is_dead)

    def test_take_damage_raises(self):
        beginner = Beginner("test")
        with self.assertRaises(ValueError) as ex:
            beginner.take_damage(-5)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_take_damage(self):
        beginner = Beginner("test")
        beginner.take_damage(30)
        self.assertEqual(beginner.health, 20)
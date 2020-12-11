import unittest

from project.card.trap_card import TrapCard

from project.card.card_repository import CardRepository


class TestCardRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.cr = CardRepository()

    def test_set_attr(self):
        self.assertEqual(self.cr.count, 0)
        self.assertEqual(len(self.cr.cards), 0)

    def test_add_raises(self):
        c = TrapCard("test")
        self.cr.add(c)
        with self.assertRaises(ValueError) as ex:
            self.cr.add(c)
        self.assertEqual(str(ex.exception), f"Card {c.name} already exists!")

    def test_add(self):
        c = TrapCard("test")
        self.cr.add(c)
        self.assertEqual(self.cr.count, 1)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cr.remove("")
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_remove(self):
        c = TrapCard("test")
        self.cr.add(c)
        self.assertEqual(self.cr.count, 1)
        self.cr.remove("test")
        self.assertEqual(self.cr.count, 0)

    def test_find(self):
        p = TrapCard("test")
        self.cr.add(p)
        result = self.cr.find("test")
        self.assertEqual(result.name, "test")
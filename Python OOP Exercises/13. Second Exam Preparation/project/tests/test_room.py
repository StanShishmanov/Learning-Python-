import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("test", 3, 1)
        for attr in ['family_name', 'budget', "members_count", 'children', 'expenses']:
            self.assertTrue(hasattr(self.room, attr))

        self.assertEqual('test', self.room.family_name)
        self.assertEqual(3, self.room.budget)
        self.assertEqual(1, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_with_negative_amounts_should_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
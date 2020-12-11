import unittest
from project.person import Group, Person


class TestGroup(unittest.TestCase):

    def setUp(self) -> None:
        self.person = Person("John", "Lennon")
        self.person2 = Person("Michael", "Jordan")
        self.group = Group("Special", [self.person, self.person2])

        self.p1 = Person("Adam", "Sandal")
        self.p2 = Person("Johann", "Strauss")
        self.p3 = Person("Freddie", "Mercury")
        self.group2 = Group("VIP", [self.p1, self.p2, self.p3])

        self.group3 = self.group + self.group2

    def test_custom_name(self):
        result = self.group.name
        expected_result = "Special"
        self.assertEqual(result, expected_result)

    def test_custom_length(self):
        result = len(self.group)
        expected_result = 2
        self.assertEqual(result, expected_result)

    def test_custom_add_group_length(self):
        result = len(self.group3)
        expected_result = 5
        self.assertEqual(result, expected_result)

    def test_custom_add_group_name(self):
        result = self.group3.name
        expected_result = "SpecialVIP"
        self.assertEqual(result, expected_result)

    def test_custom_repr(self):
        result = repr(self.group)
        expected_result = f"Group Special with members John Lennon, Michael Jordan"
        self.assertEqual(result, expected_result)

    def test_custom_getItem(self):
        result = self.group[1]
        self.assertIn("Person 1:", result)

    def test_custom_get_item_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.group[2]

    def test_custom_str(self):
        result = str(self.group)
        expected = f"Group Special with members John Lennon, Michael Jordan"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
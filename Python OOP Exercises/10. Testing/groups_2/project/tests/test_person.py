import unittest

from project.person import Person


class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        self.person = Person("John", "Lennon")
        self.person2 = Person("Michael", "Jordan")

    def test_correct_name_addition(self):
        person3 = self.person + self.person2
        result = person3.name + ' ' + person3.surname
        expected_result = "John Jordan"
        self.assertEqual(result, expected_result)

    def test_custom_str(self):
        result = str(self.person)
        expected = "John Lennon"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
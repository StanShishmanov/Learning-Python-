import unittest
from project.custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def setUp(self):
        self.custom_list = CustomList(0, 1, 2, 44, 4, 5, 6, 7)

    def test_custom_get_item(self):
        result = self.custom_list.__getitem__(3)
        expected = 44
        self.assertEqual(expected, result)

    def test_custom_repr(self):
        result = repr(self.custom_list)
        expected = "0, 1, 2, 44, 4, 5, 6, 7"
        self.assertEqual(expected, result)

    def test_check_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.custom_list.check_index(15)

    def test_check_index_returns_true(self):
        result = self.custom_list.check_index(5)
        self.assertEqual(True, result)

    def test_custom_append(self):
        self.custom_list.append(8)
        result = len(self.custom_list)
        expected = 9
        self.assertEqual(expected, result)

    def test_custom_remove(self):
        self.custom_list.remove(3)
        result = len(self.custom_list)
        expected = 7
        self.assertEqual(expected, result)

    def test_custom_get(self):
        result = self.custom_list.get(3)
        expected = 44
        self.assertEqual(expected, result)

    def test_custom_extend(self):
        new_list = self.custom_list.extend([123, 456, 789])
        result = new_list[9]
        expected = 456
        self.assertEqual(result, expected)

    def test_custom_insert(self):
        self.custom_list.insert(0, 1564)
        result = self.custom_list[0]
        expected = 1564
        self.assertEqual(result, expected)

    def test_custom_pop(self):
        result = self.custom_list.pop()
        expected = 7
        self.assertEqual(result, expected)

    def test_custom_clear(self):
        self.custom_list.clear()
        result = len(self.custom_list)
        expected = 0
        self.assertEqual(result, expected)

    def test_custom_index(self):
        result = self.custom_list.index(44)
        expected = 3
        self.assertEqual(result, expected)

    def test_custom_count(self):
        self.custom_list = [1, 2, 3, 44, 55, 44, 33]
        result = self.custom_list.count(44)
        expected = 2
        self.assertEqual(result, expected)

    def test_custom_reverse(self):
        result = self.custom_list.reverse()
        expected = self.custom_list[::-1]
        self.assertEqual(expected, result)

    def test_custom_copy(self):
        result = self.custom_list.copy()
        self.assertFalse(isinstance(result, self.custom_list.__class__))

    def test_size(self):
        result = self.custom_list.size()
        expected = 8
        self.assertEqual(expected, result)

    def test_add_first(self):
        self.custom_list.add_first(99)
        result = self.custom_list[0]
        expected = 99
        self.assertEqual(expected, result)

    def test_dictionize(self):
        custom_list = CustomList(0, 1, 2, 44, 4, 5, 6, 7, 8)
        result = custom_list.dictionize()
        expected = {
            0: 1,
            2: 44,
            4: 5,
            6: 7,
            8: " "
        }
        self.assertDictEqual(expected, result)

    def test_move(self):
        result = self.custom_list.move(2)
        expected = [2, 44, 4, 5, 6, 7, 0, 1]
        self.assertEqual(expected, result)

    def test_custom_sum(self):
        custom_list = CustomList(1, 2, 3, "two")
        result = custom_list.sum()
        expected = 9
        self.assertEqual(expected, result)

    def test_overbound(self):
        result = self.custom_list.overbound()
        expected = 3
        self.assertEqual(expected, result)

    def test_underbound(self):
        result = self.custom_list.underbound()
        expected = 0
        self.assertEqual(expected, result)

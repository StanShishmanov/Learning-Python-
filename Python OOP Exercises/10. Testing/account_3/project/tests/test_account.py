import unittest

from project.account2 import Account

import unittest


class TestACcount(unittest.TestCase):

    def setUp(self) -> None:
        self.account = Account("Mary", 50)
        self.account2 = Account("Bob", 0)
        self.account3 = Account("Mary&Bob", 50)

    def test_custom_str(self):
        result = str(self.account)
        expected = "Account of Mary with starting amount: 50"
        self.assertEqual(result, expected)

    def test_custom_repr(self):
        result = repr(self.account)
        expected = "Account(Mary, 50)"
        self.assertEqual(result, expected)

    def test_custom_len(self):
        self.account._transactions.append(50)
        self.account._transactions.append(150)
        self.account._transactions.append(250)
        result = len(self.account._transactions)
        expected = 3
        self.assertEqual(result, expected)

    def test_balance_property(self):
        self.assertEqual(self.account.balance, 50)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 100)

    def test_custom_iter(self):
        self.account.add_transaction(50)
        self.account.add_transaction(50)
        for t in self.account:
            self.assertEqual(t, 50)

    def test_custom_get_item(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        result = self.account[1]
        self.assertEqual(result, 150)

    def test_custom_reversed(self):
        self.account._transactions.append(50)
        self.account._transactions.append(150)
        self.account._transactions.append(250)
        result = list(reversed(self.account._transactions))
        expected = [250, 150, 50]
        self.assertEqual(result, expected)

    def test_custom_gt(self):
        self.assertGreater(self.account.amount, self.account2.amount)

    def test_custom_lt(self):
        self.assertLess(self.account2.amount, self.account.amount)

    def test_custom_ge(self):
        self.assertGreaterEqual(self.account.amount, self.account2.amount)
        self.assertGreaterEqual(self.account.amount, self.account3.amount)

    def test_custom_le(self):
        self.assertLessEqual(self.account2.amount, self.account.amount)
        self.assertLessEqual(self.account2.amount, 0)

    def test_custom_eq(self):
        self.assertEqual(self.account.amount, self.account3.amount)

    def test_custom_ne(self):
        self.assertNotEqual(self.account.amount, self.account2.amount)

    def test_custom_add(self):
        new_acc = Account('&'.join([self.account.owner, self.account2.owner]), self.account.amount + self.account2.amount)
        new_acc._transactions = self.account._transactions + self.account2._transactions
        expected_account_name = "Mary&Bob"
        expected_account_amount = 50
        expected_account_transactions = 0
        self.assertEqual(expected_account_name, new_acc.owner)
        self.assertEqual(expected_account_amount, new_acc.amount)
        self.assertEqual(expected_account_transactions, len(new_acc._transactions))

    def test_add_transaction_value_error(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction("not an int")

    def test_add_transaction_len_transactions(self):
        self.account.add_transaction(50)
        self.account.add_transaction(40)
        self.account.add_transaction(30)
        result = len(self.account._transactions)
        expected = 3
        self.assertEqual(result, expected)

    def test_validate_transaction_value_error(self):
        with self.assertRaises(ValueError):
            self.account.validate_transaction(self.account2, -100)

    def test_validate_transaction_negative_amount(self):
        self.account.validate_transaction(self.account, -50)
        result = self.account.balance
        expected = 0
        self.assertEqual(result, expected)

    def test_validate_transaction_len_transaction(self):
        self.account.validate_transaction(self.account, 50)
        result = len(self.account._transactions)
        expected = 1
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

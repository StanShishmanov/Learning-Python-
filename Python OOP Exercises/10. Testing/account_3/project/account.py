class Account:
    def __init__(self, owner: str, *args):
        self.owner = owner
        if args:
            self.amount = args[0]
        else:
            self.amount = 0
        self.start_amount = self.amount
        self._transactions = []

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.start_amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.start_amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        for elem in self._transactions[::-1]:
            yield int(elem)

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __add__(self, other):
        new_acc = Account('&'.join([self.owner, other.owner]), self.start_amount + other.start_amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.amount += amount
        self._transactions.append(amount)

    @property
    def balance(self):
        total = sum(self._transactions) + self.start_amount
        return total

    def validate_transaction(self, account, amount_to_add):
        if self.amount >= amount_to_add:
            account.add_transaction(amount_to_add)
            self.add_transaction(self.amount - amount_to_add)
            self.amount -= amount_to_add
            return "New balance: {account_ballance}"
        raise ValueError("sorry cannot go in debt!")

#
# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(acc.balance)
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)

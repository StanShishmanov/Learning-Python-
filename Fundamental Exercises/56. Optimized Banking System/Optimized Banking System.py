import operator

class BankAccount:

    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = float(balance)

data = input()
accounts = []
while not data == "end":
    bank = data.split(' | ')[0]
    name = data.split(' | ')[1]
    balance = float(data.split(' | ')[2])
    new_account = BankAccount(name, bank, balance)
    accounts.append(new_account)
    data = input()

s = sorted(accounts, key=lambda x: (-x.balance, len(x.bank)))

for acc in s:
    balance = acc.balance
    bank = acc.bank
    name = acc.name
    print(f'{name} -> {balance:.2f} ({bank})')

""""
DSK | Ivan | 504.403
DSK | Pesho | 2000.4031
DSK | Aleksander | 20000.0001
Piraeus | Ivan | 504.403
Piraeus | Aleksander | 20000.0001
"""
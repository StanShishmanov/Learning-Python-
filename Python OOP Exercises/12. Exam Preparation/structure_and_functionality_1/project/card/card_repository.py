from project.card.card import Card


class CardRepository:

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card in self.cards:
            raise ValueError(f"Card {card.name} already exists!")
        else:
            self.cards.append(card)
            self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        else:
            self.cards.remove(self.find(card))
            self.count -= 1

    def find(self, name: str):
        c = [c for c in self.cards if c.name == name][0]
        return c


# p = MagicCard("test")
#
# pr = CardRepository()
# pr.add(p)
# print(pr.count)
# pr.remove("test")
# print(pr.count)
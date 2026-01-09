import random

class Decks:
    def __init__(self, count=1):
        card_names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.single_deck_reference =  card_names.copy() + card_names.copy() + card_names.copy() + card_names.copy()

        self.undealt = []
        self.dealt = []
        for _ in range(count):
            self.undealt.extend(self.single_deck_reference.copy())
        self.shuffle()

    def shuffle(self):
        self.undealt.extend(self.dealt)
        self.dealt.clear()
        random.shuffle(self.undealt)

    def deal_cards(self, hand, count=1):
        for _ in range(count):
            card = self.undealt.pop()
            hand.append(card)
            self.dealt.append(card)

# Fixed
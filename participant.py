class Participant:
    def __init__(self):
        self.hand = []
        self.finished = False
        self.busted_forfeited = False
        self.bet_multiplier = 1
        self.winnings = 0

    def draw(self, deck):
        deck.deal_cards(self.hand, 1)

    def get_hand_value(self):
        value = 0
        aces = 0

        for card in self.hand:
            if card == "A":
                aces += 1
                value += 11
            elif card in ("K", "Q", "J"):
                value += 10
            else:
                value += int(card)

        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        is_soft = aces > 0
        return value, is_soft

    def has_blackjack(self):
        return len(self.hand) == 2 and self.get_hand_value()[0] == 21

    def hit(self, deck):
        self.draw(deck)
        if self.check_bust():
            self.busted_forfeited = True
            self.finished = True

    def stand(self):
        self.finished = True

    def check_bust(self):
        if self.get_hand_value()[0] > 21:
            return True
        return False

    def reset(self):
        self.hand = []
        self.busted_forfeited = False
        self.finished = False
        self.bet_multiplier = 1



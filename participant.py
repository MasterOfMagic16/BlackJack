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
        soft = False
        for card in self.hand:
            if card == "A":
                value += 1
            elif card == "2":
                value += 2
            elif card == "3":
                value += 3
            elif card == "4":
                value += 4
            elif card == "5":
                value += 5
            elif card == "6":
                value += 6
            elif card == "7":
                value += 7
            elif card == "8":
                value += 8
            elif card == "9":
                value += 9
            elif card == "10":
                value += 10
            elif card == "J":
                value += 10
            elif card == "Q":
                value += 10
            elif card == "K":
                value += 10
        for card in self.hand:
            if card == "A" and value <= 11:
                value += 10
                soft = True
        return value, soft

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



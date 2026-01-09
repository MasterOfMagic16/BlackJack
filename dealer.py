from participant import Participant

class Dealer(Participant):
    def decide(self, deck):
        value, is_soft = self.get_hand_value()
        if value < 17:
            self.hit(deck)
        elif value == 17 and is_soft:
            # Stand on soft 17, changeable
            self.stand()
        else:
            self.stand()

    def get_upcard_value(self):
        card = self.hand[0]
        if card == "A":
            return 11
        if card in ("J", "Q", "K"):
            return 10
        return int(card)

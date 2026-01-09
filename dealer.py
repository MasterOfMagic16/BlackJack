from participant import Participant

class Dealer(Participant):
    def decide(self, deck):
        if self.get_hand_value()[0] < 17:
            self.hit(deck)
        else:
            self.stand()

        # TODO: Stand on soft 17 vs not

    def get_upcard_value(self):
        card = self.hand[0]
        value = 0
        if card == "A":
            value += 11
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
        return value

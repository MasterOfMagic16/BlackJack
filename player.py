from participant import Participant
from strategy import *


class Player(Participant):

    def decide(self, deck, dealer):
        dealer_value = dealer.get_upcard_value()
        player_value, is_soft = self.get_hand_value()
        is_pair = len(self.hand) == 2 and self.hand[0] == self.hand[1]

        if is_pair:
            action = PAIRS.get((player_value // 2, dealer_value))
        elif is_soft:
            action = SOFT_TOTALS.get((player_value, dealer_value))
        else:
            action = HARD_TOTALS.get((player_value, dealer_value))

        if action == S:
            self.stand()
        elif action == H:
            self.hit(deck)
        elif action == D or action == DH or action == DS:
            if len(self.hand) == 2:
                self.double_down(deck)
            else:
                self.hit(deck)
        elif action == SP:
            self.split()
        elif action == SU:
            self.surrender()
        else:
            print("Fallback")
            self.hit(deck)  # safe fallback

    def double_down(self, deck):
        self.bet_multiplier *= 2
        self.hit(deck)
        self.finished = True

    def split(self):
        self.stand()
        # TODO: Not Implemented

    def surrender(self):
        self.bet_multiplier = .5
        self.busted_forfeited = True
        self.finished = True
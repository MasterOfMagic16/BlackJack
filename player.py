from participant import Participant

H  = "HIT"
S  = "STAND"
D  = "DOUBLE"
DS = "DOUBLE_OR_STAND"
DH = "DOUBLE_OR_HIT"
SP = "SPLIT"
SU = "SURRENDER"

HARD_TOTALS = {
    # 17–20
    (17, 2): S, (17, 3): S, (17, 4): S, (17, 5): S, (17, 6): S,
    (17, 7): S, (17, 8): S, (17, 9): S, (17, 10): S, (17, 11): S,

    (16, 2): S, (16, 3): S, (16, 4): S, (16, 5): S, (16, 6): S,
    (16, 7): H, (16, 8): H, (16, 9): SU, (16, 10): SU, (16, 11): SU,

    (15, 2): S, (15, 3): S, (15, 4): S, (15, 5): S, (15, 6): S,
    (15, 7): H, (15, 8): H, (15, 9): H, (15, 10): SU, (15, 11): H,

    # 13–14
    **{(13, d): S for d in range(2, 7)},
    **{(14, d): S for d in range(2, 7)},
    **{(13, d): H for d in range(7, 12)},
    **{(14, d): H for d in range(7, 12)},

    # 12
    **{(12, d): H for d in (2, 3)},
    **{(12, d): S for d in (4, 5, 6)},
    **{(12, d): H for d in range(7, 12)},

    # 9–11
    (11, 2): D, (11, 3): D, (11, 4): D, (11, 5): D, (11, 6): D,
    (11, 7): D, (11, 8): D, (11, 9): D, (11, 10): D, (11, 11): D,

    (10, 2): D, (10, 3): D, (10, 4): D, (10, 5): D, (10, 6): D,
    (10, 7): D, (10, 8): D, (10, 9): D, (10, 10): H, (10, 11): H,

    (9, 2): H, (9, 3): DH, (9, 4): DH, (9, 5): DH, (9, 6): DH,
    (9, 7): H, (9, 8): H, (9, 9): H, (9, 10): H, (9, 11): H,
}

SOFT_TOTALS = {
    # A,9
    **{(20, d): S for d in range(2, 12)},

    # A,8
    **{(19, d): S for d in range(2, 7)},
    **{(19, d): DS for d in (7,8)},
    **{(19, d): S for d in range(8, 12)},

    # A,7
    **{(18, d): DS for d in range(2, 7)},
    **{(18, d): S for d in (7, 8)},
    **{(18, d): H for d in range(9, 12)},

    # A,6
    **{(17, d): DH for d in range(3, 7)},
    **{(17, d): H for d in (2, 7, 8, 9, 10, 11)},

    # A,4–A,5
    **{(15, d): DH for d in range(4, 7)},
    **{(16, d): DH for d in range(4, 7)},
    **{(15, d): H for d in (2, 3, 7, 8, 9, 10, 11)},
    **{(16, d): H for d in (2, 3, 7, 8, 9, 10, 11)},

    # A,2–A,3
    **{(13, d): DH for d in range(5, 7)},
    **{(14, d): DH for d in range(5, 7)},
    **{(13, d): H for d in (2, 3, 4, 7, 8, 9, 10, 11)},
    **{(14, d): H for d in (2, 3, 4, 7, 8, 9, 10, 11)},
}

PAIRS = {
    # A,A
    **{(11, d): SP for d in range(2, 12)},

    # 10,10
    **{(10, d): S for d in range(2, 12)},

    # 9,9
    **{(9, d): SP for d in range(2, 7)},
    **{(9, d): S for d in (7,)},
    **{(9, d): SP for d in (8, 9)},
    **{(9, d): S for d in (10, 11)},

    # 8,8
    **{(8, d): SP for d in range(2, 12)},

    # 7,7
    **{(7, d): SP for d in range(2, 8)},
    **{(7, d): H for d in range(8, 12)},

    # 6,6
    **{(6, d): SP for d in range(2, 7)},
    **{(6, d): H for d in range(7, 12)},

    # 5,5
    **{(5, d): DH for d in range(2, 10)},
    **{(5, d): H for d in (10, 11)},

    # 4,4
    **{(4, d): SP for d in (5, 6)},
    **{(4, d): H for d in (2, 3, 4, 7, 8, 9, 10, 11)},

    # 2,2 & 3,3
    **{(2, d): SP for d in range(2, 8)},
    **{(3, d): SP for d in range(2, 8)},
    **{(2, d): H for d in range(8, 12)},
    **{(3, d): H for d in range(8, 12)},
}



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
        elif action == D:
            self.double_down(deck)
        elif action == DH or action == DS:
            self.double_down(deck)
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

    def split(self):
        self.stand()
        # TODO: Not Implemented

    def surrender(self):
        self.bet_multiplier = .5
        self.busted_forfeited = True
        self.finished = True
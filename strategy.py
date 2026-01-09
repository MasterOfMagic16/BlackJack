# strategy.py
# Basic Strategy tables (S17, DAS assumed; split handling deferred)

H  = "HIT"
S  = "STAND"
D  = "DOUBLE"
DS = "DOUBLE_OR_STAND"
DH = "DOUBLE_OR_HIT"
SP = "SPLIT"
SU = "SURRENDER"


# -------------------------------------------------------------------
# HARD TOTALS (excluding pairs)
# Keys: (player_total, dealer_upcard) where dealer_upcard: 2..11 (A=11)
# -------------------------------------------------------------------

HARD_TOTALS = {
    # 17–20
    **{(17, d): S for d in range(2, 12)},
    **{(18, d): S for d in range(2, 12)},
    **{(19, d): S for d in range(2, 12)},
    **{(20, d): S for d in range(2, 12)},

    # 16
    **{(16, d): S for d in range(2, 7)},
    **{(16, d): H for d in (7, 8)},
    **{(16, d): SU for d in (9, 10, 11)},

    # 15
    **{(15, d): S for d in range(2, 7)},
    **{(15, d): H for d in (7, 8, 9)},
    **{(15, 10): SU},
    **{(15, 11): H},

    # 13–14
    **{(13, d): S for d in range(2, 7)},
    **{(14, d): S for d in range(2, 7)},
    **{(13, d): H for d in range(7, 12)},
    **{(14, d): H for d in range(7, 12)},

    # 12
    **{(12, d): H for d in (2, 3)},
    **{(12, d): S for d in (4, 5, 6)},
    **{(12, d): H for d in range(7, 12)},

    # 11
    **{(11, d): D for d in range(2, 12)},

    # 10
    **{(10, d): D for d in range(2, 10)},
    **{(10, d): H for d in (10, 11)},

    # 9
    **{(9, d): DH for d in (3, 4, 5, 6)},
    **{(9, d): H for d in (2, 7, 8, 9, 10, 11)},
}


# -------------------------------------------------------------------
# SOFT TOTALS
# player_total already includes Ace counted as 11
# -------------------------------------------------------------------

SOFT_TOTALS = {
    # A,9 (20)
    **{(20, d): S for d in range(2, 12)},

    # A,8 (19)
    **{(19, d): S for d in range(2, 7)},
    **{(19, 7): DS},
    **{(19, d): S for d in range(8, 12)},

    # A,7 (18)
    **{(18, d): DS for d in range(2, 7)},
    **{(18, d): S for d in (7, 8)},
    **{(18, d): H for d in range(9, 12)},

    # A,6 (17)
    **{(17, d): DH for d in range(3, 7)},
    **{(17, d): H for d in (2, 7, 8, 9, 10, 11)},

    # A,5 (16)
    **{(16, d): DH for d in range(4, 7)},
    **{(16, d): H for d in (2, 3, 7, 8, 9, 10, 11)},

    # A,4 (15)
    **{(15, d): DH for d in range(4, 7)},
    **{(15, d): H for d in (2, 3, 7, 8, 9, 10, 11)},

    # A,3 (14)
    **{(14, d): DH for d in (5, 6)},
    **{(14, d): H for d in (2, 3, 4, 7, 8, 9, 10, 11)},

    # A,2 (13)
    **{(13, d): DH for d in (5, 6)},
    **{(13, d): H for d in (2, 3, 4, 7, 8, 9, 10, 11)},
}


# -------------------------------------------------------------------
# PAIRS
# pair_value is the numeric value of ONE card in the pair
# (A,A uses 11)
# -------------------------------------------------------------------

PAIRS = {
    # A,A
    **{(11, d): SP for d in range(2, 12)},

    # 10,10
    **{(10, d): S for d in range(2, 12)},

    # 9,9
    **{(9, d): SP for d in range(2, 7)},
    **{(9, 7): S},
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

    # 3,3
    **{(3, d): SP for d in range(2, 8)},
    **{(3, d): H for d in range(8, 12)},

    # 2,2
    **{(2, d): SP for d in range(2, 8)},
    **{(2, d): H for d in range(8, 12)},
}

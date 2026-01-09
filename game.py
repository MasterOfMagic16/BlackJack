from dealer import Dealer
from player import Player
from deck import Decks

class Game:
    def __init__(self, deck_count=1):
        self.player = Player()
        self.dealer = Dealer()
        self.decks = Decks(deck_count)

    def play_round(self, bet=10):
        self.player.reset()
        self.dealer.reset()
        self.deal()
        while not self.player.finished:
            self.player.decide(self.decks, self.dealer)
        while not self.dealer.finished:
            self.dealer.decide(self.decks)
        self.player.winnings += self.get_net_winnings(bet)

    def get_net_winnings(self, bet):
        if self.player.busted_forfeited:
            print("Busted/Forfeited")
            return -bet
        if self.player.get_hand_value()[0] > 21:
            return -bet
        if self.dealer.get_hand_value()[0] > 21:
            return bet * self.player.bet_multiplier
        if self.player.get_hand_value() > self.dealer.get_hand_value():
            print(">")
            return bet * self.player.bet_multiplier
        if self.player.get_hand_value() == self.dealer.get_hand_value():
            print("Tie")
            return 0
        return -bet

    def deal(self):
        self.decks.shuffle()
        self.decks.deal_cards(self.player.hand, 1)
        self.decks.deal_cards(self.dealer.hand, 1)
        self.decks.deal_cards(self.player.hand, 1)
        self.decks.deal_cards(self.dealer.hand, 1)
        if self.player.get_hand_value() == 21 and not self.dealer.get_hand_value() == 21:
            print("Nat Blackjack")
            self.player.bet_multiplier = 1.5
            self.player.finished = True
            self.dealer.finished = True


    def decide(self):
        self.dealer.hit(self.decks)
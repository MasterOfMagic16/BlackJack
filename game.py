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
        p_val = self.player.get_hand_value()[0]
        d_val = self.dealer.get_hand_value()[0]

        if self.player.busted_forfeited:
            print("Busted/Forfeited")
            return -bet
        if p_val > 21:
            return -bet
        if d_val > 21:
            return bet * self.player.bet_multiplier
        if p_val > d_val:
            print("Player beats dealer")
            return bet * self.player.bet_multiplier
        if p_val == d_val:
            print("Tie")
            return 0
        print("Dealer beats player")
        return -bet

    def deal(self):
        self.decks.shuffle()
        self.decks.deal_cards(self.player.hand, 1)
        self.decks.deal_cards(self.dealer.hand, 1)
        self.decks.deal_cards(self.player.hand, 1)
        self.decks.deal_cards(self.dealer.hand, 1)

        player_natural = self.player.has_blackjack()
        dealer_natural = self.dealer.has_blackjack()

        if player_natural and not dealer_natural:
            print("Nat Blackjack (player)")
            self.player.bet_multiplier = 1.5
            self.player.finished = True
            self.dealer.finished = True
        elif player_natural and dealer_natural:
            print("Both have naturals (push)")
            # Both finished; push -> no change to multiplier/winnings
            self.player.finished = True
            self.dealer.finished = True
        elif dealer_natural and not player_natural:
            print("Nat Blackjack (dealer)")
            self.player.finished = True
            self.dealer.finished = True

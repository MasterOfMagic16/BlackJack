from game import Game

game_instance = Game()

game_instance.play_round(bet=10)

print(game_instance.player.hand)
print(game_instance.dealer.hand)
print(game_instance.player.winnings)
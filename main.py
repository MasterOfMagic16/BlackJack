from game import Game
import matplotlib.pyplot as plt


rounds = 1000


game_instance = Game()
time_list = []
winnings_list = []

time_step = 1
while time_step <= rounds:
    game_instance.play_round(bet=10)
    time_list.append(time_step)
    winnings_list.append(game_instance.player.winnings)
    time_step += 1

plt.figure()
plt.plot(time_list, winnings_list)
plt.xlabel("Number of Hands Played")
plt.ylabel("Cumulative Winnings")
plt.title("Blackjack Winnings vs Time (Basic Strategy)")
plt.grid(True)
plt.show()
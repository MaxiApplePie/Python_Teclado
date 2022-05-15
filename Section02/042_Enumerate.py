# friends = ['Rolf', 'Jen', 'Anna', 'Eric']
#
# for counter, friend in enumerate(friends):
#     print(str(counter) + ' ' + friend)
#
# print(dict(enumerate(friends, start=1)))
#
# numbers = list(range(10))
# doubled = [n*2 for n in numbers]
# print(doubled)

import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))


# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
match_players = dict()

for player in players:
    match_players[player['name']] = len(player['numbers'].intersection(lottery_numbers))
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
winner_name = ""
winner_score = 0
for player, score in match_players.items():
    if score > winner_score:
        winner_name = player
        winner_score = score

print(f"{winner_name} won {winner_score * 100}.")

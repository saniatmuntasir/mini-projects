print("----- Welcome to Snake-Ludo Game -----")
import random
def roll():
    min_val = 1
    max_val = 6
    rolled_value = random.randint(min_val, max_val)
    return rolled_value

while True:
    players = input("Enter the number of players(1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1-4 players")
    else:
        print("invalid, try again!")
print("No. of Players:",players)

max_score = 100
player_score = [0 for i in range(players)]
print("Score Board:",player_score)

while max(player_score) < max_score:
    for player_idx in range(players):
        print('\nPlayer Number', player_idx+1,'turn has just started!')
        while True:
            should_roll = input("Would you like to roll(y)?:")
            if should_roll.lower() == "y":
                break
            else:
                print("Press 'y' to roll")
                continue

        ladder_values = [6,8,26,50,55,59]
        snake_values = [32,60,63,70,73,82,89,97]
        value = roll()
        player_score[player_idx] += value

        if player_score[player_idx] in ladder_values:
            print("You rolled a", value)
            player_score[player_idx] = player_score[player_idx] + 10
            print("Wow! You found a ladder. You have earned 10 points!")
        elif player_score[player_idx] in snake_values:
            print("You rolled a", value)
            player_score[player_idx] = player_score[player_idx] -15
            print("Oh no! You stepped on a Snake! You have lost 15 points!")
        else:
            print("You rolled a", value)

        print("Player Number", player_idx+1 ,"score is:" ,player_score[player_idx])
        print("Score Board:", player_score)

        if player_score[player_idx] >= 100:
            print("----- Player", player_idx+1, "Won -----")
            break



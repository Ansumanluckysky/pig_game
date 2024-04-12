import random

MAX_SCORE = 50
MIN_PLAYERS = 2
MAX_PLAYERS = 4
DICE_MIN_VALUE = 1
DICE_MAX_VALUE = 6


def get_number_of_players():
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit():
            players = int(players)
            if MIN_PLAYERS <= players <= MAX_PLAYERS:
                return players
            else:
                print("Must be between 2 - 4 players.")
        else:
            print("Invalid input, please enter a number.")


def roll_dice():
    return random.randint(DICE_MIN_VALUE, DICE_MAX_VALUE)


def player_turn(player_idx):
    current_score = 0
    print("\nPlayer number", player_idx + 1, "turn has just started!")
    print("Your total score is:", player_scores[player_idx], "\n")
    while True:
        should_roll = input("Would you like to roll (y/n)? ").lower()
        if should_roll != "y":
            break

        value = roll_dice()
        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            current_score += value
            print("You rolled a:", value)
            print("Your score is:", current_score)

    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])


def determine_winner():
    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)


def play_game():
    players = get_number_of_players()
    global player_scores
    player_scores = [0] * players

    while max(player_scores) < MAX_SCORE:
        for player_idx in range(players):
            player_turn(player_idx)

    determine_winner()


if __name__ == "__main__":
    play_game()

"""
number of players fixed to 4
input variables: grid size
the player who reaches the highest position as per the grid size wins
program terminates when the player reaches the highest position

game flow steps:
step 1:
rolling ice
step 2:
check dice side value
step 3:
move the player to the new position
step 4:
check if the player has reached the highest
step 5:
after steps of grid we alternate either from left to right or right to left
step 6:
check two dimension position for the player and record the position
step 7:
add the position history in dataframe
"""
import random
import pandas as pd

# global variables
play_history = []
players = []
current_position = []
# current_position = []
grid_size = int(input('enter the grid size: '))
highest_position = grid_size * grid_size
number_of_players = 4


def roll_dice_():
    """
    function to roll the dice
    """
    dice_roll = random.randint(1, 6)
    return dice_roll


def play_turn(player_position, dice_roll):
    """
    function to play a turn
    """
    player_position += dice_roll
    return player_position


def create_players_():
    """creating players list """
    for player in range(1, number_of_players + 1):
        players.append(player)
        current_position.append(0)
        play_history.append({
            'players': player, 'dice_roll_history': [], 'position_history': [], 'win_status': False,
            'two_d_position_history': []

        })


def check_even_(player_position_y):
    """
    check if y axis is even
    """
    if player_position_y % 2 == 0:
        return True
    else:
        return False


def create_two_d_from_position_(player_position):
    """
    creating two d position from player position
    """
    player_position_y = (player_position // grid_size) + 1
    if check_even_(player_position_y):
        player_position_x = player_position % grid_size
        if player_position_x == 0 and player_position != 0:
            player_position_x = 1
        if player_position == 0:
            player_position_x = 1
        two_d_position = player_position_x, player_position_y
    else:
        player_position_x = player_position % grid_size
        if player_position_x == 0 and player_position != 0:
            player_position_x = grid_size
        if player_position == 0:
            player_position_x = 1
        two_d_position = player_position_x, player_position_y
    return list(two_d_position)


def starting_game():
    """
    function to start the game
    """
    create_players_()
    index = None
    while True:
        for index in range(number_of_players):
            dice_roll = roll_dice_()
            two_d_position = create_two_d_from_position_(player_position=current_position[index])
            if play_turn(current_position[index], dice_roll) > highest_position:
                play_history[index]['position_history'].append(current_position[index])
                play_history[index]['dice_roll_history'].append(dice_roll)
                play_history[index]['two_d_position_history'].append(two_d_position)
                continue
            else:
                current_position[index] = play_turn(current_position[index], dice_roll)
                play_history[index]['position_history'].append(current_position[index])
                play_history[index]['dice_roll_history'].append(dice_roll)
                play_history[index]['two_d_position_history'].append(two_d_position)
                if current_position[index] == highest_position:
                    play_history[index]['win_status'] = True
                    print(f"player {play_history[index]['players']} has won the game")
                    break
        if current_position[index] == highest_position:
            break

    # output the game history in a dataframe
    df = pd.DataFrame(play_history)
    print(df.to_string())


if __name__ == "__main__":
    starting_game()
    print("players", players)
    print("play history", play_history)
    print("current position", current_position)

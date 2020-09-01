from random import randint

# --- Creates a list of player, depending on the amount of players entered --- #
def player_list(players):
    players = []
    for number in range(1, players + 1):
        player_name = 'Player ' + str(number)
        players.append(player_name)
    return players

# --- Allows you to pick from a list of revolvers, which will be used in the storyline. --- #
def revolver_selection(revolver_name):
    revolvers = ['.44 Magnum', 'Nagant M1895', '.357 Magnum']
    if revolver_name in revolvers:
        print('Your revolver has been chosen. Your revolver is: ' + revolver_name + '.')
        return revolver_name
    else:
        print('That revolver doesn\'t exist. Try the following - \'.44 Magnum\', \'Nagant M1895\', \'.357 Magnum\'')
        return 


# --- Sets a 'storyline' for the game, including the revolver you picked above. --- #
def storyline(time_in_day, place_in_game):
    lower_time_in_day = time_in_day.lower()
    lower_place_in_game = place_in_game.lower()

    if len(list_of_players) == 1:
        if lower_time_in_day == 'day' and lower_place_in_game == 'kitchen':
            try:
                print('It is daytime. The sun is shining outside. It is a pleasant and warm day with a small, fresh breeze.\nYou are alone in the kitchen. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette.')
            except TypeError:
                print('You entered an invalid revolver!')
        elif lower_time_in_day == 'day' and lower_place_in_game == 'bar':
            try:
                print('It is daytime. The sun is shining outside. It is a pleasant and warm day with a small, fresh breeze.\nYou are alone in the back of the bar. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette.')
            except TypeError:
                print('You entered an invalid revolver!')
        elif lower_time_in_day == 'night' and lower_place_in_game == 'kitchen':
            try:
                print('It is nighttime. It is dark outside. The roads are lit up with street lights.\nYou are alone in the kitchen. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette.')
            except TypeError:
                print('You entered an invalid revolver!')
        elif lower_time_in_day == 'night' and lower_place_in_game == 'bar':
            try:
                print('It is nighttime. It is dark outside. The roads are lit up with street lights.\nYou are alone in the back of the bar. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette.')
            except TypeError:
                print('You entered an invalid revolver!')
        else:
            print('Something went wrong. The options available for time are \'day\' and \'night\' and the options available for place are \'kitchen\' and \'bar\'. Try again!')
            
    elif len(list_of_players) > 1:
        if lower_time_in_day == 'day' and lower_place_in_game == 'kitchen':
            try:
                print('It is daytime. The sun is shining outside. It is a pleasant and warm day with a small, fresh breeze.\nYou are with your friends in the kitchen. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette with your friends.')
            except TypeError:
                print('You entered an invalid revolver!')
        elif lower_time_in_day == 'day' and lower_place_in_game == 'bar':
            try:
                print('It is daytime. The sun is shining outside. It is a pleasant and warm day with a small, fresh breeze.\nYou are with your friends in the back of the bar. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette with your friends.')
            except TypeError:
                print('You entered an invalid revolver!')
        elif lower_time_in_day == 'night' and lower_place_in_game == 'kitchen':
            try:
                print('It is nighttime. It is dark outside. The roads are lit up with street lights.\nYou are with your friends in the kitchen. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette with your friends.')
            except TypeError:
                print('You entered an invalid revolver!')
        elif lower_time_in_day == 'night' and lower_place_in_game == 'bar':
            try:
                print('It is nighttime. It is dark outside. The roads are lit up with street lights.\nYou are with your friends in the back of the bar. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette with your friends.')
            except TypeError:
                print('You entered an invalid revolver!')
        else:
            print('Something went wrong. The options available for time are \'day\' and \'night\' and the options available for place are \'kitchen\' and \'bar\'. Try again!')





list_of_players = player_list(4)
#print(list_of_characters)
revolver_choice = revolver_selection('.44 Magnum')
#print(revolver_choice)
storyline('day', 'kitchen')


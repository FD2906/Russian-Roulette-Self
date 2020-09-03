import random

# --- Creates a list of player, depending on the amount of players entered --- #
def player_list(players_count):
    players = []
    for number in range(1, players_count + 1):
        player_name = 'Player ' + str(number)
        players.append(player_name)
    return players


# --- An alternative list can be called here, if people are playing this game and they want to choose their own names. --- #
# --- Enter names here and uncomment this line, and comment/cut the above function. --- #

# list_of_players = ['Frank']


# --- Allows you to pick from a list of revolvers, which will be used in the storyline and the game --- #
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


# --- The main game function, takes in a list of players, the choice of revolver, and the number of rounds to be played (one round is all of the players firing once). --- #
def russian_roulette(list_of_players, revolver_choice, num_of_rounds):
    number_of_players_remaining = len(list_of_players)
    total_rounds = len(list_of_players) * num_of_rounds
    rounds_to_be_played = 0

    try:
        while number_of_players_remaining != 0 and rounds_to_be_played < total_rounds:
            for player in list_of_players:
                bullet_in_cylinder = random.randint(1, 6)
                print('\n' + player + ' takes the ' + revolver_choice + ', spins the cylinder, and takes aim.')
                if bullet_in_cylinder != 1:
                    print('The gun goes off, but doesn\'t kill ' + player + '. ' + player + ' survives to live another day.\n')
                    rounds_to_be_played += 1
                else:
                    print('The gun kills ' + player + '. ' + player + ' is dead.\n')
                    list_of_players.remove(player)
                    rounds_to_be_played += 1

        surviving_players = ''
        temp_counter = 0
        for player in list_of_players:
            surviving_players = surviving_players + player
            temp_counter += 1
            if temp_counter == len(list_of_players):
                surviving_players += '.'
            else:
                surviving_players += ', '

        print('At the end of the game, the players that survived are: ' + surviving_players)
    except TypeError:
        print('Because a revolver was not chosen, the game doesn\'t work. Just like real life, you can\'t play Russian Roulette without a gun, right?')




# Chooses how many players you want to play in the game.
list_of_players = player_list(4)
# Or if a list of names was entered, comment the above line.

# Selects which revolver you want to use; pick from the three options: '.44 Magnum', '.357 Magnum', 'Nagant M1895'
revolver_choice = revolver_selection('.44 Magnum')
#print(revolver_choice)

# Sets a storyline for the game. Pick a choice out of two times - 'day' or 'night', and place - 'kitchen' or 'bar'
storyline('day', 'kitchen')

# Starts the game. The final argument lets you select how many rounds you want to play.
russian_roulette(list_of_players, revolver_choice, 2)

